from flask import Flask,request,jsonify,abort
import flask
app = Flask(__name__,static_url_path='/static')
@app.route('/')
def index():
    print(flask.__version__)
    return 'Hello Flask'

app.run(host='127.0.0.1',port=8888, debug=True) 