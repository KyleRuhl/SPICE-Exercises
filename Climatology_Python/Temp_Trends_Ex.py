'''
Assignment: Create and plot a time series of average yearly maximum and minimum temperatures at a given location.
The sample response uses weather data from the weather station at an airport in Pheonix, Arizona from 1933-2021

This project incorporates matplotlib, pandas, datetime string conversions, and temperature trends.

To download a CSV datafile, students should go to https://crt-climate-explorer.nemac.org/?lat=33.45&lon=-112.07&mode=daily_vs_climate&zoom=9
and enter a city of their choice. Then, click on 'Historical Weather Data'. They should then select a station.
Next, press 'Downloads' > 'Download temperature data' and retrieve their CSV file. 

The instructor may want to preselect a dataset(s) as some stations have significant gaps in data collection. 
SPICE has provided a few preselected datasets on the github (https://github.com/KyleRuhl/SPICE-Exercises)

After plotting, have students analyze the plot- are temperatures increasing or decreasing at your location over time? 
Consider climate change trends vs weather variability. What do you think your plot is telling you? 
What other factors could account for the yearly changes in temperature at your location?  
'''
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import pandas as pd
import datetime

pathin = '/Users/kyleruhl/Documents/GitHub/SPICE-Exercises/Climatology_Python/PHX_Temps.csv'

PHXtemps = pd.read_csv(pathin, na_filter=True) #load CSV 
PHXtemps['date'] =  pd.to_datetime(PHXtemps['date'], format='%Y%m%d') #convert from str to datetime

#group by year and calculate mean (a crude climatology)
PHX_clim = PHXtemps.groupby(PHXtemps.date.dt.year)['min','max','normal_min','normal_max'].mean()
PHX_clim = PHX_clim.drop(labels=2022,axis=0) #Drop current year in progress (will not be an accurate reflection)

fig = plt.figure()
plt.plot(PHX_clim['min'], color="blue", label='Avg Min Temps') #plot average min temps
plt.plot(PHX_clim['max'], color="red", label='Avg Max Temps') #plot average max temps
#plt.plot(PHX_clim['max']-PHX_clim['min'], color="green", label='Avg Max-Min') #plot max-min
plt.title("Phoenix, AZ Climatology")
plt.ylabel("Temperature (deg F)")
plt.xlabel("Year")
plt.grid(True)
plt.legend()
plt.show()
fig.savefig('PHX.png')

#END