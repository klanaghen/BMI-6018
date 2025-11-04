#!/usr/bin/env python
# coding: utf-8

# In[24]:


#Libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Importing Data
flights_data = pd.read_csv('Untitled Folder 1/flights.csv')
flights_data.head(10)
weather_pd = pd.read_csv('Untitled Folder 1/weather.csv')
weather_np = weather_pd.to_numpy()
# Pandas Data Filtering/Sorting Question Answering
#use flights_data

#Question 1 How many flights were there from JFK to SLC? Int
q_1 = len(flights_data[(flights_data['origin'] == 'JFK') &
                       (flights_data['dest'] == 'SLC')])
print("Question 1:", q_1)

#Question 2 How many airlines fly to SLC? Should be int
q_2 = flights_data[flights_data['dest'] == 'SLC']['carrier'].nunique()
print("Question 1:",q_2)

#Question 3 What is the average arrival delay for flights to RDU? float
q_3 = flights_data[flights_data['dest'] == 'RDU']['arr_delay'].mean()
print("Question 3:",q_3)

#Question 4 What proportion of flights to SEA come from the two NYC airports (LGA and JFK)?  float
sea_flights = flights_data[flights_data['dest'] == 'SEA']
q_4 = len(sea_flights[sea_flights['origin'].isin(['LGA','JFK'])]) / len(sea_flights)
print("Question 4:",q_4)

#Question 5 Which date has the largest average depature delay? Pd slice with date and float
#please make date a column. Preferred format is 2013/1/1 (y/m/d)
flights_data['date'] = pd.to_datetime(flights_data[['year','month','day']])
q_5 = flights_data.groupby('date')['dep_delay'].mean().idxmax(), \
      flights_data.groupby('date')['dep_delay'].mean().max()
print("Question 5:",q_5)

#Question 6 Which date has the largest average arrival delay? pd slice with date and float
flights_data['date'] = flights_data['date'].dt.strftime('%Y/%m/%d')
q_6 = flights_data.groupby('date')['arr_delay'].mean().idxmax(), \
      flights_data.groupby('date')['arr_delay'].mean().max()
print("Question 6:",q_6)

#Question 7 Which flight departing LGA or JFK in 2013 flew the fastest? pd slice with tailnumber and speed
#speed = distance/airtime
subset = flights_data[flights_data['origin'].isin(['LGA','JFK'])].copy()
subset['speed'] = subset['distance'] / subset['air_time']
q_7 = subset.loc[subset['speed'].idxmax(), ['tailnum','speed']]
print("Question 7:",q_6)

#Question 8 Replace all nans in the weather pd dataframe with 0s. Pd with no nans
q_8 = weather_data_pd.fillna(0)
print("Question 8:",q_8)


# In[36]:


#%% Numpy Data Filtering/Sorting Question Answering
#Use weather_data_np # month = column 2 but have to change type
#Just file checks

weather_pd = pd.read_csv('Untitled Folder 1/weather.csv')
weather_np = weather_pd.to_numpy()
weather_pd.head(10)
weather_pd.columns


# In[32]:


# Numpy Questions 

#Normalize month column (column 2) to clean strings
months = np.char.strip(weather_np[:, 2].astype(str))

#Filter for February rows
feb_rows = weather_np[months == "2"]

#Question 9: How many observations in February?
q_9 = feb_rows.shape[0]
print("Question 9:", q_9)

# Convert humidity column to numeric 
humidity = pd.to_numeric(feb_rows[:, 7], errors='coerce').astype(float)

# Question 10: Mean humidity for February
q_10 = np.nanmean(humidity)
print("Question 10 (mean humidity):", q_10)

# Question 11: Std of humidity for February
q_11 = np.nanstd(humidity)
print("Question 11 (std humidity):", q_11)

