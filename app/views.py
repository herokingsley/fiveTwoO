from app import app
from flask import request
import hashlib

@app.route('/')
@app.route('/index')
def index():
    a = request.args.get('a')
    b = request.args.get('b')
    return "Hello, World!" + a + b

@app.route('/wx/api')
def wx_api():
    sign = request.args.get('signature')
    timestamp = request.args.get('timestamp')
    nonce = request.args.get('nonce')
    echostr = request.args.get('echostr')
    token = 'notoken'
    list = [token, timestamp, nonce]
    list.sort()
    localSign = sha1(list)
    if localSign == sign:
        return echostr
    else:
        return 'error'


def md5(src):
    m2 = hashlib.md5()
    m2.update(src)
    print m2.hexdigest()

def sha1(list):
    sha1 = hashlib.sha1()
    map(sha1.update, list)
    return sha1.hexdigest()