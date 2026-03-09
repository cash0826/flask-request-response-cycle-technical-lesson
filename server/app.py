#!/usr/bin/env python3

import os
from flask import Flask, request, current_app, g, make_response

app = Flask("Melanie's application") # __name__ sets the name to the name of the file. 

@app.before_request # helpful for logic to check if a user is logged in, if they have correct credentials, correct permissions, etc.. before giving data/response
def app_path():
    g.path = os.path.abspath(os.getcwd()) # absolute path / get current working directory
    # object is in-scope
    # g object will last 1 request.  When user makes a new HTTP request, this value won't be set unless it hits this before request and sets it. 
    # HTTP requests

@app.route('/')
def index():
    host = request.headers.get('Host')
    appname = current_app.name
    response_body =  f'''
    <h1>The host for this page is {host}</h1>
    <h2>The name of this application is {appname}</h2> 
    <h3>The path of this application on the user's deveice is {g.path} </h3>
    <h4>Updated! </h4>
    ''' 
    status_code = 200 # allows you to return HTTP status code
    headers = {}
    return make_response(response_body, status_code, headers) # allows you to send string, status code, and header's dictionary

if __name__ == '__main__':
    app.run(port=5555, debug=True)
