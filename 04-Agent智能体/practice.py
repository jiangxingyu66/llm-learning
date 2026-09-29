"""
04 - Agent 智能体练习

逐个补全 TODO，运行：python practice.py
"""
import os
import re
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["LLM_API_KEY"],
    base_url="https://api.deepseek.com",  # TODO: 换成你用的平台地址
)
MODEL = "deepseek-chat"  # TODO: 换成你用的模型名


# ============ TODO 1：定义工具 ============
# 工具就是带清楚说明的普通函数
def calculator(expression: str) -> str:
    """计算数学表达式，比如 calculator("2+3*4")"""
    # TODO: 用 eval 计算 expression，try/except 包住，出错返回"计算失败"
    return "TODO"


def get_weather(city: str) -> str:
    """查询天气，比如 get_weather("北京")"""
    # TODO: 先返回假数据："北京：晴，15度"。以后可以接真实天气 API
    return "TODO"


TOOLS = {"calculator": calculator, "get_weather": get_weather}


# ============ TODO 2：手写 ReAct 循环 ============
def run_agent(task: str, max_steps: int = 5) -> str:
    system = """你是一个智能助手，可以调用以下工具：
- calculator(表达式)：计算数学，比如 calculator(2+3*4)
- get_weather(城市)：查询天气，比如 get_weather(北京)

每轮你只能做一件事，用下面格式回复：
思考：<你这一步在想什么>
行动：<工具名(参数)>  或  完成：<最终答案>

收到工具结果后继续，直到输出"完成："。
"""
    messages = [
        {"role": "system", "content": system},
        {"role": "user", "content": task},
    ]
    # TODO: 写循环（最多 max_steps 轮）：
    #   1. 调用模型，拿到回复，打印出来
    #   2. 如果回复里有"完成："，返回最终答案，结束
    #   3. 否则用正则从"行动："里提取 工具名 和 参数，比如 calculator(2+3)
    #      提示：re.search(r"(\w+)\((.*)\)", 行)
    #   4. 真的调用 TOOLS[工具名](参数)，拿到结果
    #   5. 把"工具返回：<结果>"追加到 messages，继续下一轮
    return "TODO: 补全循环"


# ============ TODO 3：跑一个真实任务 ============
print("=== TODO 3 ===")
# TODO: 取消下面注释，运行并观察 Agent 的每一步
# answer = run_agent("北京现在天气怎么样？15+27 等于多少？")
# print("最终答案：", answer)


# ============ TODO 4（可选）：加新工具 ============
# TODO: 加一个 search_notes(关键词) 工具，能从下面的 notes 里搜内容
# 然后在 system 里告诉模型有这个新工具，出题考它："报销流程是什么？"
notes = [
    "报销流程：先在 OA 系统提交申请，附上发票照片，部门经理审批后 3 个工作日内到账。",
    "年会定在 12 月 20 日晚上 6 点，三楼宴会厅。",
]
