# -*- coding: utf-8 -*-
import os
import gensim

from flask import Flask, request

# flask
# 相対パスで指定
app = Flask(__name__, static_folder='resources')
model = gensim.models.KeyedVectors.load_word2vec_format('entity_vector.model.bin', binary=True)

@app.route('/api/calc_words',methods=["POST"])
def calc_words():

    post_data = request.get_json()
    result = None
    positive_ary = []
    negative_ary = []

    for data in post_data:
        if data["sw"] == "pos":
            positive_ary.append(data["text"])
        elif data["sw"] == "neg":
            negative_ary.append(data["text"])
    
    try:
        result = model.most_similar(positive=positive_ary,negative=negative_ary)
    except KeyError as error:
        result = error
        print(error)

    return str(result)

# main
if __name__ == "__main__":
    # Flaskのマッピング情報を表示
    print(app.url_map)
    app.run(host=os.getenv("APP_ADDRESS", 'localhost'), \
    port=os.getenv("APP_PORT", 3000))