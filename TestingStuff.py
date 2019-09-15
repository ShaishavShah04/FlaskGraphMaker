import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.ticker import MaxNLocator
#### Plot the graph

f = pd.read_csv('StockTestFile.csv',
                    names=['X_val','Y_val'],  # Add own names so that code works better
                    header=None, # So it doesnt use the values as names
                    na_values=['no info','.'] # So that values are treated like numbers not strings
                    )
x = f['X_val'].astype(float)
y = f['Y_val'].astype(float)
#
graph = plt.figure(1, figsize=(6.4,4.8))
graph = graph.add_subplot(111)
graph.scatter(x,y)
graph.xaxis.set_major_locator(MaxNLocator(integer=True)) # Only integers for the x-axis

#### Line OF Best Fit

m,b = np.polyfit(x,y,1) # the last number is the degree - I think

def line(x):
    global m,b
    y = (m*x)+b
    return y

graph.plot(x, line(x), 'r-')

### Output

plt.show()