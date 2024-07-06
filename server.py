# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: server.py
# Bytecode version: 3.11a7e (3495)
# Source timestamp: 1970-01-01 00:00:00 UTC (0)

from bottle import route, run, template, request, response
import base64
import socket
import pyautogui
import os
SERVER_PORT = 8080

def getname():
    return socket.gethostname()

def getipadress():
    return socket.gethostbyname(getname())

@route('/')
def index():
    return template('index', hostname=getname())

@route('/screen', method='POST')
def screenshot():
    pyautogui.screenshot('img.png')
    with open('img.png', 'rb') as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    response.content_type = 'application/json'
    return {'img_data': f'data:image/png;base64,{encoded_string}'}

@route('/off', method='POST')
def shutdown():
    time = request.json.get('time')
    os.system(f'shutdown /s /t {time}')

@route('/cmd', method='POST')
def run_command():
    text_command = request.json.get('command')
    os.system(str(text_command))
run(host=getipadress(), port=SERVER_PORT)