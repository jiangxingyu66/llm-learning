"""
02 - 调用大模型 API 练习

逐个补全 TODO，运行：python practice.py
"""
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["LLM_API_KEY"],
    base_url="https://api.deepseek.com",  # TODO: 换成你用的平台地址
)
MODEL = "deepseek-chat"  # TODO: 换成你用的模型名


# ============ TODO 1：改 system，看风格变化 ============
print("=== TODO 1 ===")
resp = client.chat.completions.create(
    model=MODEL,
    messages=[
        {"role": "system", "content": "你是一个有帮助的助手。"},  # TODO: 改成"严格的语文老师"再跑一次
        {"role": "user", "content": "介绍一下你自己"},
    ],
)
print(resp.choices[0].message.content)


# ============ TODO 2：多轮对话（记住上下文）============
print("\n=== TODO 2 ===")
messages = [{"role": "system", "content": "你是一个有帮助的助手。"}]
# TODO: 写一个循环：读用户输入 -> 追加到 messages -> 调用 API -> 打印回复 -> 把回复也追加到 messages
# 先问"我叫小明"，再问"我叫什么"，验证模型记住了
# 提示：输入 "quit" 时退出循环
# while True:
#     ...


# ============ TODO 3：temperature 对比 ============
print("\n=== TODO 3 ===")
# TODO: 用 prompt="给一只猫起个名字"，分别用 temperature=0 和 temperature=1.2 各跑 3 次
# 把结果打印出来对比，想想：写代码用哪个？写诗用哪个？
# for temp in [0, 1.2]:
#     ...


# ============ TODO 4：流式输出 ============
print("\n=== TODO 4 ===")
# TODO: 加上 stream=True，用 for chunk in resp 逐块打印，实现打字机效果
# 注意：stream=True 时 resp 不是直接拿 .choices[0].message，要遍历 chunk
# stream_resp = client.chat.completions.create(..., stream=True)
# for chunk in stream_resp:
#     ...


# ============ TODO 5：强制 JSON 输出 ============
print("\n=== TODO 5 ===")
# TODO: 加上 response_format={"type": "json_object"}，
# 让模型把"推荐三本 Python 入门书（书名、作者、一句话推荐理由）"输出成 JSON
# resp = client.chat.completions.create(
#     model=MODEL,
#     response_format={"type": "json_object"},
#     messages=[...],
# )
# print(resp.choices[0].message.content)
