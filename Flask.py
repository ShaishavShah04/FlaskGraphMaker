import os
from flask import Flask, render_template, redirect, request, url_for, flash
#
ALLOWED_EXTENSIONS = set(['csv'])
STORAGE = 'C:/Users/shais/PycharmProjects/Volunteer_Work/Uploads'
#
app = Flask(__name__)
app.secret_key = "NoIdea"
#
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
#
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS
##


@app.route('/')
def home():
    return render_template("main.html")

@app.route('/', methods = ['POST','GET'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            file.save(os.path.join('C:/Users/shais/PycharmProjects/Volunteer_Work/Uploads', file))
            flash('File Uploaded. Now wait!')
            return redirect('/')


@app.route('/instructions')
def instructions():
    return render_template("instruction.html")



if __name__ == '__main__':
    app.run(debug = True)

