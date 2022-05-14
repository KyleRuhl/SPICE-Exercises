import csv
import os
import numpy as np

pathin = '/Users/kyleruhl/documents/GitHub/SPICE-Exercises/Ewaste_Calculator_Python/'
filein = 'Ewaste_Product_Breakdown.csv' 
#DATAFILE UNITS: plastic, aluminium, copper in grams, total ewaste in kg, co2 in kg co2 equilavent

'''
SPICE [SUSTAINABILITY PEDAGOGY IN COMPUTER SCIENCE EDUCATION] E-WASTE MODULE SAMPLE ACTIVITY:

TASK: Create an ewaste calculator program that calculates a users total material usage (plastic, aluminium, copper, total materials) and carbon footprint
based on the number of common e-waste items they have used/discarded in their lifetime. Use the provided dataset Ewaste_Product_Breakdown.csv, available on 
the SPICE github, as a key for the material costs and carbon footprint of one of 18 common products.

SAMPLE ANSWER BELOW IN PYTHON. Programming language and tasks may be changed to fit course goals. 
'''

ewaste = []

with open(pathin+filein) as data:
    next(data) #skip top header lines in data file
    for row in data:
        row = row.strip().split(',') #load from .csv into list, seperate at each comma
        ewaste.append([h for h in row]) 

for i in range(len(ewaste)):
    for j in range(5):
        ewaste[i][j+1] = float(ewaste[i][j+1]) #convert from strings to floats, ignore col[0]

def checkformat(userin):
    if (userin >= 0): #check to make sure user input is a postiive number or 0
        return True
    else:
        return False

#interactive portion- get user input
'''
counts1 = []
print("To calculate your E-waste footprint, enter in digit format the following questions...")
for var in range(len(ewaste)):
    response = input("How many " + ewaste[var][0] + " Have You Discarded? ")
    response = int(response)
    if (checkformat(response) == True):
        counts1.append(response) #if a positive or 0 number, accept
    else:
         counts1.append(np.NaN) #if not, nan
'''
counts1 = [3,2,4,0,3,1,1,0,0,2,0,1,0,2,1,0,1,0] #preset input list for code testing purposes

plastic = []
aluminium = []
copper = []
total_ewaste = []
co2 = []

for k in range(len(ewaste)):
    #multiply number of devices * impact of one of said device
    plastic.append(counts1[k] * ewaste[k][1])
    aluminium.append(counts1[k] * ewaste[k][2])
    copper.append(counts1[k] * ewaste[k][3])
    total_ewaste.append(counts1[k] * ewaste[k][4])
    co2.append(counts1[k]*ewaste[k][5])

def screen_clear(): #clear command 
   # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('cls')

#CALCULATOR OUTPUT
screen_clear()
print('*** CALCULATING ***\n\n') 
print("You've collected a total of ", round(sum(total_ewaste),2), " kg of e-waste.") 
print("\nBroken into: \n")
print("         " ,round(sum(plastic),2) , " grams of plastic")
print("         " ,round(sum(aluminium),2) , " grams of aluminium")
print("         " ,round(sum(copper),2) , " grams of copper\n")
print("Correctly recycled, this saves up to " , round(sum(co2),2) , " Kg CO2 equilavent.\n")

#END    