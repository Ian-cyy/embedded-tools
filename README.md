# embedded-tools

嵌入式和机器人项目里复用的常用小工具（纯 Python，与固件端实现逐位一致）。

## 内容

- `tools.py`
  - `crc16_ccitt`：CRC16-CCITT（poly 0x1021 / init 0xFFFF），支持增量累加（整包校验）
  - `crc8`：CRC8（poly 0x07），用于板间二进制协议帧校验
- `test_tools.py`：标准校验值、增量校验一致性、单 bit 检错能力测试

## 测试

```bash
pip install pytest
python -m pytest -q
```

## CI

GitHub Actions：每次 push 自动安装环境并执行 `pytest`，结果见仓库 Actions 页。
