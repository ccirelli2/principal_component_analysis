import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import load_iris


iris = load_iris()
colnames = iris.feature_names
data = pd.DataFrame(iris.data, columns=colnames)
print(data)
