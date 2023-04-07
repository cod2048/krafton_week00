from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.project0

## HTML을 주는 부분
@app.route('/')
def home():
   return render_template('login.html')

@app.route('/sign', methods=['POST'])
def listing():
    # 1. 모든 document 찾기 & _id 값은 출력에서 제외하기
    # 2. articles라는 키 값으로 영화정보 내려주기
    return jsonify({'result':'success', 'msg':'GET 연결되었습니다!'})

## API 역할을 하는 부분
@app.route('/login', methods=['GET'])
def login():
    # 클라이언트로부터 받은 아이디 및 비밀번호 변수에 저장
    id_recieve = request.form['id_give']
    pwd_recieve = request.form['pwd_give']
    id_list = list(db.ids.find({}))
    for document in db.ids.find({'ids': {'$exists': True}}):
        if id_recieve in document['ids']:

            

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)