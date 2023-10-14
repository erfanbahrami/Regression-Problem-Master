import keras
import pandas
import IPython
from keras.models import Sequential
from keras.layers import Dense
from keras.activations import *
from keras.optimizers import RMSprop
from keras.callbacks import EarlyStopping
from sklearn.datasets import make_regression
from sklearn.preprocessing import MinMaxScaler
from sklearn import preprocessing
from sklearn.preprocessing import scale
# read data from file
df = pandas.read_csv("data_1_out.csv")

X = df[['X1', 'X2', 'X3']].astype('float64')
y = df['Y'].astype('float64')

scalarX, scalarY = MinMaxScaler(), MinMaxScaler()
scalarX.fit(X)

x_train = X.to_numpy(dtype='float64')
y_train = y.to_numpy(dtype='float64')

model = keras.Sequential([Dense(1, kernel_initializer = 'normal', activation = 'relu', input_shape=(3,))])
#model = Sequential()
#model.add(Dense(64, kernel_initializer = 'normal', activation = 'relu', input_shape = (3,)))
#model.add(Dense(64, activation = 'relu'))
#model.add(Dense(1))
model.compile(
   loss = 'mse',
   optimizer = RMSprop(0.001), #('empty')
   metrics = ['mean_absolute_error', 'mse']
)

history = model.fit(
   x_train, y_train,
   batch_size=128,
   epochs = 500,
   verbose = 1,
   validation_split = 0.2
)

Xnew, a = make_regression(n_samples=3, n_features=3, noise=0.1, random_state=1)
Xnew = scalarX.transform(Xnew)
ynew = model.predict(Xnew)
print(model.layers[0].weights)
print(Xnew)
print(ynew)

IPython.embed()
#print(history)
#prediction = model.predict(x_train)
#model.layers[0].weights
