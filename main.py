from flask import Flask,render_template,request
import requests
import json

web = Flask(__name__)

@web.route('/')
def explore():
    node = "https://mainnet.cn.utools.club"
    res = requests.get(str(node) + '/blocks')
    text = res.text
    txt = json.loads(text)
    return render_template("page.html",txt = txt,node=node)

@web.route('/node')
def explore_node():
    node = request.args.get('node')
    res = requests.get(str(node) + '/blocks')
    text = res.text
    txt = json.loads(text)
    return render_template("page.html",txt = txt,node=node)

web.run(host='0.0.0.0',port='5001')
