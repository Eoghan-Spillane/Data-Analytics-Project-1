#Author: Eoghan Spillane
#Description:

#pip install numpy==1.19.3
#pip install pandas
#pip install -U matplotlib

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def import_data():
    data = pd.read_csv('us-Hotel.csv')
    return data

def main():
    print(import_data())

main()
