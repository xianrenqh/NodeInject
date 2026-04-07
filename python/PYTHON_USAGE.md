# Python 版本使用说明

> 仅用于学习目的

## 环境要求

- Python 3.7+
- 依赖包：`asar`

## 安装依赖

```bash
pip install -r requirements.txt
```

## 使用方法

### 准备工作

需要将以下 3 个文件一起复制到 **Typora 安装目录**：
- `node_inject.py`
- `license_gen.py`
- `hooklog.js`

> 💡 典型路径：`D:\Program Files\Typora` 或 `C:\Program Files\Typora`

### 1. 注入 Hook

在 **Typora 安装目录**下运行（需要管理员权限）：

```bash
# 首次注入
python node_inject.py

# 强制重新注入（如果已经注入过）
python node_inject.py --force
# 或
python node_inject.py -f

# 清理注入（恢复原始文件）
python node_inject.py --clean
# 或
python node_inject.py -c
```

**命令参数说明：**
- `--force` / `-f`: 强制重新安装，自动删除旧的注入文件并重新注入
- `--clean` / `-c`: 清理注入，恢复备份的原始文件并删除 node 目录

### 2. 生成许可证

```bash
python license_gen.py
```

会生成一个格式如 `XXXXXX-XXXXXX-XXXXXX-XXXX` 的许可证密钥。

### 3. 激活 Typora

1. 启动 Typora
2. 在激活窗口中输入生成的许可证
3. 完成激活

## 与原 Rust 版本的功能对比

| 功能 | Rust 版本 | Python 版本 | 状态 |
|------|-----------|-------------|------|
| 解压 ASAR | ✅ rasar | ✅ asar | 完全一致 |
| 嵌入 hook.js | ✅ include_bytes! | ✅ 运行时读取 | 完全一致 |
| 写入 hook.js | ✅ | ✅ | 完全一致 |
| 注入 require | ✅ | ✅ | 完全一致 |
| 重新打包 ASAR | ✅ rasar | ✅ asar | 完全一致 |
| 许可证生成 | ✅ random-string | ✅ random | 完全一致 |
| 校验算法 | ✅ | ✅ | 完全一致 |
| 格式化输出 | ✅ | ✅ | 完全一致 |

## 跨平台支持

Python 版本天然支持跨平台：
- ✅ Windows
- ✅ Linux
- ✅ macOS

无需交叉编译，直接运行即可！

## 打包为可执行文件（可选）

### Windows
```bash
pip install pyinstaller
pyinstaller --onefile node_inject.py
pyinstaller --onefile license_gen.py
```

### Linux
```bash
pip install pyinstaller
pyinstaller --onefile node_inject.py
pyinstaller --onefile license_gen.py
```

生成的可执行文件在 `dist/` 目录下。

## 完整使用流程示例

### Windows (PowerShell)

```powershell
# 1. 以管理员身份打开 PowerShell

# 2. 进入 Typora 安装目录
cd "D:\Program Files\Typora"

# 3. 注入 Hook（首次）
python node_inject.py

# 如果需要重新注入
# python node_inject.py --force

# 4. 生成许可证
python license_gen.py

# 5. 启动 Typora 并输入许可证
.\Typora.exe
```

### 常见问题

#### Q1: 提示 "你可能已经安装过 hook"
**A:** 使用 `--force` 参数重新注入：
```bash
python node_inject.py --force
```

#### Q2: 想恢复原始文件
**A:** 使用 `--clean` 参数：
```bash
python node_inject.py --clean
```

#### Q3: 注入后仍然未激活
**A:** 检查以下几点：
1. 确认 Typora 版本 ≤ v1.9.5
2. 确认以管理员权限运行
3. 确认关闭 Typora 后再注入
4. 尝试 `--force` 重新注入
5. 检查是否输入了正确的许可证

#### Q4: 提示找不到 node_modules.asar
**A:** 确认脚本放在 Typora 安装目录下（与 `Typora.exe` 同一目录）

## 注意事项

1. ⚠️ **必须**将 `node_inject.py`、`license_gen.py` 和 `hooklog.js` 三个文件一起复制到 Typora 安装目录
2. ⚠️ **必须**在 Typora 安装目录下运行脚本（与 `Typora.exe` 同一目录）
3. ⚠️ 运行前请确保 **Typora 已关闭**
4. ⚠️ 需要 **管理员权限**（如果 Typora 安装在 Program Files）
5. ⚠️ 适用于 Typora v1.9.5 及以前版本
6. ⚠️ 脚本会自动备份原始文件为 `node_modules.asar.bak`
7. 💡 如果注入失败，可以使用 `--clean` 参数恢复
8. 💡 建议首次使用后测试激活，确认成功后再关闭日志输出
9. 仅用于学习目的
