from pymilvus import connections, FieldSchema, CollectionSchema, DataType, Collection, utility, Milvus
from flask import Flask, jsonify, request
# 参考：https://github.com/milvus-io/pymilvus/blob/master/examples/example_str.py

MILVUS_HOST = '116.204.100.229'
MILVUS_PORT = '19530'
collection_name = "chatgpt_formset"
_INDEX_TYPE = 'IVF_FLAT'
_METRIC_TYPE = 'L2'

connections.connect(host=MILVUS_HOST, port=MILVUS_PORT)
collection = Collection(name=collection_name)


def _create_chatgpt_milvus_collection():
    if utility.has_collection(collection_name):
        utility.drop_collection(collection_name)

    fields = [
        FieldSchema(name='question', dtype=DataType.VARCHAR, description='问题', max_length=1024,
                    is_primary=True, auto_id=False),
        FieldSchema(name='chatgpt_embedding', dtype=DataType.FLOAT_VECTOR, description='cahtgpt embedding vectors',
                    dim=1536)
    ]
    schema = CollectionSchema(fields=fields, description='question for chatgpt search')
    collection = Collection(name=collection_name, schema=schema)

    index_params = {
        'metric_type': _METRIC_TYPE,
        'index_type': _INDEX_TYPE,
        'params': {"nlist": 1536}
    }
    collection.create_index(field_name='chatgpt_embedding', index_params=index_params)
    return collection


def insert_chatgpt(question, chatgpt_embedding):
    data = [[question], [chatgpt_embedding]]
    collection.insert(data)


def search_chatgpt(chatgpt_embedding):
    print(jsonify(chatgpt_embedding))
    search_param = {
        "data": [chatgpt_embedding],
        "anns_field": "chatgpt_embedding",
        "param": {"metric_type": _METRIC_TYPE, "params": {"nprobe": 16}},
        "limit": 10}
    results = collection.search(**search_param)
    resList = []
    for i, result in enumerate(results):
        for j, res in enumerate(result):
            resList.append(res.id)
    return resList
