from flask import Flask,request,jsonify,abort
import flask
app = Flask(__name__)
@app.route('/')
def index():
    return 'Hello Flask'

app.run(host='127.0.0.1',port=80, debug=True) 