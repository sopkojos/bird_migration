import pandas as pd
import matplotlib.pyplot as plt
#pd.set_option('max_columns', None)
#df = pd.read_csv('artic_loon_import.csv', sep='\t',low_memory=False)


def ebird_import(filename):
    '''imports csv file. creates array for longitude and latitude of sightings. Generates an animated plot of the sightings over time '''
    df = pd.read_csv(filename, sep='\t', low_memory=False)
    #df = pd.read_csv('artic_loon_import.csv', sep='\t',low_memory=False)
    # formats csv file
    long = df['decimalLongitude']
    lat = df['decimalLatitude']
    # formats date columns
    # plt.scatter(long,lat)
    return [long, lat]


def average_latitude_position(yearmonth, latitude):
    '''calculates the average latitude of the species over the course of 1950-1980 then calculates monthly change over the entire period'''
    return [latitude_index]


def weather_import(weather_filename):
    '''imports csv file for NASAs GLOBAL LAND-OCEAN TEMPERATURE INDEX. function will also convert into the same date format as the latitude index'''
    df_w = pd.read_csv('weather_filename')
    return [temperature_index]


def correlation_func(long_index, weather_index):
    '''peforms statistical analysis between the latitude and weather indexes including plots'''
    return
