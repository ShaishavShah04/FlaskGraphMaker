import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import csv

apl_price = [93,112,104,144,169]
ms_price = [39 ,50,57, 69, 94.39]
year = [2014, 2015, 2016, 2017, 2018]
plt.plot(year, apl_price,'k'
        ,year,ms_price)

plt.title('Stock Prices')
plt.xlabel('Years')
plt.ylabel('Stock Price')

# Optional creating own limits
# plt.axis([2013,2019, 20,180])
plt.show()

#
#
#
fig_1 = plt.figure(1, figsize=(6.4,4.8))
chart_1 = fig_1.add_subplot(121)
# First Number Represents the Number of rows, Second number is the number of columns. Basically creating a grid for the charts to show in
chart_2 = fig_1.add_subplot(122)

chart_1.plot(year, apl_price)
chart_1.xaxis.set_major_locator(MaxNLocator(integer=True)) # makes the xaxis only integers
chart_2.scatter(year, ms_price)

plt.show()