__author__ = 'Steve'
import matplotlib.pyplot as plt
import pandas as pd

def Hist_plot():
    item = Hist_plot()
    df = pd.read_csv('100.csv')
    df[item].value_counts()
    df[item].hist(bins=30)
    plt.title('--- Distribution ---')
    plt.xlabel('Age')
    plt.ylabel('Density')



if __name__=='__main__':
    Hist_plot()