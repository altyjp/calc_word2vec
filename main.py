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
    data = model.most_similar(positive=['ディズニーランド'],negative=['面白い'])
    return data

# main
if __name__ == "__main__":
    # Flaskのマッピング情報を表示
    print app.url_map
    app.run(host=os.getenv("APP_ADDRESS", 'localhost'), \
    port=os.getenv("APP_PORT", 3000))