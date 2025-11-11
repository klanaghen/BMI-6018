#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np

df = pd.read_csv('Untitled Folder 1/diabetic_data.csv')

#Melt
melted = df.melt(
    id_vars=["encounter_id", "patient_nbr"],
    value_vars=med_columns,
    var_name="medication",
    value_name="med_status"
)

print("Melted Medication Table:")
print(melted.head())


#Pivot: Observing counts of race and gender, this gives us a better idea of demographics affected by diabetes 
pivot_table = df.pivot_table(
    index="race",
    columns="gender",
    values="encounter_id",
    aggfunc="count"
)

print("Pivot Table: Encounters by Race × Gender")
print(pivot_table)

#3: Aggregation: Avg stays, medications, and labs grouped by age group
agg_results = df.groupby("age")[["time_in_hospital", 
             "num_lab_procedures",
             "num_medications"]].agg(["mean", "median", "min", "max"])

print("Aggregation by Age Group:")
print(agg_results)

#Iteration: To see if each patient takes insulin and metformin: 
print("Iteration Example:")
for idx, row in df.head(10).iterrows():  # limit to first 10 for readability
    print(f"Patient {row['patient_nbr']} — insulin: {row['insulin']}, metformin: {row['metformin']}")

#Group By: 
readmit_by_diag = df.groupby("diag_1")["readmitted"].value_counts(normalize=True).unstack()

print("Readmission rate by primary diagnosis:")
print(readmit_by_diag)





# In[ ]:




