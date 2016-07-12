import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import urllib2



def graph(stock):
    url = 'http://ichart.finance.yahoo.com/table.csv?s='+stock+'&d=9&e=14&f=2015&g=d&a=8&b=7&c=2009&ignore=.csv'
    date, open, high, low, close, volume, adj_close = np.loadtxt(urllib2.urlopen(url), skiprows=1, delimiter=',', unpack=True, converters={0: mdates.strpdate2num('%Y-%m-%d')})

    fig = plt.figure()
    ax1 = fig.add_subplot(1,1,1, axisbg='w')
    plt.plot_date(x=date, y=high, fmt='-')
    plt.plot_date(x=date, y=low, fmt='-')
    plt.plot_date(x=date, y=adj_close, fmt='-')

    plt.title(stock + ', 2009 to 2015')
    plt.ylabel('Adjusted close')
    plt.xlabel('Date')
    plt.show()

graph('TSLA')