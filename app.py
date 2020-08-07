from flask import Flask,request,jsonify,abort
import flask
import requests
import xmltodict
from konlpy.tag import Komoran
import platform
import pymongo
from pymongo import MongoClient

conn=MongoClient('localhost',27017)
db=conn['auth']
url="https://stdict.korean.go.kr/api/search.do"
api_key='E6D5AAE591392D05D77F18CE05B339EA'
app = Flask(__name__)

@app.route('/favicon.ico')
def fav():
    return "test"

@app.route('/test')
def test():
    return "test"  
@app.route('/')
def index():
    return 'Sunrinton Backend'

@app.route('/register',methods=['POST'])
def regiser():
    auth=db['auth']
    json=request.json
    print(request.form)
    for i in auth.find({'id':id}):
        return jsonify(message='이미 있는 아이디 입니다',code= 403)   
    try:
        auth.insert({'birth':request.form['birth'], "name":request.form['name'],"id":  request.form['id'],"pw":request.form['pw']})
        return jsonify(message="complete",code=200)
    except expression as identifier:
        return jsonify(message="failed",code=400)

    
    
    
@app.route('/auth',methods=['POST'])
def login():
    auth=db['auth']
    data=request.data.decode('utf-8')
    
    user=request.get_json()
    json=request.json
    print(json)
    phone=json['id']
    pw=json['pw']
    a=auth.find({'id':id})
    for i in a:
        print(i)
        if i['pw']==pw:
            return jsonify(code=400,message="seccess")

    if id==None or pw==None:
        return jsonify(message="Id or Pw was Null",code=406)
    return jsonify(message="server error",code=500)

@app.route('/transport')
def transport():
    query=request.args.get('q')

    if query==None:
        print('매개변수 애러')
        return jsonify(code=400,message="Required parameters are not included")

    

    return jsonify(code=200,message="Good")

def isInDict(query='나무'):
    parameters={'key':api_key,'q':query,'pos':1}
    re=requests.get(url,parameters)
    response=xmltodict.parse(re.text)

    return response.get('channel').get('total')!='0'
print('run Server')
print(platform.system())

app.run(host='0.0.0.0',port=3000, debug=True) 

