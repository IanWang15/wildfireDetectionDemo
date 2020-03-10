import numpy as np
from sklearn.neural_network import MLPRegressor
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import datetime
from sklearn.model_selection import ShuffleSplit

# this program uses to train models using sklearn
# input is prepared data 1) training data 2) testing data
# output is the predict results

print(datetime.datetime.now(), 'loading data ...')
Xtrain = np.loadtxt('../dat/xtrain.txt')
Ytrain = np.loadtxt('../dat/ytrain.txt')

print('shape:', np.shape(Xtrain))
print(datetime.datetime.now(), 'training data ...')
rs = ShuffleSplit(n_splits = 5, test_size = .1, random_state = 0)
rs.get_n_splits(Xtrain)

#Xtrain, Xtest, Ytrain, Ytest = train_test_split(Xtrain, Ytrain, test_size=0.1, random_state=88)
#rs = ShuffleSplit(n_splits = 5, test_size = .1, random_state = 0)
#rs.get_n_splits(Xtrain)

scaler  = StandardScaler()
scaler_model = scaler.fit(Xtrain)
X_train_trans = scaler_model.transform(Xtrain)

Xtest = np.loadtxt('../dat/xtest20191211.txt')
X_test_trans = scaler_model.transform(Xtest)

clf = MLPClassifier(hidden_layer_sizes=(128,64,), activation = 'relu', solver = 'adam', \
                   alpha = 0.0001, batch_size = 'auto', learning_rate = 'adaptive', \
                   learning_rate_init = 0.001, power_t = 0.5, max_iter=2000, tol = 1e-4)

clf_model = clf.fit(X_train_trans, Ytrain)
pred = clf_model.predict(X_test_trans)

Ytest = np.loadtxt('../dat/ytest20191211.txt')

from sklearn.metrics import mean_squared_error

np.savetxt('../dat/outputv2x.txt', pred)

print(mean_squared_error(Ytest, pred))
print(clf_model.score(X_test_trans, Ytest))

print(datetime.datetime.now(), 'computation is finished ...')

