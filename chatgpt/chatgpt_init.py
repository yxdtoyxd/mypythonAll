import openai
from flask import Flask, jsonify, request
from flask import Blueprint
from chatgpt import chatgpt_base_biz

chatgpt_init_app = Blueprint('chatgpt_init_app', __name__)


@chatgpt_init_app.route('/chatgpt/v1/chat/completions', methods=['POST'])
def create_completion():
    return chatgpt_base_biz.createCompletion(request.get_json().get('content'))


@chatgpt_init_app.route('/chatgpt/v1/embeddings', methods=['POST'])
def create_embeddings():
    return chatgpt_base_biz.createEmbeddings(request.get_json().get('content'))
