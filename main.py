"""extract feature and search with user query."""
from dotenv import load_dotenv
load_dotenv()
import openai
import os
from dwchatbot.rag import CacheRetriever
from dwchatbot.config import Config
deepapi_key = os.getenv("deepapi_key")
moonapi_key = os.getenv("moonapi_key")
openapi_key = os.getenv("openapi_key")
zhipuai_key = os.getenv("zhipuai_key")

def chat(prompt,model):
    if model=='zhipuai':
        try:
            from zhipuai import ZhipuAI
            client = ZhipuAI(api_key=zhipuai_key)
        except Exception as e:
            print(str(e))
            print('please `pip install zhipuai` and check API_KEY')
            return ''
        completion = client.chat.completions.create(
            model='glm-4',
            messages=[
                {"role": "user", "content": prompt},
            ],
            temperature=0.1,
        )
        return completion.choices[0].message.content

    if model=='deepseek-chat':
       client = openai.OpenAI(api_key=deepapi_key, base_url="https://api.deepseek.com/v1")
    elif model=='moonshot-v1-8k':
       client = openai.OpenAI(api_key=moonapi_key, base_url="https://api.moonshot.cn/v1")
    else:
       client = openai.OpenAI(api_key=openapi_key,)

    response = client.chat.completions.create(
        model=model,
        messages=[
            {'role': 'system', 'content': "你现在是一个检索助手，会根据我给你的材料进行问题回答并给出相应出处、内容及出处的 URL。请仔细阅读参考材料回答问题，如果材料和问题无关，尝试用你自己的理解来回答问题。如果无法确定答案，直接回答不知道。"},
            {"role": "user", "content": prompt},
        ]
    )
    return response.choices[0].message.content

cache = CacheRetriever()
retriever = cache.get(work_dir=Config.work_dir)

system_prompt = '问题：“{}” \n 材料：“{}”\n  '  # noqa E501


if __name__ == "__main__":
    question = '推荐几个学习大数据的课程'
    chunk, db_context, references = retriever.query(question)
    input_prompt = system_prompt.format(question,db_context)
    result = chat(input_prompt,"zhipuai")
    print(result)