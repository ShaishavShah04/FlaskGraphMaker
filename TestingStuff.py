import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.ticker import MaxNLocator
### Functions for error bars
def intro():
    print('''
    Hello!
    This is a graph maker using python code!
    If you wish to have varying error bars for each point, add that data in the format: POINT_X , POINT_Y , ERROR_X , ERROR_Y. 
    Otherwise, the csv file shall be in the format POINT_X, POINT_Y.
    Thank You.
    ''')
def checkcsverror():
    pass

#####################################################
intro()
#### Inputs
title = input('Title of graph: ')
x_axis = input('X axis label with measurement if any: ')
y_axis = input("Y axis of graph with measurement if any: ")
eznum = input('Axises have only integers? Y or N: ')
lreg = input("Graph linear regression line (1)? OR connect data points with line (2) ? OR scatter plot only (3): ")
wanterror = input('Do you wish to add error bars? Y or N: ')

if wanterror in ['Y','y']:
    errortype = input('Only procced if you have static error bars. To add varying error bars, add error bar data in the csv file. Continue? Y or N ')
    if errortype in ['Y','y']:
        y_err = float(input("Static error bar for y_axis? 0 if none: "))
        x_err = float(input("Static error bar for x_axis? 0 if none: "))

#### Sort the Data

f = pd.read_csv('StockTestFile.csv',
                    names=['X_val','Y_val','X_err','Y_err'],  # Add own names so values can become callable later
                    header=None, # So it doesnt use the values as names
                    # na_values=['no info','.'] # So that values are treated like numbers not strings
                    )
x = f['X_val'].astype(float)
y = f['Y_val'].astype(float)

# The error bars for non-static errors
x_error = f['X_err'].astype(float)
y_error = f['Y_err'].astype(float)
#
graph = plt.figure(1, figsize=(6.4,4.8)) # size ( in inches)
graph = graph.add_subplot(111)

if lreg in ['1','3']:
    graph.plot(x,y,'o', color = 'blue')
else:
    graph.plot(x,y,'-ok', color = 'blue')

if eznum in ['Y','y']:
    graph.xaxis.set_major_locator(MaxNLocator(integer=True)) # Only integers for the x-axis
    graph.yaxis.set_major_locator(MaxNLocator(integer=True))

## Line of Best Fit

if lreg in ['1']:
    m,b = np.polyfit(x,y,1) # the last number is the degree - I think

    def line(x):
        global m,b
        y = (m*x)+b
        return y

    graph.plot(x, line(x), color='red')

## Error bars

if wanterror in ['Y','y']:
    # Static error
    if errortype in ['Y','y']:
        plt.errorbar(x,y,yerr = y_err, xerr= x_err)
    # Non-static error bars
    if wanterror in ['Y','y'] and errortype not in ['Y','y']:
        plt.errorbar(x, y, yerr=y_error, xerr=x_error)

#### Output
plt.title(title)
plt.xlabel(x_axis)
plt.ylabel(y_axis)
# The real output
plt.show()