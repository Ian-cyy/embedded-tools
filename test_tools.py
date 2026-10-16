# -*- coding: utf-8 -*-
from tools import crc8, crc16_ccitt


def test_crc16_ccitt_check_value():
    # CRC-16/CCITT-FALSE 标准校验值
    assert crc16_ccitt(b"123456789") == 0x29B1


def test_crc16_ccitt_incremental():
    # 分帧累加 == 整包一次算（IAP 整包校验的用法）
    acc = crc16_ccitt(b"123")
    acc = crc16_ccitt(b"456789", init=acc)
    assert acc == crc16_ccitt(b"123456789")


def test_crc8_check_value():
    # CRC-8（poly 0x07）标准校验值
    assert crc8(b"123456789") == 0xF4


def test_crc8_detects_single_bit_error():
    data = bytes([0xAA, 0x55, 0x01, 0x02])
    bad = bytes([0xAA, 0x55, 0x01, 0x03])
    assert crc8(data) != crc8(bad)


def test_crc16_detects_single_bit_error():
    data = b"\xfe\xee\x10\x00\x00\x97\x01"
    bad = b"\xfe\xee\x10\x00\x00\x97\x03"
    assert crc16_ccitt(data) != crc16_ccitt(bad)
