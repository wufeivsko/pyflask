#!/usr/bin/python3
#coding:utf-8
from flask import Flask,request,render_template

app = Flask(__name__)

@app.route('/')
def first():
	return "welcome to python"

if __name__=='__main__':
    app.run(host='0.0.0.0',port=9999,debug=True)

