from flask import Flask,request,jsonify,abort


@app.route('/')
def index():
    return 'Hello Flask'

app = Flask(__name__,static_url_path='/static')