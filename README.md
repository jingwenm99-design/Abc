# 中英文翻译器 / Chinese-English Translator

这是一个轻量级命令行中英文翻译器。

## 功能

- 支持中文 -> 英文翻译
- 支持英文 -> 中文翻译
- 支持自动识别语言方向（`auto`）

## 使用方式

```bash
python3 translator.py "你好"
python3 translator.py "thank you"
python3 translator.py "早上好" --direction zh-en
python3 translator.py "good evening" --direction en-zh
```

## 说明

当前版本使用内置词典进行翻译，适合作为示例和基础版本。
后续你可以扩展词库，或者接入第三方翻译 API（如 OpenAI、Google、DeepL）。
