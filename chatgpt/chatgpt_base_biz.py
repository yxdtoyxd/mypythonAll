import openai

openai.api_key = "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"
openai.organization = "org-8IOzxKfMnE2zKEGGfGbDNCol"


def createCompletion(contentData):
    completion = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        # Change the prompt parameter to the messages parameter
        messages=[{'role': 'user', 'content': contentData}],
        temperature=0
    )
    resultMsg = completion['choices'][0]['message']['content']
    print("响应结果" + resultMsg)
    return resultMsg


def createEmbeddings(contentData):
    completion = openai.Embedding.create(
        model='text-embedding-ada-002',
        input=contentData
    )
    return completion.data[0].embedding