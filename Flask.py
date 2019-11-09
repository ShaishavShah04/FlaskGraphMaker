# FLASK CODE

import os
from flask import Flask, render_template, redirect, request, url_for, flash
#
app = Flask(__name__)
app.secret_key = "NoIdea"
app.config['UPLOAD_FOLDER'] = './Uploads'
ALLOWED_EXTENSIONS = set(['csv'])

#
def allowed_file(filename):
    if filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS:
        return True
    else:
        return False
#

@app.route('/')
def home():
    return render_template("main.html")

@app.route('/', methods = ['POST','GET'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if True == allowed_file(file.filename):
            file.save(file.filename)
            print(file)
    if request.method == 'POST':
        if request.method == 'POST':
            result = request.form
            print(result)

    return render_template('uploaded.html')





'''
@app.route('/instructions')
def instructions():
    return render_template("instruction.html")
''' # I dont wanna do this right now, will add later


if __name__ == '__main__':
    app.run(debug = True)

