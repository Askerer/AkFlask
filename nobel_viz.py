# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 22:11:49 2019

@author: asker
"""

from flask import Flask
from flask import render_template


app = Flask(__name__)

winners=[
        {'name':'Albert Einstein','category':'Physics'},
        {'name':'V.S. Naipaul','category':'Literature'},
        {'name':'Dorothy Hodgkin','category':'Chemistry'}
        ]

@app.route("/test")
def hello():
    return "Hello World!"


@app.route("/")
def demo_list():
    return render_template('testj2.html',heading="A little winners' list",winners=winners)



if __name__ == "__main__":
    app.run(port=8000,debug=True)
    