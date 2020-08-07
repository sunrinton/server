from flask import Flask,request,jsonify,abort
import flask
import requests
import xmltodict
from konlpy.tag import Komoran
url="https://stdict.korean.go.kr/api/search.do"
api_key='E6D5AAE591392D05D77F18CE05B339EA'
app = Flask(__name__)

@app.route('/favicon.ico')
def fav():
    return "test"
    
@app.route('/')
def index():
    return 'Sunrinton Backend'

@app.route('/transport')
def transport():
    query=request.args.get('q')
    kkma=Komoran()
    if query==None:
        print('매개변수 애러')
        return jsonify(code=400,message="Required parameters are not included")
    print(kkma.nouns(query))
    print(isInDict(query))

    return jsonify(code=200,message="Good")

def isInDict(query='나무'):
    parameters={'key':api_key,'q':query,'pos':1}
    re=requests.get(url,parameters)
    response=xmltodict.parse(re.text)

    return response.get('channel').get('total')!='0'
print('run Server')
app.run(host='0.0.0.0',port=3000, debug=True) 