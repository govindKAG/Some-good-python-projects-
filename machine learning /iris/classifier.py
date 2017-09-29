import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

from subprocess import check_output
print(check_output(['ls', './iris-species']).decode('utf8'))

iris = pd.read_csv("./iris-species/Iris.csv")
# print(iris['Species'])
# print(iris.dtypes)

iris["Species"] = iris["Species"].map(
    {"Iris-setosa": 0, "Iris-virginica": 1, "Iris-versicolor": 2})
# just changing up those labels into integers
print(iris.iloc[:,1:5])
x_train, x_test, y_train, y_test = train_test_split(iris.iloc[:,1:5], iris["Species"], test_size=0.33, random_state=42)
