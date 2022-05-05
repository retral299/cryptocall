from bs4 import BeautifulSoup
import requests
import datetime
import time
import pyfiglet
import os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib.animation import FuncAnimation
from sklearn import linear_model
import csv


R = '\033[31m'
G = '\033[32m'
C = '\033[36m'
W = '\033[0m'

buyborder = 300000

sellborder = 300000

sec = 60

def animate_reg(i):

    data = pd.read_csv('data.csv')

    date = data["Date"]
    bit = data["price"]

    plt.cla()
    plt.style.use('bmh')
    plt.xticks(rotation=90)

    x_values = np.asanyarray(date)
    y_values = np.asanyarray(bit)

    reg = linear_model.LinearRegression()

    x_values = x_values.reshape(-1, 1)
    y_values = y_values.reshape(-1, 1)

    reg.fit(x_values, y_values)

    y_values_ = reg.predict(x_values)

    for i in range(len(y_values)):

        if y_values[i] < y_values_[i]:

            diff = int(abs(y_values[i] - y_values_[i]))

            aton = int(abs(y_values[i] - y_values_[i]))

            if diff >= buyborder:

                print(R+'buy now'+C+f' diff : {aton}')

        elif y_values[i] > y_values_[i]:

            diff = int(y_values[i] - y_values_[i])

            aton = int(y_values[i] - y_values_[i])

            if diff >= buyborder:

                print(G+'sell now'+C+f' diff : {aton}')

        else:

            diff = y_values[i] - y_values_[i]

            aton = int(abs(y_values[i] - y_values_[i]))

            print(G+'cold zone!'+C+f' diff : {aton}')



    plt.plot(x_values, y_values, color='red')
    plt.plot(x_values, y_values_, color='blue')
   
    plt.show()


if __name__ == '__main__':

    ani = FuncAnimation(plt.gcf(), animate_reg, interval=f'{sec}000')
    plt.tight_layout()
    # plt.style.use('bmh')
    plt.show()
