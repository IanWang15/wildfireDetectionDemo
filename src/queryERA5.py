import cdsapi
import sys
import datetime

print(datetime.datetime.now())
c = cdsapi.Client()

day = sys.argv[1] 
filename = '../data/era5201912'+sys.argv[1]+'.nc'
c.retrieve(
    'reanalysis-era5-land',
    {
        'variable': [
            '10m_u_component_of_wind', '10m_v_component_of_wind', '2m_dewpoint_temperature',
            '2m_temperature', 'evaporation_from_bare_soil', 'evaporation_from_open_water_surfaces_excluding_oceans',
            'evaporation_from_the_top_of_canopy', 'evaporation_from_vegetation_transpiration', 'evapotranspiration',
            'forecast_albedo', 'leaf_area_index_high_vegetation', 'leaf_area_index_low_vegetation',
            'potential_evaporation', 'runoff', 'skin_reservoir_content',
            'skin_temperature', 'snow_evaporation', 'soil_temperature_level_1',
            'soil_temperature_level_2', 'soil_temperature_level_3', 'soil_temperature_level_4',
            'sub_surface_runoff', 'surface_latent_heat_flux', 'surface_net_solar_radiation',
            'surface_net_thermal_radiation', 'surface_pressure', 'surface_runoff',
            'surface_sensible_heat_flux', 'surface_solar_radiation_downwards', 'surface_thermal_radiation_downwards',
            'total_precipitation', 'volumetric_soil_water_layer_1', 'volumetric_soil_water_layer_2',
            'volumetric_soil_water_layer_3', 'volumetric_soil_water_layer_4',
        ],
        'year': '2019',
        'month': '12',
        'day': day,
        'time': [
            '00:00', '06:00', '12:00',
            '18:00',
        ],
        'format': 'netcdf',
    },
    filename)

print(datetime.datetime.now())
print('computation finished')

