import openai
from flask import Flask, jsonify, request

openai.api_key = "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"
openai.organization = "org-8IOzxKfMnE2zKEGGfGbDNCol"

app = Flask(__name__)

@app.route('/chatgpt/v1/chat/completions', methods=['POST'])
def createCompletion():
    contentData = request.get_json().get('content')
    completion = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        # Change the prompt parameter to the messages parameter
        messages=[{'role': 'user', 'content': contentData}],
        temperature=0
    )
    resultMsg = completion['choices'][0]['message']['content']
    print("响应结果" + resultMsg)
    return resultMsg

@app.route('/chatgpt/v1/embeddings', methods=['POST'])
def createEmbeddings():
    contentData = request.get_json().get('content')
    completion = openai.Embedding.create(
        model='text-embedding-ada-002',
        input=contentData
    )
    resultMsg = completion['data']['embedding']
    print("响应结果" + resultMsg)
    return resultMsg


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)