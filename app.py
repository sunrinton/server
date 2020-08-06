from flask import Flask,request,jsonify,abort
import flask
app = Flask(__name__)
@app.route('/favicon.ico')
def fav():
    return "test"
    
@app.route('/')
def index():
    return 'Hello Flask'
if __name__=='main':
    print('run Server')
    app.run(host='127.0.0.1',port=3000, debug=True) 