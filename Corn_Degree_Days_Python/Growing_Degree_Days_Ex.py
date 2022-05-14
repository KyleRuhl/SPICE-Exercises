'''
TASK: Create a Growing Degree Day Calculator for Corn using the given 2021 weather observation dataset Ithaca_2021_wxdata.csv

Calculate the Corn growing degree days for April and May of the 2021 growing season using the following information:

*Growing Degree Days (GDD) is calculated using the following formula:
Average Temperature - 50, where Tavg = (Tmax + Tmin) /2, and Tmax is capped at 86 degrees F, where any value >86 should be set to 86 before taking the average.
<For reference, Corn does not grow under 50 degrees F and does not growth maxes out at 86F, hence our limits>

Where the GDD for the period is given by summing the positive daily GDDs over the period only. 

*Then, Categorize the corn growing status over the given period by using the following decision rules:
<100 GDD = Poor 
100-200 GDD = Good
>200 GDD = Very Good

*Finally, calculate the total rainfall (in inches) over the given period. 
*Then output to the console the total number of GDD days, the total rainfall, and the corn status for the time period. 

--------------------------------------------------
Additional Resources for Corn Growing Degree Days:
http://climatesmartfarming.org/tools/csf-growing-degree-day-calculator/ from Cornell University
https://mrcc.purdue.edu/gismaps/info/gddinfo.htm from Purdue University

To find a dataset in a different year or location, go to https://www.ncdc.noaa.gov/cdo-web/search?datasetid=GHCND,
select 'Daily Summaries', your perfered date range, 'zip codes', enter your zip code, and press search. 
Press 'add to cart' on the station you want, then press the orange cart button to go to your cart.
In output format, choose 'Custom GHCN-Daily CSV', verify your date range, and press continue.
Deselect station name. Under select data types, under 'Precipitation' select 'Precipitation (PRCP)'. 
Under 'Air Temperature', select both 'Maximum temperature (TMAX)' and 'Minimum temperature (TMIN)'.
Press continue. Enter your email address and sumbit the order. Data will then be available to download in csv format in <5 min. 

The following is an example solution in Python:
'''

##Step 1: Load Data
import numpy as np
pathin = '/Users/kyleruhl/Documents/GitHub/SPICE-Exercises/Corn_Degree_Days_Python/Ithaca_2021_wxdata.csv'

data = [] 
with open(pathin) as ourfile: 
    next(ourfile)
    for row in ourfile:
        row = row.strip().split(',') #seperate values by commma
        data.append([i for i in row]) #load into data list
        
##Step 2: Narrow down your dates from the year-long data set
#From the 2021 weather data for Ithaca, create a new list with only April & May observations
aprilmay_data = []
for obs in range(len(data)):
    date = data[obs][0]
    if((date[:1] == "4") or (date[:1]=="5")): #check for april or may
        aprilmay_data.append(data[obs]) #if in april or may, append to aprilmay_data list

##Step 3: Calculate the daily temperature average by taking (tmax-tmin)/2
gdd = []
for i in range(len(aprilmay_data)):
    tmax = float(aprilmay_data[i][2])
    if(tmax > 86.0): #cap high temp at 86 degrees F
        tmax = 86.0 
    tmin = float(aprilmay_data[i][3])
    taverage = (tmax+tmin)/2 #calc daily average
    gdd.append(taverage-50) #Subtract 50 (minimum corn growing temperature), append to ggd

##Step 4: Sum the total growing degree days for corn in the time period
totalGDD = 0 #sum of GDD, starts at zero
for k in range(len(gdd)): 
    if gdd[k]<0: #if the GDD is negative, set it equal to zero (no growth)
        gdd[k]=0
    else:
        totalGDD = totalGDD + gdd[k] #if the GGD is positive, add it to the total sum of GGD in deg. F

## Step 5: Categorize local corn status by GDD Total 
if totalGDD < 100.: #if totalGDD is less than 100, poor status set
    cornStatus = 'Poor'
else:
    if(totalGDD >= 100. and totalGDD < 200.):
        cornStatus = 'Good' #if totalGGD is >= 100 but <200 sets good status
    else:
        cornStatus = 'Very Good' #all else if totalGDD is greater than or equal to 200, very good status set

##Step 6: Calculate total rainfall
totalRain = 0
for h in range(len(aprilmay_data)):
    totalRain = totalRain + float(aprilmay_data[h][1])    

## Step 7: Print Outputs in Console 
lastday = len(aprilmay_data)-1
print('\nTime Period: ', aprilmay_data[0][0], " to ", aprilmay_data[lastday][0])
print('\nTotal Number of GDD =', totalGDD, 'F') #print total number of gdd in F
print('Total Precipitation =', totalRain, 'Inches') #print total rain in inch
print('\nCorn is in', cornStatus, 'Shape\n') #prints corn status

#END