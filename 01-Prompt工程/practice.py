"""
01 - Prompt 工程练习

先完成 00-准备工作，确保 hello.py 能跑通。
把下面的 BASE_URL / MODEL 换成你自己的，然后逐个补全 TODO。
每次补完一个就运行：python practice.py
"""
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["LLM_API_KEY"],
    base_url="https://api.deepseek.com",  # TODO: 换成你用的平台地址
)
MODEL = "deepseek-chat"  # TODO: 换成你用的模型名


def ask(prompt: str, system: str = "你是一个有帮助的助手。") -> str:
    resp = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": prompt},
        ],
    )
    return resp.choices[0].message.content


review = """这个台灯颜值很高，放在桌上很好看，
但是灯光有点暗，晚上看书不太够，充电线也很短。
客服态度倒是不错，问问题回复很快。"""


# ============ TODO 1：烂 prompt vs 好 prompt ============
# 先用一句话让模型总结这条评价，再写一个详细版（指定：分优点/缺点/一句话总结）
# 对比两次输出，哪个更好？为什么？
print("=== TODO 1 ===")
bad_prompt = review  # TODO: 先试试只扔原文，不加任何指令
# good_prompt = ...  # TODO: 写一个详细的指令版本
print(ask(bad_prompt))


# ============ TODO 2：用分隔符圈定内容 ============
# 把"指令"和"评价原文"用 """ 分开写，让模型只总结分隔符里的内容
print("\n=== TODO 2 ===")
# prompt2 = f"""..."""  # TODO: 补全
# print(ask(prompt2))


# ============ TODO 3：按 JSON 格式输出 ============
# 要求模型输出 JSON，包含三个字段：优点（列表）、缺点（列表）、评分（1-5分）
print("\n=== TODO 3 ===")
# prompt3 = ...  # TODO: 补全
# print(ask(prompt3))


# ============ TODO 4：给模型看一个例子 ============
# 先给一个"评价 -> 理想总结"的例子，再让它处理上面的 review
print("\n=== TODO 4 ===")
# prompt4 = ...  # TODO: 补全
# print(ask(prompt4))


# ============ TODO 5：先思考，再回答 ============
# 让模型先列出"这条评价提到了哪几个方面"，再给出总结
print("\n=== TODO 5 ===")
# prompt5 = ...  # TODO: 补全
# print(ask(prompt5))
