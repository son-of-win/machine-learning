import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('dataset1.csv',header=0)
radio = data.values[:,2]
radio = np.array([radio]).T # lấy ma trận chuyển vị của mảng radio
sale = data.values[:,4]
plt.scatter(radio,sale,marker='o')

"""print(radio)

def predict(new_radio,weight, bias):
	return new_radio*weight + bias

def cost_function(radio,sale,weight,bias):
	tong_err = 0.0;
	n = len(radio)
	for i in range(n):
		tong_err += (sale[i] - (radio[i]*weight + bias))**2
	return tong_err/2
# hàm gradient descent
def update_weight(radio,sale, weight,bias, learning_rate):
	n = len(radio)
	weight_temp = 0.0
	bias_temp = 0.0
	for i in range(n):
		weight_temp += -2*radio[i]*(sale[i] - (radio[i]*weight + bias))
		bias_temp += -2*(sale[i] - (radio[i]*weight + bias))

	weight -= (weight_temp/n)*learning_rate
	bias -= (bias_temp/n)*learning_rate

	return weight, bias

def training(radio, sale, weight, bias, learning_rate, so_lan_lap):
	
	cost_history = []
	for i in range(so_lan_lap):
		weight, bias  = update_weight(radio, sale, weight, bias, learning_rate)
		cost = cost_function(radio, sale, weight, bias)
		cost_history.append(cost)

	return weight, bias, cost_history

weight, bias, cost = training(radio, sale, 0.01,0.0014,0.001,30)

plt.plot(radio,radio*weight+bias)

print(weight)
print(bias)"""
# Thêm số 1 vào đầu mảng X, xem chú thích ở file
one = np.ones((radio.shape[0], 1))
X = np.concatenate((one, radio), axis = 1)

# tính theo công thức
a = np.dot(X.T,X)
a_i = np.linalg.pinv(a)
b = np.dot(X.T,sale)
w = np.dot(a_i,b)
# weight = w[0], bias = w[1]
print(w)


