from sparkai.llm.llm import ChatSparkLLM, ChunkPrintHandler
from sparkai.core.messages import ChatMessage

# ================= 替换成你控制台获取的凭证 =================
SPARKAI_URL = 'wss://spark-api.xf-yun.com/chat/pro-128k'  # 星火Max模型地址
SPARKAI_APP_ID = "74220d96"
SPARKAI_API_KEY = "62198ca16e3930fb054d96a2ff3c3e02"
SPARKAI_API_SECRET = "YjIxNTU3ZDcxMjEyNDU0YWQ1MzZlNzRk"
SPARKAI_DOMAIN = "Spark Pro-128K"  # 和URL对应，v3.5模型固定generalv3.5



        # 1. 初始化大模型客户端

spark = ChatSparkLLM(
        spark_api_url=SPARKAI_URL,
        spark_app_id=SPARKAI_APP_ID,
        spark_api_key=SPARKAI_API_KEY,
        spark_api_secret=SPARKAI_API_SECRET,
        spark_llm_domain=SPARKAI_DOMAIN,
        streaming=False,  # False=一次性返回完整回答；True=打字机流式输出
    )



def ai_ask(system_prompt,user_content):
     # 2. 构造对话消息（支持system角色设定、多轮对话）
    messages = [
        ChatMessage(role="system", content=system_prompt),
        # ChatMessage(role="user", content="解释Python里class类的作用")
        ChatMessage(role="user", content=user_content)
        ]

    # 3. 发起调用，获取AI回复
    handler = ChunkPrintHandler()
    result = spark.generate([messages], callbacks=[handler])

    # 打印完整结果
    print("\n完整回复：")
    print(result.generations[0][0].text)

if __name__ == '__main__':
    resp = ai_ask("你是助手","你好")
    print(resp)