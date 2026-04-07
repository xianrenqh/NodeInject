# NodeInject

适用于 Typora v1.9.5 及以前版本

> ⚠️ 仅用于学习目的

## 版本选择

本项目提供两个版本：

### 🦀 Rust 版本
- 编译为独立可执行文件
- 无需运行时依赖
- 适合分发

### 🐍 Python 版本（推荐）
- 开箱即用，无需编译
- 支持 `--force` 和 `--clean` 参数
- 自动备份原始文件
- 跨平台支持
- **查看详细文档**: [python/PYTHON_USAGE.md](python/PYTHON_USAGE.md)

---

## Rust 版本

### 构建

需要 Rust 开发环境，在根目录和 license-gen 目录下分别执行构建命令得到 node_inject.exe 和 license-gen.exe 程序。

```bash
# 构建 node_inject
cargo build

# 构建 license-gen
cd license-gen
cargo build
```

### 使用

将生成的 `\target\debug` 目录中的 `node_inject.exe` 和 `license-gen.exe` 复制到 Typora 安装目录下执行

```bash
# 以管理员身份运行
.\node_inject.exe

# 生成许可证
.\license-gen.exe
```

最终在 Typora 中填入生成的 License 就行了。

---

## Python 版本

### 快速开始

```powershell
# 1. 安装依赖
pip install asar

# 2. 进入 Typora 安装目录
cd "D:\Program Files\Typora"

# 3. 注入 Hook（首次）
python node_inject.py

# 强制重新注入
# python node_inject.py --force

# 4. 生成许可证
python license_gen.py

# 5. 启动 Typora 并输入许可证
```

### 常用命令

```bash
# 首次注入
python node_inject.py

# 强制重新注入
python node_inject.py --force

# 清理注入（恢复原始文件）
python node_inject.py --clean

# 生成许可证
python license_gen.py
```

> 📖 **完整文档**: 查看 [python/PYTHON_USAGE.md](python/PYTHON_USAGE.md)

---

## 常见问题

### Q: 提示 "你可能已经安装过 hook"
**A:** 使用 `--force` 参数重新注入（Python 版本）或手动删除 `node` 目录

### Q: 注入后仍然未激活
**A:**
1. 确认 Typora 版本 ≤ v1.9.5
2. 确认以管理员权限运行
3. 确认关闭 Typora 后再注入
4. 尝试重新注入

### Q: 如何恢复原始文件
**A:** Python 版本使用 `--clean` 参数，或从备份文件 `node_modules.asar.bak` 恢复


### Thank
https://github.com/DiamondHunters/NodeInject
