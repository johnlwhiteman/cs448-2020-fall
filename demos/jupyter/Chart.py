import copy
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def plot1(samples):
    cnt = len(samples)
    samples = [int(sample) for sample in samples] # Prepadded zeros will be squashed
    df = pd.DataFrame(data=samples, index=np.arange(0, cnt), columns=['Random'])
    ax = df.plot(figsize=(15, 5), lw=1.5, colormap='jet',
                 marker='.', markersize=10,
                 title="Sample vs. Result: Samples={1}, Seed={0:,}".format(samples[0], cnt),
                                                                  legend=False);
    ax.set_xlabel('Sample')
    ax.set_ylabel('Result')
    ax.locator_params(axis="both", integer=True, tight=False)
    ax.ticklabel_format(style='plain')
    ax.yaxis.set_major_formatter(mpl.ticker.StrMethodFormatter('{x:,.0f}'))
    return

def plot2(samples):
    cnt = len(samples)
    samples = [int(sample) for sample in samples] # Prepadded zeros will be squashed
    x = copy.deepcopy(samples)
    x.pop(0)
    samples.pop()
    df = pd.DataFrame(data=samples, index=x, columns=['Random'])
    ax = df.plot(figsize=(15, 5), lw=1.5, colormap='jet',
                 marker='.', markersize=10,
                 title="Seed vs. Result Plot: Samples={1}, Seed={0:,}".format(samples[0], cnt),
                                                                  legend=False);
    ax.set_xlabel('Seed')
    ax.set_ylabel('Result')
    ax.locator_params(axis="both", integer=True, tight=False)
    ax.ticklabel_format(style='plain')
    ax.xaxis.set_major_formatter(mpl.ticker.StrMethodFormatter('{x:,.0f}'))
    ax.yaxis.set_major_formatter(mpl.ticker.StrMethodFormatter('{x:,.0f}'))
    return

def plot3(samples):
    cnt = len(samples)
    samples = [int(sample) for sample in samples] # Prepadded zeros will be squashed
    x = copy.deepcopy(samples)
    y = copy.deepcopy(samples)
    x.pop()
    y.pop(0)
    data = [[x[i], y[i]] for i in range(0, len(x))]
    dataFrame = pd.DataFrame(data=data, columns=['Seed','Random Number']);
    ax = dataFrame.plot.scatter(figsize=(15, 5), x='Seed', y='Random Number', title= "Scattered Random Seeds Plot");
    ax.xaxis.set_major_formatter(mpl.ticker.StrMethodFormatter('{x:,.0f}'))
    ax.yaxis.set_major_formatter(mpl.ticker.StrMethodFormatter('{x:,.0f}'))

def plotLineX(x, y, title, xLabel, yLabel):
    with plt.xkcd():
        plt.plot(x, y)
        plt.title(title)
        plt.xlabel(xLabel)
        plt.ylabel(yLabel)
        plt.show()
