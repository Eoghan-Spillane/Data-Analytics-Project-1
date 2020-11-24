# Author: Eoghan Spillane
# Student ID: R00175214
# Student Course Name: SDH3B

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def import_data():
    data = pd.read_csv('us-Hotel.csv')
    return data


def task1():
    data = import_data()
    data_average_price = np.average(data.price)
    group1 = []
    group2 = []

    group1 = data[data['price'] <= data_average_price]  # Where the price is below average
    group2 = data[data['price'] > data_average_price]  # Where the price is above average

    group1_average_price = np.average(group1.price)
    group2_average_price = np.average(group2.price)

    groupA = group1[group1['price'] <= group1_average_price]
    groupB = group1[group1['price'] > group1_average_price]
    groupC = group2[group2['price'] <= group2_average_price]
    groupD = group2[group2['price'] > group2_average_price]

    print(len(data))
    print(group1_average_price)
    print(data_average_price)
    print(group2_average_price)
    print(len(group1), len(group2))

    chart = np.array([len(groupA), len(groupB), len(groupC), len(groupD)])
    labels = ["A- Under €105", "B- Under €219", "C- Under €599", "D- Over €599"]
    explode = [0, 0, 0, 0.2]

    fig = plt.figure()
    plt.pie(chart, explode=explode, autopct='%.2f')
    plt.legend(labels, loc="upper left", title="% of hotels charging:")
    plt.title("Hotel Cost Per Night (Sample Size = 226,030)")
    plt.show()

    #

task1()
