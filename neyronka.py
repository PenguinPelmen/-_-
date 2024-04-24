import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, mean_squared_error, r2_score
import math

data = pd.read_csv("C:/Users/Maks/PycharmProjects/HACKATHON/Ar.dat", delimiter=' ')
column_array_x = data['Uinx'].values
column_array_y = data['Uiny'].values
column_array_z = data['Uinz'].values
column_array_x0 = data['Uoutx'].values
column_array_y0 = data['Uouty'].values
column_array_z0 = data['Uoutz'].values
target_in = ['Freeze', 'Temperature', 'Uinx', 'Uiny', 'Uinz']
x = data[target_in]
target_out = ['Uoutx', 'Uouty', 'Uoutz']
y = data[target_out]
train_x, test_x, train_y, test_y = train_test_split(x, y)
regr = RandomForestRegressor(random_state=0)
clf=regr.fit(train_x, train_y)
#clf = LinearRegression().fit(train_x, train_y)
predict = clf.predict(test_x)
mse = mean_squared_error(test_y, predict)
print("Mean Squared Error:", mse)
# Коэффициент детерминации
r_squared = r2_score(test_y, predict)
print("R-squared:", r_squared)
