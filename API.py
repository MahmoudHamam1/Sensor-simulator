import json
import os , sys
from flask import Flask,jsonify,request,render_template
import time
import random
import pandas as pd
import requests
from threading import Timer

app = Flask(__name__)
data="no data"
def update_data(interval):
    Timer(interval, update_data, [interval]).start()
    global data
    

update_data(1)

@app.route("/stream",methods=["get"])
def get_res():
    data=request.args.get('data')
    print(data)
    return data;
#################################### For solving cross ##########################
@app.after_request
def add_headers(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    return response

###################################  Runnting the server #################################################
if __name__ == '__main__':
    app.run(host="127.0.0.1",port=9090)
