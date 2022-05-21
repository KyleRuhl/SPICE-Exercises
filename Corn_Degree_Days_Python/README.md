#Corn Growing Degree Days

TASK: Create a Growing Degree Day Calculator for Corn using the given 2021 weather observation dataset Ithaca_2021_wxdata.csv

Calculate the Corn growing degree days for April and May of the 2021 growing season using the following information:

Growing Degree Days (GDD) is calculated using the following formula:

>Average Temperature - 50, where Tavg = (Tmax + Tmin) /2, and Tmax is capped at 86 degrees F, where any value >86 should be set to 86 before taking the average.
>>[For reference, Corn does not grow under 50 degrees F and does not growth maxes out at 86F, hence our limits]

Where the GDD for the period is given by summing the **positive** daily GDDs over the period only. 

Then, Categorize the corn growing status over the given period by using the following decision rules:
<100 GDD = Poor 
100-200 GDD = Good
>200 GDD = Very Good

Finally, calculate the total rainfall (in inches) over the given period. 
Then output to the console the total number of GDD days, the total rainfall, and the corn status for the time period. 

---
Additional Resources for Corn Growing Degree Days:
http://climatesmartfarming.org/tools/csf-growing-degree-day-calculator/ from Cornell University
https://mrcc.purdue.edu/gismaps/info/gddinfo.htm from Purdue University

To find a dataset in a different year or location, go to https://www.ncdc.noaa.gov/cdo-web/search,
select 'Daily Summaries', your perfered date range, 'zip codes', enter your zip code, and press search. 
Press 'add to cart' on the station you want, then press the orange cart button to go to your cart.
In output format, choose 'Custom GHCN-Daily CSV', verify your date range, and press continue.
Deselect station name. Under select data types, under 'Precipitation' select 'Precipitation (PRCP)'. 
Under 'Air Temperature', select both 'Maximum temperature (TMAX)' and 'Minimum temperature (TMIN)'.
Press continue. Enter your email address and sumbit the order. Data will then be available to download in csv format in <5 min. 

*Last Updated 5/21/2022*