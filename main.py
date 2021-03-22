# coding=utf-8
from flask import  Flask, request
from LAC import LAC
from gevent.pywsgi import WSGIServer

# init flask
app = Flask(__name__)


# 装载分词模型
LAC_SEG = LAC(mode='seg')
LAC_LAC = LAC(mode='lac')
LAC_RANK = LAC(mode="rank")

PASSWORD = 'zzerd.com'
UNA_UTHORIZED_CODE = 401
UNA_UTHORIZED_MSG = "认证失败"
BAD_REQUEST_CODE = 400
BAD_REQUEST_MSG = "参数错误"
NOT_FOUND_CODE = 404
NOT_FOUND_MSG = "请求的资源不存在，或者没有这个请求方法"


# 单个样本输入，输入为Unicode编码的字符串
# seg 普通分词
@app.route('/seg', methods=['POST'])
def lac_seg():
    return create_respose(request,LAC_SEG)

@app.route('/lac',methods=['POST'])
def lac_lac():
    return create_respose(request,LAC_LAC)

@app.route('/rank',methods=['POST'])
def lac_rank():
    return create_respose(request,LAC_RANK)

# error page relink
@app.errorhandler(400)
def errorhandler(error):
    return create_error_respose(BAD_REQUEST_CODE,BAD_REQUEST_MSG)
@app.errorhandler(404)
def request_not_found(error):
    return create_error_respose(NOT_FOUND_CODE,NOT_FOUND_MSG)

def lac_common(lac, text):
    if not text:
        return {"data": []}
    seg_result = lac.run(text)
    return {"data": seg_result}

def create_respose(request,lac_mod):
        text = request.form['text']
        password = request.form['password']
        # auth error
        if password != PASSWORD:
            return create_error_respose(UNA_UTHORIZED_CODE,UNA_UTHORIZED_MSG)
        if text and password:
            return lac_common(lac_mod, text)
        # bad request
        else:
            return create_error_respose(BAD_REQUEST_CODE,BAD_REQUEST_MSG)

def create_error_respose(error_code, error_msg):
    return {
        "error_code": error_code,
        "error_msg": error_msg,
        "data": [],
    },error_code


if __name__ == "__main__":
    app.config['JSON_AS_ASCII'] = False
    app.config["DEBUG"] = False
    #app.run(host='127.0.0.1', port='3001')
    http_server = WSGIServer(('',3001),app)
    http_server.serve_forever()
