# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from flask import Flask

app = Flask(__name__)
@app.route("/")

def example():
    return "Let's learn Docker!"#add our message

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = int("5000"), debug = True)
    


