#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Question 1 — Euclidean Distance Between Two Series

p = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
q = pd.Series([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])

diff = p - q
q1 = np.sqrt(np.sum(diff**2))

print("\nQ1 — Euclidean Distance:")
print(q1)

# Question 2 — Swap Columns 'a' and 'c'

df2 = pd.DataFrame(np.arange(20).reshape(-1, 5), columns=list('abcde'))

cols = df2.columns.tolist()
cols[0], cols[2] = cols[2], cols[0]   # swap 'a' and 'c'

q2 = df2[cols]

print("\nQ2 — Swap columns 'a' and 'c':")
print(q2)

#Question 3 — Generic Column Swap Function

df3 = pd.DataFrame(np.arange(20).reshape(-1, 5), columns=list('abcde'))

def swap_columns(df, col1, col2):
    cols = df.columns.tolist()
    i, j = cols.index(col1), cols.index(col2)
    cols[i], cols[j] = cols[j], cols[i]
    return df[cols]

q3 = swap_columns(df3, 'b', 'e')

print("\nQ3 — Generic column swap (b <-> e):")
print(q3)

#Question 4 — Suppress Scientific Notation, 4 decimals

df4 = pd.DataFrame(np.random.random(4)**10, columns=['random'])

q4 = df4.copy()
q4['random'] = q4['random'].apply(lambda x: format(x, '.4f'))

print("\nQ4 — Scientific notation removed, 4 decimals:")
print(q4)

#Question 5 — Nearest Row by Euclidean Distance

df5 = pd.DataFrame(
    np.random.randint(1, 100, 40).reshape(10, 4),
    columns=list('pqrs'),
    index=list('abcdefghij')
)

# Compute pairwise distance matrix
distances = pd.DataFrame(index=df5.index, columns=df5.index)

for i in df5.index:
    for j in df5.index:
        distances.loc[i, j] = np.sqrt(((df5.loc[i] - df5.loc[j])**2).sum())

nearest = []
dvals = []

for i in df5.index:
    d = distances.loc[i].replace(0, np.nan)  # ignore distance to itself
    nearest_row = d.idxmin()
    nearest_dist = d.min()
    nearest.append(nearest_row)
    dvals.append(nearest_dist)

df5['nearest_row'] = nearest
df5['dist'] = dvals

print("\nQ5 — Nearest row by Euclidean distance:")
print(df5)

#Question 6 — Correlation Matrix

data6 = {
    'A': [45, 37, 0, 42, 50],
    'B': [38, 31, 1, 26, 90],
    'C': [10, 15, -10, 17, 100],
    'D': [60, 99, 15, 23, 56],
    'E': [76, 98, -0.03, 78, 90]
}

df6 = pd.DataFrame(data6)
q6 = df6.corr()

print("\nQ6 — Correlation matrix:")
print(q6)


# In[ ]:




