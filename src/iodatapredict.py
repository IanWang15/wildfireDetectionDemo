import numpy as np
# this program used to prepare data for training and testing
# data from ERA5 NetCDF file and from MODIS/VIIRS satellite csv files

# prepare training data
f0 = np.loadtxt('../dat/input20191210.txt')
f1 = np.zeros(shape = (len(f0), np.shape(f0)[1]))

for i in range(len(f0)):
    for j in range(0,np.shape(f0)[1]):
        f1[i,j] = float(f0[i,j])

np.savetxt('../dat/xtrain20191210.txt', f1[:200,3:-2], fmt='%10.5f')
np.savetxt('../dat/ytrain20191210.txt', f1[:200,-1], fmt='%10.5f')


# prepare testing data
f0 = np.loadtxt('../dat/inputpredict.txt')
f1 = np.zeros(shape = (len(f0), np.shape(f0)[1]))

for i in range(len(f0)):
    for j in range(0,np.shape(f0)[1]):
        f1[i,j] = float(f0[i,j])

np.savetxt('../dat/xtest20191211.txt', f1[:,3:-2], fmt='%10.5f')
np.savetxt('../dat/ytest20191211.txt', f1[:,-1], fmt='%10.5f')

print('data preparation is finished')

