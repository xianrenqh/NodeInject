#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试脚本 - 验证许可证生成算法
"""

import random

LICENSE_CHARS = "L23456789ABCDEFGHJKMNPQRSTUVWXYZ"


def generate_license_detailed() -> tuple:
    """
    生成许可证并返回详细信息用于验证
    """
    # 生成 22 位随机字符
    license_chars = list(random.choices(LICENSE_CHARS, k=22))
    license_str = ''.join(license_chars)

    print(f"基础字符 (22位): {license_str}")
    print(f"长度: {len(license_str)}")

    # 计算并添加 2 个校验位
    checksums = []
    for n in range(2):
        o = 0
        print(f"\n校验位 {n+1} 计算:")
        for i in range(0, 16, 2):
            char = license_str[n + i]
            idx = LICENSE_CHARS.index(char)
            o += idx
            print(f"  位置 {n+i}: '{char}' -> 索引 {idx}, 累计 {o}")

        o %= len(LICENSE_CHARS)
        checksum_char = LICENSE_CHARS[o]
        checksums.append(checksum_char)
        print(f"  最终: {o} % {len(LICENSE_CHARS)} = {o} -> '{checksum_char}'")
        license_str += checksum_char

    print(f"\n添加校验位后 (24位): {license_str}")
    print(f"长度: {len(license_str)}")

    # 添加分隔符
    license_list = list(license_str)
    license_list.insert(6, '-')
    license_list.insert(13, '-')
    license_list.insert(20, '-')

    final_license = ''.join(license_list)
    print(f"\n最终许可证: {final_license}")
    print(f"格式: XXXXXX-XXXXXX-XXXXXX-XXXX")

    return final_license


if __name__ == "__main__":
    print("=" * 60)
    print("许可证生成算法验证")
    print("=" * 60)
    print()

    # 设置随机种子以便复现
    random.seed(42)

    license_key = generate_license_detailed()

    print("\n" + "=" * 60)
    print("验证要点:")
    print("1. 基础字符 22 位")
    print("2. 添加 2 位校验码 = 24 位")
    print("3. 插入 3 个分隔符 = 27 位")
    print(f"4. 最终长度: {len(license_key)} (应该为 27)")
    print("=" * 60)
