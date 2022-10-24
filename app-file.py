from flask import Flask
from datetime import datetime
from random import randint
import time
import os
import socket
app = Flask(__name__)
f = open('color.txt','w')
f.close()
@app.route("/")
def main():
    container = socket.gethostname()
    color = ''
    name = 'gal'
    now = datetime.now()
    current = now.strftime("%H:%M:%S")
    f = open('color.txt','r')
    color = f.read()
    f.close()
    if color == '':
        value = randint(0, 5)
        if value == 1:
            color = 'blue'
        elif value == 2:
            color = 'yellow'
        elif value == 3:
            color = 'green'
        elif value == 4:
            color = 'grey'
        elif value == 5:
            color = 'purple'
        f = open('color.txt','w')
        f.write(color)
        f.close()
    return '''
       <html>
    <head>
        <title>GalKing</title>
    </head>
    <body style="background-color:{};">
    <h2>{}, Current Time is: {} HAIDEEEEEE!!!!</h2><br>
    <p>welcome from: {}</p>
    </body>
    </html>
        '''.format(color,name,current,container)
@app.route("/gal")
def g():
    return'''<html><head><b>HAIDEEEE!!!!!</b></head></html>'''
@app.route("/read")
def file():
    container = socket.gethostname()
    fi = open('/data/file.txt','r')
    fi = fi.read()
    return '''<html><head><b>my file:<br>{}<br>Welcome from: {}!</b></head></html>'''.format(fi,container)
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080)
