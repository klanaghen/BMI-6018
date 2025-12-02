#!/usr/bin/env python
# coding: utf-8

# In[18]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans


diabetic_data = pd.read_csv('diabetic_data.csv')
#, usecols = ['race', 'gender', 'age'])
#print(diabetic_data.head())

df = diabetic_data



# In[19]:


numeric_cols = [
    "time_in_hospital",
    "num_lab_procedures",
    "num_procedures",
    "num_medications",
    "number_outpatient",
    "number_emergency",
    "number_inpatient",
    "number_diagnoses"
]

numeric_df = df[numeric_cols].copy()

# Replace "?" with NaN and drop missing rows
numeric_df = numeric_df.replace("?", np.nan).dropna()

numeric_df.head()


# In[20]:


#Subsample for faster computation
numeric_df = numeric_df.sample(10000, random_state=42)

scaler = StandardScaler()
scaled_data = scaler.fit_transform(numeric_df)
scaled_data[:5]


# In[21]:


sse = []
K_range = range(1, 11)

for k in K_range:
    km = KMeans(n_clusters=k, n_init='auto', random_state=42)
    km.fit(scaled_data)
    sse.append(km.inertia_)


# In[22]:


plt.figure(figsize=(8,4))
plt.plot(K_range, sse, marker='o')
plt.title("Elbow Method for Optimal k")
plt.xlabel("Number of clusters (k)")
plt.ylabel("Sum of Squared Errors (SSE)")
plt.xticks(K_range)
plt.grid(True)
plt.show()


# In[23]:


optimal_k = 3

kmeans = KMeans(n_clusters=optimal_k, random_state=42)
clusters = kmeans.fit_predict(scaled_data)

numeric_df["cluster"] = clusters
numeric_df.head()


# In[24]:


x_feature = "num_lab_procedures"
y_feature = "num_medications"

plt.figure(figsize=(8,6))
plt.scatter(
    numeric_df[x_feature],
    numeric_df[y_feature],
    c=numeric_df["cluster"],
    cmap="viridis",
    alpha=0.4
)

plt.xlabel(x_feature)
plt.ylabel(y_feature)
plt.title(f"K-Means Clusters Using {x_feature} and {y_feature}")

# Convert centroids back to original units
centroids = scaler.inverse_transform(kmeans.cluster_centers_)

plt.scatter(
    centroids[:, numeric_cols.index(x_feature)],
    centroids[:, numeric_cols.index(y_feature)],
    s=200,
    c="red",
    marker="X",
    label="Centroids"
)

plt.legend()
plt.show()


# In[25]:


centroid_df = pd.DataFrame(
    scaler.inverse_transform(kmeans.cluster_centers_),
    columns=numeric_cols
)

centroid_df


# In[ ]:




