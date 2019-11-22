# Shaishav Shah #
# Flask Code Application #
########################

## Imports
import os
from flask import Flask, render_template, request, redirect, session, url_for
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
def line(x,m,b):
    global all
    y = (m * x) + b
    return y

def allowed_file(filename):
    if filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS:
        return True
    else:
        return False

#######################
#### Main Code now ####
#######################

## Inputs ( with uploaded file processing )

@app.route('/')
def home():
    return render_template("main.html")


@app.route('/', methods = ['POST','GET'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        session['name'] = f.filename
        f.save(os.path.join("C:/Users/shais/PycharmProjects/Volunteer_Work/Uploads", f.filename))

    if request.method == 'POST':
        reqform = request.form
        #
        session['title'] = reqform['title']
        session['x_axis'] = reqform['x_axis']
        session['y_axis'] = reqform['y_axis']
        session['Eznum'] = reqform['Eznum']
        session['lreg'] = reqform['lreg']
        #
    return redirect(url_for('make'))

## Processing

@app.route('/make1', methods = ['POST','GET'])
def make():
    # Organizing Info

    title = session.get('title', None)
    x_axis = session.get('x_axis', None)
    y_axis = session.get('y_axis', None)
    ez_num = session.get('Eznum', None)
    lreg = session.get('lreg', None)
    namefile = session.get('name', None)
    f = pd.read_csv(namefile,
                    names=['X_val', 'Y_val', 'X_err', 'Y_err'],  # Add own names so values can become callable later
                    header=None,  # So it doesnt use the values as names
                    # na_values=['no info','.'] # So that values are treated like numbers not strings
                    )
    x = f['X_val'].astype(float)
    y = f['Y_val'].astype(float)
    # The error bars for non-static errors
    x_error1 = f['X_err'].astype(float)
    y_error1 = f['Y_err'].astype(float)
    x_error = x_error1.fillna(0)  # Helpful to work around NaN values
    y_error = y_error1.fillna(0)

    ##

    graph = plt.figure(1, figsize=(6.4, 4.8))  # size ( in inches)
    graph = graph.add_subplot(111)

    if lreg in ['1', '3']:
        graph.plot(x, y, 'o', color='blue')
    else:
        graph.plot(x, y, '-ok', color='blue')

    if ez_num in ['Y', 'y']:
        graph.xaxis.set_major_locator(MaxNLocator(integer=True))  # Only integers for the x-axis
        graph.yaxis.set_major_locator(MaxNLocator(integer=True))

    ## Line of Best Fit

    if lreg in ['1']:
        m, b = np.polyfit(x, y, 1)  # the last number is the degree - I think

        graph.plot(x, line(x,m,b), color='red')

    ## Error Bars even tho dont work

    if x_error[0] != 0 and y_error[0] != 0:
        plt.errorbar(x, y, yerr=y_error, xerr=x_error, fmt='o')

    ## Output

    plt.title(title)
    plt.xlabel(x_axis)
    plt.ylabel(y_axis)
    plt.show()
    ##

    return 'Ok'




if __name__ == '__main__':
    app.run(debug = True)

