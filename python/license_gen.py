#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
License Generator - 许可证生成器
生成 Typora 格式的许可证密钥
"""

import random
import string

# 许可证字符集（排除容易混淆的字符：0, 1, I, O）
LICENSE_CHARS = "L23456789ABCDEFGHJKMNPQRSTUVWXYZ"


def generate_license() -> str:
    """
    生成许可证密钥

    算法说明：
    1. 随机生成 22 位基础字符
    2. 添加 2 位校验码（基于特定位置的字符计算）
    3. 格式化为 XXXXXX-XXXXXX-XXXXXX-XXXX 格式

    Returns:
        格式化的许可证字符串
    """
    # 生成 22 位随机字符
    license_chars = list(random.choices(LICENSE_CHARS, k=22))
    license_str = ''.join(license_chars)

    # 计算并添加 2 个校验位
    for n in range(2):
        o = 0
        # 从位置 n 开始，每隔 2 个字符取一个，共取 8 个字符
        for i in range(0, 16, 2):
            char = license_str[n + i]
            o += LICENSE_CHARS.index(char)

        # 取模得到校验字符
        o %= len(LICENSE_CHARS)
        license_str += LICENSE_CHARS[o]

    # 添加分隔符
    # 原始: 24 个字符
    # 格式: XXXXXX-XXXXXX-XXXXXX-XXXX
    #       012345 6 789012 3 456789 0 1234
    license_list = list(license_str)
    license_list.insert(6, '-')   # 第 7 位插入
    license_list.insert(13, '-')  # 第 14 位插入（原第 13 位）
    license_list.insert(20, '-')  # 第 21 位插入（原第 18 位）

    return ''.join(license_list)


def main():
    """主函数"""
    print("=" * 50)
    print("License Generator - Typora 许可证生成器")
    print("=" * 50)
    print()

    license_key = generate_license()

    print(f"🔑 你的许可证: {license_key}")
    print()
    print("=" * 50)
    print("请在 Typora 中填入此许可证")
    print("=" * 50)


if __name__ == "__main__":
    main()
