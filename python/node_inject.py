#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NodeInject Python 版本
适用于 Typora v1.9.5 及以前版本
"""

import os
import sys
import shutil
from pathlib import Path

try:
    import asar
except ImportError:
    print("错误: 需要安装 asar 模块")
    print("请运行: pip install asar")
    sys.exit(1)

# 配置常量
HOOK_JS_WRITE_PATH = "./node/raven/hook.js"
INJECT_JS_PATH = "./node/raven/index.js"
NO_EMBED_HOOK_JS_PATH = "./hook.js"

# 嵌入的 hook.js 内容（从 hooklog.js 读取）
EMBED_HOOK_JS_CONTENT = None


def load_embedded_hook_js():
    """加载嵌入的 hook.js 内容"""
    global EMBED_HOOK_JS_CONTENT
    if EMBED_HOOK_JS_CONTENT is None:
        hook_js_path = Path(__file__).parent / "hooklog.js"
        if hook_js_path.exists():
            EMBED_HOOK_JS_CONTENT = hook_js_path.read_bytes()
        else:
            print(f"警告: 找不到 {hook_js_path}")
            EMBED_HOOK_JS_CONTENT = b""


def file_exist(path: str) -> bool:
    """检查文件或目录是否存在"""
    return Path(path).exists()


def write_js_to_file(use_external: bool = False):
    """写入 hook.js 文件"""
    if use_external:
        # 从外部文件读取
        if not file_exist(NO_EMBED_HOOK_JS_PATH):
            print(f"错误: 找不到 {NO_EMBED_HOOK_JS_PATH}")
            sys.exit(1)
        with open(NO_EMBED_HOOK_JS_PATH, 'rb') as f:
            content = f.read()
    else:
        # 使用嵌入的内容
        load_embedded_hook_js()
        content = EMBED_HOOK_JS_CONTENT

    # 确保目录存在
    os.makedirs(os.path.dirname(HOOK_JS_WRITE_PATH), exist_ok=True)

    with open(HOOK_JS_WRITE_PATH, 'wb') as f:
        f.write(content)
    print(f"✓ 已写入 {HOOK_JS_WRITE_PATH}")


def append_require_to_file():
    """在 index.js 末尾添加 require 语句"""
    with open(INJECT_JS_PATH, 'a', encoding='utf-8') as f:
        f.write("\nrequire('./hook')")
    print(f"✓ 已添加 require 到 {INJECT_JS_PATH}")


def main():
    """主函数"""
    import argparse

    parser = argparse.ArgumentParser(
        description='NodeInject - Typora Hook 注入工具')
    parser.add_argument('--force', '-f', action='store_true',
                        help='强制重新安装（删除已存在的 node 目录）')
    parser.add_argument('--clean', '-c', action='store_true',
                        help='清理注入（恢复备份并删除 node 目录）')
    args = parser.parse_args()

    print("=" * 50)
    print("NodeInject - Typora Hook 注入工具")
    print("=" * 50)

    # 清理模式
    if args.clean:
        print("\n🧹 清理模式：恢复原始文件...")
        backup_path = "./resources/node_modules.asar.bak"
        if file_exist(backup_path):
            if file_exist("./resources/node_modules.asar"):
                os.remove("./resources/node_modules.asar")
            shutil.copy2(backup_path, "./resources/node_modules.asar")
            print("✓ 已恢复原始 node_modules.asar")

        if file_exist("./node"):
            shutil.rmtree("./node")
            print("✓ 已删除 node 目录")

        print("\n✅ 清理完成！")
        return

    # 检查是否已安装
    if file_exist("./node"):
        if args.force:
            print("\n🔄 强制模式：删除已存在的 node 目录...")
            shutil.rmtree("./node")
            print("✓ 已删除")
            # 恢复原始备份
            backup_path = "./resources/node_modules.asar.bak"
            if file_exist(backup_path) and file_exist("./resources/node_modules.asar"):
                os.remove("./resources/node_modules.asar")
                shutil.copy2(backup_path, "./resources/node_modules.asar")
                print("✓ 已恢复原始备份")
        else:
            print("\n⚠ 检测到已安装的 hook")
            print("选项：")
            print("  1. 使用 --force 或 -f 参数强制重新安装")
            print("  2. 使用 --clean 或 -c 参数清理注入")
            print("  3. 手动删除 node 目录后重新运行")
            return

    # 检查 ASAR 文件是否存在
    if not file_exist("./resources/node_modules.asar"):
        print("❌ 错误: 找不到 node_modules.asar")
        print("请将此程序放到 Typora 安装目录下")
        print("（与 Electron 可执行文件在同一目录）")
        return

    try:
        # 1. 备份原始 ASAR
        print("\n📦 步骤 1/5: 备份 node_modules.asar...")
        backup_path = "./resources/node_modules.asar.bak"
        if not file_exist(backup_path):
            shutil.copy2("./resources/node_modules.asar", backup_path)
            print("✓ 备份完成")
        else:
            print("✓ 备份已存在，跳过")

        # 2. 解压 ASAR
        print("\n📦 步骤 2/5: 解压 node_modules.asar...")
        asar.extract_all("./resources/node_modules.asar", "./node")
        print("✓ 解压完成")

        # 3. 写入 hook.js
        print("\n📝 步骤 3/5: 添加 hook.js...")
        write_js_to_file()

        # 4. 注入 require 语句
        print("\n🔧 步骤 4/5: 应用补丁...")
        append_require_to_file()

        # 5. 删除原始 ASAR 并重新打包
        print("\n📦 步骤 5/5: 重新打包 node_modules.asar...")
        os.remove("./resources/node_modules.asar")
        asar.create_package("./node", "./resources/node_modules.asar")
        print("✓ 打包完成")

        print("\n" + "=" * 50)
        print("✅ 全部完成！")
        print("=" * 50)

    except Exception as e:
        print(f"\n❌ 错误: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
