# 00 - 准备工作

目标：让你的电脑能跑通第一行"调用大模型"的代码。

## 分步任务

### 第 1 步：安装 Python
- 去 python.org 下载安装 **Python 3.10 或更高版本**
- 安装完打开终端（Windows 按 `Win+R` 输入 `cmd`），输入 `python --version`，能看到版本号就行

### 第 2 步：准备一个大模型 API Key
吴恩达课程里用的是 OpenAI 的接口。你可以用任何**兼容 OpenAI 接口**的服务，比如：
- DeepSeek（便宜，国内可直接用）
- 通义千问 / 智谱 / Kimi（都有兼容接口）
- OpenAI 官方（需要境外网络）

去对应平台注册 → 找到 "API Key" → 创建一个，复制保存好。

> ⚠️ API Key 等于你的账号密码，**不要发给任何人，也不要写进代码里**。

### 第 3 步：安装依赖
在终端里运行：
```bash
pip install openai
```

### 第 4 步：把 Key 存成环境变量（不要写进代码）
- Windows（cmd）：`setx LLM_API_KEY "你的key"`
- Mac/Linux：`export LLM_API_KEY="你的key"`（加到 `~/.bashrc` 或 `~/.zshrc` 永久生效）

### 第 5 步：跑通验证代码
把下面的代码存成 `hello.py`，运行 `python hello.py`。如果模型回复了你，环境就通了。

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["LLM_API_KEY"],
    base_url="https://api.deepseek.com",  # 换成你用的平台地址
)

resp = client.chat.completions.create(
    model="deepseek-chat",  # 换成你用的模型名
    messages=[{"role": "user", "content": "你好，你是谁？"}],
)
print(resp.choices[0].message.content)
```

## 完成标准
- [ ] `python hello.py` 能打印出模型的回复
- [ ] 你的 Key 只存在环境变量里，代码里没有出现

卡住了就把报错截图发给我。
