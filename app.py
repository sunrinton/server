from flask import Flask,request,jsonify,abort
import flask
import requests
import xmltodict
import platform
import pymongo
from pymongo import MongoClient
import base64
import random

conn=MongoClient('localhost',27017)
db=conn['sunrinton']


app = Flask(__name__)




@app.route('/')
def index():
    return 'Sunrinton Backend'

@app.route('/register',methods=['POST'])
def regiser():
    auth=db['auth']
    
    user_id=request.args.get('id')
    pw=request.args.get('pw')
    birth=request.args.get('birth')
    name=request.args.get('name')
    
    if user_id==None or pw==None or birth==None or name==None:
        return jsonify(message='매개변수가 비어있습니다',code=400)
   
    for i in auth.find({'id':user_id}):
        return jsonify(message='이미 있는 아이디 입니다',code= 403)   

    if birth.isdigit()==False:
        return jsonify(message="birth is must type int",code=400)

    auth.insert({'birth':birth, "name":name,"id": user_id,"pw":base64.b64encode(pw.encode('euc-kr'))})
    return jsonify(message="complete",code=200)

@app.route('/search')
def search():
    data=db['data']
    re=request.args.get('text')
    if re==None:
        return '매개변수를 채워주세요'
    print(re)
    find=data.find_one({'word':re})
    if find==None:
        return jsonify(code=400,data={"message":"일치하는 단어가 없습니다"})
    return jsonify(code=200,data={'word':find.get('word'),'mean':find.get('mean'),'sentence':find.get('sentence'),})


@app.route('/getOne')
def getInfo():
    data=db['data']
    ran=data.find_one({'index':int(random.uniform(1,data.count()))})

    for i in ran:
        print(i)
    print(ran)
    return jsonify(word=ran.get('word'),mean=ran.get('mean'),sentence=ran.get('sentence'))
@app.route('/quiz')
def quiz():
    data=db['data']
    used=[0]
    response=[]

    for i in range(10):
        ra=0
        while(ra in used):
            ra=int(random.uniform(1,data.count()))    
        print(ra)

        ran=data.find_one({'index':ra})
        print(data.count())
        response.append({'word':ran.get('word'),'mean':ran.get('mean'),'sentence':ran.get('sentence')})
        used.append(ra)
    print(data.count())
    return jsonify(data=response)

    
    
@app.route('/auth',methods=['POST'])
def login():
    auth=db['auth']
    data=request.data.decode('utf-8')
    
    
    user_id=request.args.get('id')
    pw=request.args.get('pw')
    a=auth.find({'id':user_id})
    for i in a:
        print(i)
        if i['pw']==base64.b64encode(pw.encode('euc-kr')):
            
            jsons={'name':i['name'],'birth':i['birth']}
            return jsonify(code=200,message="seccess",data=jsons)
        else:
            return jsonify(code=403,message='login fail')

    if user_id==None or pw==None:
        return jsonify(message="Id or Pw was Null",code=403)
    return jsonify(message="don't this id ow pw",code=403)


if __name__=='__main__':
    app.run(host='0.0.0.0',port=3000, debug=True) 

