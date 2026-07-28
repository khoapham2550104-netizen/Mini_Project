import os
os.environ['OMP_NUM_THREADS'] = '1'

import pandas as pd
import numpy as np
import pickle


from sklearn.linear_model import LinearRegression

data_file = pd.read_csv("all_combination.csv")

X = data_file.iloc[:,:]
linear_model = LinearRegression()


