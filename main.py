# -*- coding: utf-8 -*-
import os
import gensim

from flask import Flask

# flask
# 相対パスで指定
app = Flask(__name__, static_folder='resources')
model = gensim.models.KeyedVectors.load_word2vec_format('entity_vector.model.bin', binary=True)

@app.route('/api/calc_words',methods=["POST"])
def calc_words():
    #[{sw: "pos", text: "TEST"},{sw: "pos", text: "TEST"},{sw: "pos", text: "TEST"}....]
    #result = model.most_similar(positive=positive_ary,negative=negative_ary)

    post_data = [{'sw': "pos", 'text': "TEST"},
            {'sw': "pos", 'text': "TEST"},
            {'sw': "pos", 'text': "TEST"}]

    positive_ary = []
    negative_ary = []

    for data in post_data:
        if data["sw"] == "pos":
            positive_ary.append(data["text"])
        elif data["sw"] == "neg":
            negative_ary.append(data["text"])
    
    result = model.most_similar(positive=positive_ary,negative=negative_ary)

    return result

# main
if __name__ == "__main__":
    # Flaskのマッピング情報を表示
    print(app.url_map)
    app.run(host=os.getenv("APP_ADDRESS", 'localhost'), \
    port=os.getenv("APP_PORT", 3000))