from flask import Flask,request,jsonify,abort
import flask
app = Flask(__name__)
@app.route('/')
def index():
    return 'Hello Flask'
if __name__=='main':
    app.run(host='0.0.0.0',port=80, debug=True) 