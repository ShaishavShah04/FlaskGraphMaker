# Shaishav Shah #
# Flask Code Application #
########################

## Imports

from flask import Flask, render_template, request, redirect, session
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.ticker import MaxNLocator

## Intializing flask

app = Flask(__name__)
app.secret_key = "NoIdea"
app.config['UPLOAD_FOLDER'] = './Uploads'
ALLOWED_EXTENSIONS = set(['csv'])

#### Subroutines ####

def allowed_file(filename):
    if filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS:
        return True
    else:
        return False

#### Main Code now ####

@app.route('/')
def home():
    return render_template("main.html")


@app.route('/', methods = ['POST','GET'])
def upload_file():
    global title, x_axis, y_axis
    if request.method == 'POST':
        f = request.files['file']
        if True == allowed_file(f.filename):
            f.save(f.filename)

    if request.method == 'POST':
        if request.method == 'POST':
            reqform = request.form
            #
            session['title'] = reqform['title']
            session['x_axis'] = reqform['x_axis']
            session['y_axis'] = reqform['y_axis']

    return render_template('uploaded.html')

@app.route('/', methods = ['POST','GET'])
def making_graph():
    title = session.get('title', None)
    x_axis = session.get('x_axis', None)
    y_axis = session.get('y_axis', None)

    print(title, x_axis, y_axis)

    return render_template('uploaded.html')


'''
@app.route('/instructions')
def instructions():
    return render_template("instruction.html")
'''


if __name__ == '__main__':
    app.run(debug = True)

