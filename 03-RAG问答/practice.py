"""
03 - RAG 问答练习

逐个补全 TODO，运行：python practice.py
"""
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["LLM_API_KEY"],
    base_url="https://api.deepseek.com",  # TODO: 换成你用的平台地址
)
MODEL = "deepseek-chat"  # TODO: 换成你用的模型名

# 假装这是你的"私有文档"（以后可以换成读真实文件）
documents = [
    "公司年会定在 12 月 20 日晚上 6 点，在三楼宴会厅举行，请大家准时参加。",
    "报销流程：先在 OA 系统提交申请，附上发票照片，部门经理审批后 3 个工作日内到账。",
    "Python 学习路线：先学基础语法，再学 requests 爬虫，最后学 Django 做网站。",
    "台灯使用说明：长按 3 秒开机，短按切换三档亮度，充电时指示灯为红色。",
]


# ============ TODO 1：文档切分 ============
# 写一个函数 chunk_text(text, size=100)，把长文本按 size 个字切成小段
# 然后对 documents 里每一段调用它，得到 chunks 列表并打印
print("=== TODO 1 ===")
# def chunk_text(text, size=100):
#     ...
# chunks = []
# for doc in documents:
#     chunks.extend(chunk_text(doc))
# print(f"共切出 {len(chunks)} 个片段")


# ============ TODO 2：关键词检索 ============
# 写一个函数 retrieve(question, chunks)，返回包含问题中任意 2 个以上汉字的片段
# 提示：先对问题分词（最土的办法：逐字），再统计每个 chunk 命中了几个字
print("\n=== TODO 2 ===")
# def retrieve(question, chunks):
#     ...
# hits = retrieve("年会什么时候开？", chunks)
# print("检索到的片段：", hits)


# ============ TODO 3：拼出完整 RAG ============
# 写一个函数 rag_answer(question)：
#   1. 调用 retrieve 找到相关片段
#   2. 拼 prompt："参考以下资料回答问题，如果资料里没有就说不知道。\n资料：...\n问题：..."
#   3. 调用模型，返回答案
# 对比：直接问模型"年会什么时候开？" vs 用 RAG 问，答案有什么区别？
print("\n=== TODO 3 ===")
# def rag_answer(question):
#     ...
# print("直接问：", ask_direct("我们公司年会什么时候开？"))
# print("RAG 问：", rag_answer("我们公司年会什么时候开？"))


# ============ TODO 4（可选）：向量检索 ============
# 调用 embedding 接口，把 chunks 和问题都变成向量，用余弦相似度找最相关的片段
# 替换掉 TODO 2 的关键词检索，对比两种检索方式的效果
