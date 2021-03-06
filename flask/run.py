#!flask/bin/python
from app import app
from flask import Flask, render_template, request, json, jsonify
import re
import time
import urllib2
import glob
import os
from pprint import pprint  # print json object

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summary')
def summary():
    return render_template('summary.html')

@app.route('/content')
def content():
    return render_template('content.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/404')
def empty():
    return render_template('404.html')

if __name__ == "__main__":
	app.run(debug = True)
	# app.run(host='0.0.0.0')