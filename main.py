from flask import Flask,render_template,request
import requests
import json

web = Flask(__name__)

@web.route('/')
def explore():
    res = requests.get('https://mainnet.cn.utools.club/blocks')
    text = res.text
    txt = json.loads(text)
    return render_template("page.html",txt = txt)

@web.route('/data')
def explore_data():
    try:
        block_num = request.args.get("id")
    except:
        block_num = request.args.get("11")
    res = requests.get('https://mainnet.cn.utools.club/blocks')
    text = res.text
    txt = json.loads(text)
    return render_template("data.html",data = txt)

web.run(host='0.0.0.0',port='5001')
