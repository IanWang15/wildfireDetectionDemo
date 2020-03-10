# Wildfire Detection Demo
This demo is used to predict and detect wildfire using weather reanalysis data and also satellite detections.

## Problem

Develop wildfire warning and detection system demo using python, SQL, arcGIS under Linux.

This demo has the following functions:

* Download wildfire measurement data (weather model NetCDF outputs, MODIS, and VIIRS satellite datasets) automatically.
* Statistically analyze the current fire situation in the remote sensing images
* Predict the watching area based on the last 3 day's weather conditions using machine learning approach
* Outputs prediction results to SQL and visulazed in ArcGIS.

### Directory Structure

    ├── README.md
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

1. This system downloaded satellite products from MODIS and VIIR satellites. Download is from NASA earthdata center [here](https://earthdata.nasa.gov/earth-observation-data/near-real-time/firms/active-fire-data)

The dataset can be plotted in Python, ArcGIS, or others.

![](https://github.com/IanWang15/wildfireDetectionDemo/blob/master/image/MODIS201912.png)
Figure 1. MODIS fire dataset between 12-01-2019 and 12-31-2019

2. The reanalysis data is from ECMWF ERA5. The resolution is 1degree times 1 degreee. Download is from ECMWF [here](https://cds.climate.copernicus.eu/cdsapp#!/search?type=dataset&keywords=((%20%22Product%20type:%20Reanalysis%22%20))&text=era5)

It is okay to download dataset manually, but also able to download automatically. This download code is written by Python 3 + Bash scripts. To run this code, just simply execute

`./download.sh`

This script will call queryERA5.py to download data automatically. You can modify the parameters in queryERA5.py to change date, variable, and temperal resolution.

![](https://github.com/IanWang15/wildfireDetectionDemo/blob/master/image/era5d2m20191201.png)
Figure 2. 2m dewpoint temperature from ERA5 reanalysis dataset between 12-01-2019 and 12-31-2019

3. Reading, processing, and preparing data can execute

`python loadEraModPredict.py`

This code will read the last 3 day's ERA5 data and current MODIS detection data simultaneously. It is able to change the selected region by changing latitude and longitude in this code. Current setting is select Western coast region in US.

4. The model is based on the logistical neural network approach. The comparation between satellite detection and detection system prediction is displayed in ArcGIS.

![](https://github.com/IanWang15/wildfireDetectionDemo/blob/master/image/results.png)
Figure 3. The fire measurements from MODIS and VIIRS (red points) and prediction from this detection system (heatmap).

## Limitation

This system currently relys on 1degree times 1 degreee resolution data from ECMWF ERA5 reanalysis dataset. It is able to convert to use high resolution weather model outputs like WRF.

By collecting more data to train this system, I suppose the prediction accuracy rate will be further improved. 

## Questions?
Email me at yiwangtamu@gmail.com

