from flask import Flask,request,jsonify,abort
import flask
app = Flask(__name__)
@app.route('/favicon.ico')
def index():
    return "test"
    
@app.route('/')
def index():
    return 'Hello Flask'
if __name__=='main':
    app.run(host='0.0.0.0',port=3000, debug=True) 