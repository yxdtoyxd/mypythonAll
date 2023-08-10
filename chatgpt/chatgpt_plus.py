import openai
from flask import Flask, jsonify, request
from flask import Blueprint
from milvus import milvus_chatgpt
from chatgpt import chatgpt_base_biz

chatgpt_plus_app = Blueprint('chatgpt_plus_app', __name__)

@chatgpt_plus_app.route('/chatgpt/v1/embeddings/milvus', methods=['POST'])
def createEmbeddingsToMilvus():
    contentData = request.get_json().get('content')
    completion = openai.Embedding.create(
        model='text-embedding-ada-002',
        input=contentData
    )
    resultMsg = completion.data[0].embedding
    milvus_chatgpt.insert_chatgpt(contentData, resultMsg)
    return resultMsg


@chatgpt_plus_app.route('/chatgpt/v1/embeddings/search', methods=['POST'])
def match_content_by_embeddings():
    contentData = request.get_json().get('content')
    embeddings = chatgpt_base_biz.createEmbeddings(contentData)
    return jsonify(milvus_chatgpt.search_chatgpt(embeddings))
