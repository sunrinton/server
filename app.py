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
    app.run(host='0.0.0.0',port=80, debug=True) 