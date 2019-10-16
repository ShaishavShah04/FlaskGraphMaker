import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.ticker import MaxNLocator
### Functions for error bars
def errorx():
    pass

#### Inputs
title = input('Title of graph: ')
x_axis = input('X axis label with measurement if any: ')
y_axis = input("Y axis of graph with measurement if any: ")
eznum = input('Axises have only integers? Y or N: ')
lreg = input("Graph line of best fit (linear only)? Y or N: ")
wanterror = input('Do you wish to add error bars? Y or N')

if wanterror in ['Y','y']:
    errortype = input('Only procced if you have static error bars. If you have varying error per point on the graph, please add error to the csv file. Continue? Y or N ')
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
graph.scatter(x,y)

if eznum in ['Y','y']:
    graph.xaxis.set_major_locator(MaxNLocator(integer=True)) # Only integers for the x-axis
    graph.yaxis.set_major_locator(MaxNLocator(integer=True))

## Line of Best Fit

if lreg in ['Y','y']:
    m,b = np.polyfit(x,y,1) # the last number is the degree - I think

    def line(x):
        global m,b
        y = (m*x)+b
        return y

    graph.plot(x, line(x), color='green')

## Error bars

# Static error bars
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