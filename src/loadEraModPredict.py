import sys
import math
import netCDF4
import numpy as np
from scipy.interpolate import griddata
from datetime import datetime
from os.path import realpath, expanduser, join
import csv

# -------------------- Function section --------------------
# Read a ECMWF atmosphere NetCDF file
def ReadECMWF(File):
    # Input>  File: File name
    # Output> Lat: Latitude
    #         Lon: Longitude
    #         Time: Time
    #         u10/v10: 10m u/v-component of wind
    #         d2m : 2m dewpoint temperature
    #         stl: soil temperature level
    #         swvl: volumetric soil water layer
    #         slhf/sshf: surface latent/sensible heat flux
    #         ssrd: surface thermal radiation downwards
    #         svabs: evaporation from bare soil
    #         precipitation, leaf area index

    # following 2 commands list key varaibles from NetCDF
    #print(data.dimensions.keys())
    #print(data.variables.keys())
    var = ['longitude', 'latitude', 'time', 'u10', 'v10', 'd2m', 't2m', 'evabs', 'evaow', 'evatc', 'evavt', 'e', 'fal', 'lai_hv', 'lai_lv', 'pev', 'ro', 'src', 'skt', 'es', 'stl1', 'stl2', 'stl3', 'stl4', 'ssro', 'slhf', 'ssr', 'str', 'sp', 'sro', 'sshf', 'ssrd', 'strd', 'tp', 'swvl1', 'swvl2', 'swvl3', 'swvl4']
    # Open the NetCDF file
    F = netCDF4.Dataset(File, "r", format="NETCDF4")
    Data = {}
    # Latitude
    Data['Lat'] = F.variables['latitude'][:]
    # Longitude (Longitudes range from 0 to 360, which is equivalent to
    # -180 to +180 in Geographic coordinate systems)
    Data['Lon'] = F.variables['longitude'][:]
    # Time
    Data['Time'] = netCDF4.num2date(F.variables['time'][:],
                                    F.variables['time'].units,
                                    F.variables['time'].calendar)
    for i in range(3,37):#len(var)):
        print('loading ', var[i])
        Data[var[i]] = F.variables[var[i]][:]
    F.close()
    return Data

def loadMODIS(file):
    # Input>  File: File name
    # Output> PIXID: Pixel ID
    #         Lat: Latitude
    #         Lon: Longitude
    #         other variables see the MODIS/VIIRS csv files
    print('loading file: ', file)
    with open(file) as csv_file:
        data = np.loadtxt(csv_file, dtype='str',comments='#', delimiter=',', skiprows=1)
    print('modis file size: ',np.shape(data))
    return data


# Find the largest and smallest values based on Num for a given array
def RoundNearest(X, Num):
    # Input> X: A given array
    #        Num: The base to be rounded to
    # Output> DataMin: The smallest value based on Num in the array X
    #         DataMax: The largest value based on Num in the array X
    DataMax = math.ceil(max(X) / Num) * Num
    DataMin = math.floor(min(X) / Num) * Num
    return DataMin, DataMax

# -------------------- Main section --------------------

PathECMWF = '/cir2/ywang/Data/ERA5/data/'
FileECMWF = 'era520191211.nc'
print(datetime.now(),'loading dataset ...')

MODPath = '../dat/'
MODFile = 'fire_archive_M6_108775.csv'
dataflg = loadMODIS(realpath(expanduser(join(MODPath, MODFile))))

Dataland = ReadECMWF(realpath(expanduser(join(PathECMWF, FileECMWF))))

# loading the previous day dataset
FileECMWFn1 = 'era520191210.nc'
Datalandn1 = ReadECMWF(realpath(expanduser(join(PathECMWF, FileECMWFn1))))
FileECMWFn2 = 'era52019129.nc'
Datalandn2 = ReadECMWF(realpath(expanduser(join(PathECMWF, FileECMWFn2))))


#  output file
f=open('../dat/inputpredict.txt','w')

var = ['longitude', 'latitude', 'time', 'u10', 'v10', 'd2m', 't2m', 'evabs', 'evaow', 'evatc', 'evavt', 'e', 'fal', 'lai_hv', 'lai_lv', 'pev', 'ro', 'src', 'skt', 'es', 'stl1', 'stl2', 'stl3', 'stl4', 'ssro', 'slhf', 'ssr', 'str', 'sp', 'sro', 'sshf', 'ssrd', 'strd', 'tp', 'swvl1', 'swvl2', 'swvl3', 'swvl4']

geoflg = np.zeros(shape=(1801, 3600))

Num = 0.1
for i in range(1350,1936):
    lat = float(dataflg[i,0])
    lon = float(dataflg[i,1])
    lat0 = (math.floor(lat*10)/ 10)
    lon0 = (math.floor(lon*10)/ 10) + 180.0
    ECMWFLatIndex = [np.where(Dataland['Lat'] == lat0)]
    ECMWFLonIndex = [np.where(Dataland['Lon'] == lon0)]
    #print(ECMWFLatIndex,ECMWFLonIndex)
    #print(Dataland['Lat'][ECMWFLatIndex])
    #print(Dataland['Lon'][ECMWFLonIndex]-180)
    #print('v10',i,ECMWFLatIndex,ECMWFLonIndex,Dataland['v10'][2,ECMWFLatIndex,ECMWFLonIndex])

    geoflg[ECMWFLatIndex,ECMWFLonIndex] = 1

#print('longitude',Dataland['Lon'][1],Dataland['Lon'][3500])
ECMWFLatmin = [np.where(Dataland['Lat'] == 33)]
ECMWFLonmin = [np.where(Dataland['Lon'] == -125+180)]
ECMWFLatmax = [np.where(Dataland['Lat'] == 45)]
ECMWFLonmax = [np.where(Dataland['Lon'] == -114+180)]
#print(ECMWFLatmax,ECMWFLatmin,ECMWFLonmax,ECMWFLonmin)
ECMWFLatmax = 570
ECMWFLatmin = 450
ECMWFLonmin = 550
ECMWFLonmax = 660

for i in range(ECMWFLatmin,ECMWFLatmax):
    for j in range(ECMWFLonmin,ECMWFLonmax):
        if geoflg[i,j]==1:
            f.write(str(Dataland['Lat'][i])+' '+str(Dataland['Lon'][j]-180)+' ')
            for ii in range(3,37): #len(var)):
                f.write(str(Datalandn2[var[ii]][2,i,j])+' ')
            for ii in range(3,37): #len(var)):
                f.write(str(Datalandn1[var[ii]][2,i,j])+' ')
            for ii in range(3,37): #len(var)):
                f.write(str(Dataland[var[ii]][2,i,j])+' ')
            f.write(str(geoflg[i,j])+'\n')

for i in range(ECMWFLatmin,ECMWFLatmax):
    for j in range(ECMWFLonmin,ECMWFLonmax):
        if Dataland['t2m'][2,i,j]:
            f.write(str(Dataland['Lat'][i])+' '+str(Dataland['Lon'][j]-180)+' ')
            for ii in range(3,37): #len(var)):
                f.write(str(Datalandn2[var[ii]][2,i,j])+' ')
            for ii in range(3,37): #len(var)):
                f.write(str(Datalandn1[var[ii]][2,i,j])+' ')
            for ii in range(3,37):#len(var)):
                f.write(str(Dataland[var[ii]][2,i,j])+' ')
            f.write(str(geoflg[i,j])+'\n')

print('computation is finished')


