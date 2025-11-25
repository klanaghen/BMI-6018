#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


# Load Data (fixes your broken URL)

url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv"
covid_df = pd.read_csv(url)


# Helper: Convert date columns to datetime

date_cols = covid_df.columns[11:]  # first 11 columns are metadata
formatted_dates = pd.to_datetime(date_cols)


# VIZ 1 — Utah counties over time
utah_df = covid_df[covid_df['Province_State'] == 'Utah']

plt.figure(figsize=(12, 6))
plt.title("COVID-19 Cases Over Time in Utah Counties")
plt.xlabel("Date")
plt.ylabel("Cumulative Confirmed Cases")

# Plot all counties in grey
for _, row in utah_df.iterrows():
    plt.plot(formatted_dates, row[date_cols], color='lightgrey', linewidth=1)

# Highlight one county
highlight_county = "Salt Lake"
target_row = utah_df[utah_df['Admin2'] == highlight_county].iloc[0]
plt.plot(formatted_dates, target_row[date_cols], color='red', linewidth=3, label=highlight_county)

# Format dates
plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=2))
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))

plt.legend()
plt.tight_layout()
plt.show()


# VIZ 2 — Utah vs Florida: Counties with the most cases

# Find Utah county with most cases
utah_df['latest'] = utah_df[date_cols].iloc[:, -1]
utah_top = utah_df.sort_values("latest", ascending=False).iloc[0]

# Find Florida county with most cases
florida_df = covid_df[covid_df['Province_State'] == 'Florida']
florida_df['latest'] = florida_df[date_cols].iloc[:, -1]
florida_top = florida_df.sort_values("latest", ascending=False).iloc[0]

plt.figure(figsize=(12, 6))
plt.title("COVID-19 Cases: Utah vs Florida Top Counties")
plt.xlabel("Date")
plt.ylabel("Cumulative Confirmed Cases")

# Plot Utah county
plt.plot(formatted_dates, utah_top[date_cols], label=f"Utah — {utah_top['Admin2']} County", color='blue', linewidth=3)

# Plot Florida county
plt.plot(formatted_dates, florida_top[date_cols], label=f"Florida — {florida_top['Admin2']} County", color='green', linewidth=3)

plt.legend()
plt.tight_layout()
plt.show()


# VIZ 3 — One county: Running total + daily new cases (two axes)

county = utah_top  # reuse the Utah top county
cumulative = county[date_cols].values
daily_new = cumulative[1:] - cumulative[:-1]

fig, ax1 = plt.subplots(figsize=(12, 6))

ax1.set_title(f"Cumulative vs Daily New Cases — {county['Admin2']} County, Utah")
ax1.set_xlabel("Date")
ax1.set_ylabel("Cumulative Cases", color='blue')

ax1.plot(formatted_dates, cumulative, color='blue', linewidth=3, label="Cumulative Cases")
ax1.tick_params(axis='y', labelcolor='blue')

# Second axis
ax2 = ax1.twinx()
ax2.set_ylabel("Daily New Cases", color='orange')
ax2.bar(formatted_dates[1:], daily_new, color='orange', alpha=0.6, label="Daily New Cases")
ax2.tick_params(axis='y', labelcolor='orange')

plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=2))
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))

fig.tight_layout()
plt.show()


# VIZ 4 — Stacked Bar Chart: County contributions in a single state

state = "Utah"
state_df = covid_df[covid_df['Province_State'] == state]

# Last date column = total cases to date
state_counts = state_df[date_cols].iloc[:, -1]
counties = state_df['Admin2']

plt.figure(figsize=(2, 6))
plt.title(f"County Contributions to Total COVID-19 Cases in {state}")
plt.xlabel("State")
plt.ylabel("Total Confirmed Cases")

# Stacked bar: one bar for the entire state, slices = counties
bottom = 0
for county, cases in zip(counties, state_counts):
    plt.bar(state, cases, bottom=bottom, label=county)
    bottom += cases

plt.tight_layout()
plt.show()


# In[ ]:




