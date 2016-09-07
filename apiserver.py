#!/usr/bin/python

#Written by Goose 5/30/2016
import os
import sys
import sqlite3
import requests
import uuid
import time
import logging
import gfortune
import Icmd
#from wsgilog import log

from flask import Flask, jsonify, abort, request, make_response, url_for, g, Response, json, redirect, render_template
from flask.ext.httpauth import HTTPBasicAuth

#GLOBALS

randID = uuid.uuid4()
app = Flask(__name__, static_url_path = "")
auth = HTTPBasicAuth()

#Functions


@auth.get_password
def get_password(username):
    if username == 'paas':
        return 'G00531t'
    return None

@auth.error_handler
def unauthorized():
    return make_response(jsonify( { 'error': 'Unauthorized access' } ), 403)
    # return 403 instead of 401 to prevent browsers from displaying the default auth dialog

@app.errorhandler(400)

def not_found(error):
    return make_response(jsonify( { 'error': 'Bad request' } ), 400)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'Not found' } ), 404)




@app.route('/form', methods = [ 'GET','POST'])
def form():

    cresp = Icmd.scmd(command)
    return render_template('form.html')
    #return "Text Message recieved: " + request.data

@app.route('/formaction', methods = [ 'GET','POST'])
def form_action():

    return render_template('formaction.html')
    #return "Text Message recieved: " + request.data


@app.route('/response', methods=['GET','POST'])
def gresponse():
    command = request.form['command']

    cresp = Icmd.scmd(command)
    return gresp
    #return render_template('formaction.html')

@app.route('/test', methods = [ 'GET','POST'])
def api_test():
    testMsg = "honk honk world"
    return testMsg


@app.route('/incoming', methods = [ 'POST'])
def incoming():

    command = request.get_data()
    cresp = Icmd.scmd(command) #+ "\n"
    #time.sleep(2)
    return cresp

# test with curl
#curl -X post -d "who am i" http://127.0.0.1:5000/incoming

@app.route('/fortune', methods = [ 'GET'])
def fortune():

    fortune = gfortune.fortune()
    time.sleep(2)
    return fortune +  "\n"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int("5000"), debug = True)
    #app.run( debug = True )
