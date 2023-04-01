#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 16:42:24 2023

@author: giannidiarbi

Gianni Diarbi
 DS2000
 Spring 2023
 HW 4 Problem 3
 nola_v2.py
 
 Test Case:
     Ideal: 71, 52, 54
     Ideal List Becomes: [71, 52, 61.5, 54]
     
     Distance to here from 1992 - 
     72, 53, 62.5, 54
     (71 - 72)**2 + (52 - 53)**2 + (61.5 - 62.5)**2 + (54 - 54)** 2
     = 1 + 1 + 1 + 0
     And then sqrt(3) = 1.73  
"""

YEAR_POS = 0
MAX_POS = 1
MIN_POS = 2
MEAN_POS = 3
HUMIDITY_POS = 4

WEATHER_FILE = "nola_weather_feb.csv"

def main():
    # Gather data - prompt the user for their ideal high and low temps, 
    # as well as their ideal humidity 
    ideal_max = int(input("What is your ideal high temperature?\n"))
    ideal_min = int(input("What is your ideal low temperature?\n"))
    ideal_humidity = int(input("What is your ideal humidity?\n"))
    
    # Calculate the user's ideal mean 
    ideal_mean = ( ideal_max + ideal_min ) / 2
    
    # Create a list and append the user's ideal values to it
    # Calculate the ideal mean using the prompted ideal high and low values
    ideal_mean = ( ideal_max + ideal_min ) / 2
    
    # Create a list and append the user's values to it
    ideal_lst = []
    
    ideal_lst.append(ideal_max)
    ideal_lst.append(ideal_min)
    ideal_lst.append(ideal_mean)
    ideal_lst.append(ideal_humidity)
    
    # Initialize variables for the year and distance reported in later steps
    min_dist = 10000
    min_year = 0
    
    # Open the file and read in (skip) the header
    with open(WEATHER_FILE, "r") as infile:
        header = infile.readline()

        # Read in each line of weather data using a for loop
        for line in infile:
            
            # Turn the string line into a list of strings
            data_lst = line.split(",")
             
            # Categorize the data using their positions in the list
            year_data = int(data_lst[YEAR_POS])
            data_max = int(data_lst[MAX_POS])
            data_min = int(data_lst[MIN_POS])
            data_mean = float(data_lst[MEAN_POS])
            data_humidity = int(data_lst[HUMIDITY_POS])
            
            # Initialize distance in order to compare it later on
            dist = 0
            
            # Computations - calculate the euclidean distance between ideal 
            # and current weather
            dist = (((data_max - ideal_max) ** 2) + \
                    ((data_min - ideal_min) ** 2) + \
                        ((data_mean - ideal_mean) ** 2) + \
                            ((data_humidity - ideal_humidity) ** 2)) ** 0.5
            
            # Find the minimum distance and its associated year
            if dist < min_dist:
                min_dist = dist
                min_year = year_data
            
        # Communicate the results back to the user
        print("The year with the closest distance to your ideal is:", min_year)
        print("The distance at this year is:", round(min_dist, 2))
            
main()