from sklearn import linear_model
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('dataset1.csv')
radio = data.values[:,2]
sale = data.values[:,4]
plt.scatter(radio,sale,color="red")
plt.xlabel("radio")
plt.ylabel("sale")

radio = np.array(radio)
radio = radio.reshape(-1,1)

reg = linear_model.LinearRegression()
reg.fit(radio,sale)

weight = reg.coef_[0]
bias = reg.intercept_

print(weight)
print(bias)
