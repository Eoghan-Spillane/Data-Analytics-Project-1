# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 17:45:12 2020
@Student name: Eoghan Spillane
@Student ID: R00175214
@Student Course Name: SDH3-B
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def import_data():
    data = pd.read_csv('us-Hotel.csv', encoding="ISO-8859-1")
    return data


def task1():
    data = import_data()
    data_average_price = np.average(data.price)

    group1 = data[data['price'] <= data_average_price]  # Where the price is below average
    group2 = data[data['price'] > data_average_price]  # Where the price is above average

    group1_average_price = np.average(group1.price)
    group2_average_price = np.average(group2.price)

    groupA = group1[group1['price'] <= group1_average_price]
    groupB = group1[group1['price'] > group1_average_price]
    groupC = group2[group2['price'] <= group2_average_price]
    groupD = group2[group2['price'] > group2_average_price]

    # print(len(data))
    # print(group1_average_price)
    # print(data_average_price)
    # print(group2_average_price)
    # print(len(group1), len(group2))

    chart = np.array([len(groupA), len(groupB), len(groupC), len(groupD)])
    labels = ["A- Under €105", "B- Under €219", "C- Under €599", "D- Over €599"]
    explode = [0, 0, 0, 0.2]

    plt.pie(chart, explode=explode, autopct='%.2f')
    plt.legend(labels, loc="upper left", title="% of hotels charging:")
    plt.title("Hotel Cost Per Night (Sample Size = 226,030)")
    plt.show()

    """
    This data is showing me how many hotels charge in the different price brackets. 
    I.e. 43% of the hotels charge less than €105 per night.
    """


def task2():
    data = import_data()
    hostsNumbers = data.groupby(['host_id', 'host_name'])['host_id'].count().sort_values(ascending=False).nlargest(20,'first')
    # hosts = data.groupby(['host_id', 'host_name'])
    # bigHosts = hosts.count().sort_values(ascending=False).nlargest(20, 'first')
    labels = hostsNumbers.keys()

    hostName = []
    values = []

    for x in hostsNumbers:
        values.append(x)

    for x in labels:
        name = str(x[0]) + ": " + str(x[1])
        hostName.append(name)

    plt.bar(hostName, values, width=0.4)
    plt.xticks(rotation=45, ha='right')
    plt.xlabel("Names")
    plt.ylabel("No. of Accommodations")
    plt.title("20 Largest Hotel Moguls")
    plt.show()

    """
    Looking at the data, even though these are the 20 biggest hotel mogul's, it's clear that both Zues and Blueground
    own significantly more than the following moguls. This is most likely indicitive of a large hotel chain, hotels etc
    """


def task3():
    data = import_data()
    cheap500 = data[data['price'] < 500]
    prices = cheap500['price']

    plt.hist(prices, bins=90)
    plt.title("Prices Under 500")
    plt.xlabel("Cost Per Night")
    plt.ylabel("Frequency of price")

    plt.show()

    """
    Looking at the data it's clear the majority of the sub 500 hotels normally cost between 50 and 130. This, along with
    task 1 shows us that quite a lot of the hotels in the US are more aiming for an affordable per night cost of 100
    It's also more common to charge at €50 intervals which can be seen by the spikes located at 100, 150, 200, 250 etc
    """

def task4():
    data = import_data()
    less500 = data[data['price'] <= 500]
    range = less500[less500['price'] > 150]
    prices = range['price']

    plt.hist(prices, bins=100)
    plt.title("Prices Under 500 and over 150")
    plt.xlabel("Cost Per Night")
    plt.ylabel("Frequency of price")

    plt.show()

    """
    Due to the data having spikes plottig it as a line wouldn't work as the spikes at €50 intervals would mis-vizualize
    it. That's why I decided to use a histogram as it would display all the values inbetween those spikes.
    Looking at the graph there are no clear outliers in this range due to the number of hotels charging 500 per night
    and all of the hotels charging between 300 and 500.
    """

def task5():
    data = import_data()
    accomodationTypes = pd.unique(data['room_type'])

    #print(accomodationTypes)



task5()
