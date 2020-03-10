# wildfire Detection Demo
developed a predict and detect wildfire system

## Problem

Develop wildfire warning and detection system demo using python, SQL, arcGIS under Linux.

This system has following functions:

* Download wildfire measurement data (weather model NetCDF outputs, MODIS, and VIIRS satellite datasets) automatically.
* Statistically analyze the current fire situation in the remote sensing images
* Predict the watching area based on the last 3 day's weather conditions using machine learning approach
* Outputs prediction results to SQL and visulazed in ArcGIS.

### Directory Structure

    ├── README.md
    |
    ├── src
    │   └── download.sh
    │   └── queryERA5.py
    │   └── loadEraModPredict.py
    │   └── trainmodel.py
    │   └── iodatapredict.py
    │   └── genCSV.py
    ├── input
    │   └── ERA5 reanalysis data
    │   └── MODIS Collection 6 satellite product
    │   └── VIIRS 375m data satellite product
    ├── output
    |   └── output.csv
    
### Usage

1. This system downloaded satellite products from MODIS and VIIR satellites. Download is [here](https://earthdata.nasa.gov/earth-observation-data/near-real-time/firms/active-fire-data)

The dataset can be plotted in Python, ArcGIS, or others.
![](https://github.com/IanWang15/wildfireDetectionDemo/blob/master/image/MODIS201912.png)
MODIS fire dataset between 12-01-2019 and 12-31-2019

2. The reanalysis data is from ECMWF ERA5. Download is [here](https://cds.climate.copernicus.eu/cdsapp#!/search?type=dataset&keywords=((%20%22Product%20type:%20Reanalysis%22%20))&text=era5)
![](https://github.com/IanWang15/wildfireDetectionDemo/blob/master/image/era5d2m20191201.png)

3. The model is based on the neural network
![](https://github.com/IanWang15/wildfireDetectionDemo/blob/master/image/results.png)

## Questions?
Email me at yiwangtamu@gmail.com

