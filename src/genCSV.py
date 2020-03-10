import numpy as np

# this program uses to select the pixel that predict as high probility area that
# may be affected by wildfire
# input is machine learning output
# output is the csv file used for ArcGIS

f0 = np.loadtxt('../dat/outputv3x.txt')

fmet = np.loadtxt('../dat/input20191211.txt')

f1 = np.zeros(shape = (len(fmet), np.shape(fmet)[1]))

for i in range(len(fmet)):
    for j in range(0,np.shape(fmet)[1]):
        f1[i,j] = float(fmet[i,j])


f2 = np.zeros(shape = (len(f0), 3))

ii = 0
for i in range(len(f0)):
    if f0[i] == 1:
        f2[ii,0] = fmet[i,0]
        f2[ii,1] = fmet[i,1]
        f2[ii,2] = 1
        ii = ii + 1

np.savetxt('../dat/predictv2.csv', f2[:ii-1,:], fmt='%10.5f')
print('csv file is ready')
