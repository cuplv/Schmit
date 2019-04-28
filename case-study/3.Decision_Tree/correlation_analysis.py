import numpy as np
import sys
import random
import scipy.io
import pandas as pd
import csv
from sklearn import preprocessing


csv_filename = sys.argv[1]
df = pd.read_csv(csv_filename)
num_rows = df.shape[0]

X = np.array(df)
XX = []
le = preprocessing.LabelEncoder()
flag_contains = False
for x in X.T:
    for e in x:
        if "y" in str(e):
            flag_contains = True
    if flag_contains:
        print x
        le_fit = le.fit(x)
        arr = le.transform(x)
        XX.append(arr)
    else:
        XX.append(x)
    flag_contains = False
XX = np.asarray(XX,dtype='int64')
X = XX.T

df = pd.DataFrame(X, columns = df.columns)

M = df.corr()

if "/" in csv_filename:
    csv_filename_path = csv_filename.split("/")[0]
else:
    csv_filename_path = csv_filename

M.to_csv(csv_filename_path + "/" + "correlation_analysis.csv")
