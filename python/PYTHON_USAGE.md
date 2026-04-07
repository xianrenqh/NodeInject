# Python 版本使用说明

## 环境要求

- Python 3.7+
- 依赖包：`asar`

## 安装依赖

```bash
pip install -r requirements.txt
```

## 使用方法

### 1. 注入 Hook

```bash
python node_inject.py
```

### 2. 生成许可证

```bash
python license_gen.py
```

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

## 注意事项

1. 运行 `node_inject.py` 前，请确保在 Typora 安装目录下
2. 需要备份原始的 `node_modules.asar` 文件
3. hook.js 文件需要与脚本在同一目录或子目录
