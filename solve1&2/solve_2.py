import pandas
from sklearn import linear_model

df = pandas.read_csv("out_2.csv")

X = df[['X1', 'X2', 'X3', 'X4']]
y = df['Y']

regr = linear_model.LinearRegression()
regr.fit(X, y)

print(regr.coef_)
