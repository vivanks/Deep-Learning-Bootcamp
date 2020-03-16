import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt

#read data
dataframe = pd.read_csv('bmi.csv')
x_values = dataframe[['Life expectancy']]
y_values = dataframe[['BMI']]

#train model on data
model = linear_model.LinearRegression()
model.fit(x_values,y_values)

#visualize results
plt.scatter(x_values,y_values)
plt.plot(x_values,model.predict(x_values),color='red')
plt.show()