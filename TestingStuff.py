import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.ticker import MaxNLocator

#### Inputs
title = input('Title of graph: ')
x_axis = input('X axis label with measurement if any: ')
y_axis = input("Y axis of graph with measurement if any: ")
eznum = input('Axises have only integers? Y or N: ')
lreg = input("Graph line of best fit (linear only)? Y or N: ")
y_err = float(input("Static error bar for y_axis? 0 if none: "))
x_err = float(input("Static error bar for x_axis? 0 if none: "))
#### Sort the Data

f = pd.read_csv('StockTestFile.csv',
                    names=['X_val','Y_val'],  # Add own names so values can become callable later
                    header=None, # So it doesnt use the values as names
                    # na_values=['no info','.'] # So that values are treated like numbers not strings
                    )
x = f['X_val'].astype(float)
y = f['Y_val'].astype(float)
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

    graph.plot(x, line(x), 'r-')

## Error bars
if not y_err == 0 or not x_err == 0:
    plt.errorbar(x,y,yerr = y_err, xerr= x_err)
#### Output

plt.title(title)
plt.xlabel(x_axis)
plt.ylabel(y_axis)
# The real output
plt.show()