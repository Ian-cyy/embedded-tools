# -*- coding: utf-8 -*-
"""嵌入式常用校验工具（纯 Python）。

与固件端实现保持逐位一致的版本，用于上位机脚本 / 自动化测试做数据校验。
"""


def crc16_ccitt(data: bytes, init: int = 0xFFFF) -> int:
    """CRC16-CCITT（poly 0x1021，初值 0xFFFF）。

    与 STM32 固件端 IAP / 串口协议实现一致；
    支持传入上一次结果做增量累加（整包 CRC 场景）。
    """
    crc = init
    for byte in data:
        crc ^= byte << 8
        for _ in range(8):
            if crc & 0x8000:
                crc = ((crc << 1) ^ 0x1021) & 0xFFFF
            else:
                crc = (crc << 1) & 0xFFFF
    return crc


def crc8(data: bytes, poly: int = 0x07, init: int = 0x00) -> int:
    """CRC8（poly 0x07），用于板间二进制协议帧校验。"""
    crc = init
    for byte in data:
        crc ^= byte
        for _ in range(8):
            if crc & 0x80:
                crc = ((crc << 1) ^ poly) & 0xFF
            else:
                crc = (crc << 1) & 0xFF
    return crc
