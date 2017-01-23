#!/usr/bin/env python
from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

def get_port():
    port = os.getenv("PORT")
    
    if type(port) == str:
        return port
    
    return 8080

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=get_port())

