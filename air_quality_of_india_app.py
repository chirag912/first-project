# -*- coding: utf-8 -*-
"""Air quality of India.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sBlgTZLLJO-AJZqoSPYDLLVtc0KjSEcR
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import geopandas as gpd
import geoplot

df = pd.read_csv("city_day.csv")

df.head()

df['Date'] = pd.to_datetime(df['Date'],format='%Y-%m-%d') # date parse
df['year'] = df['Date'].dt.year # year
df['year'] = df['year'].fillna(df["year"].min())
df['year'] = df['year'].values.astype(int)

print(df.dtypes.value_counts())

def printNullValues(df):
    total = df.isnull().sum().sort_values(ascending = False)
    total = total[df.isnull().sum().sort_values(ascending = False) != 0]
    percent = total / len(df) * 100
    percent = percent[df.isnull().sum().sort_values(ascending = False) != 0]
    concat = pd.concat([total, percent], axis=1, keys=['Total','Percent'])
    print (concat)
    print ( "-------------")

printNullValues(df)

print(df.columns)

df["AQI_Bucket"].value_counts()

sns.catplot(x = "AQI_Bucket", kind = "count",  data = df, height=5, aspect = 4)

grp = df.groupby(["AQI_Bucket"]).mean()["SO2"].to_frame()
grp.plot.bar(figsize = (20,10), color={"red"})

grp = df.groupby(["AQI_Bucket"]).mean()["NO2"].to_frame()
grp.plot.bar(figsize = (20,10), color={"green"})

df[['SO2', 'City']].groupby(['City']).median().sort_values("SO2", ascending = False).plot.bar(figsize=(20,10))

df[['SO2','year','City']].groupby(["year"]).median().sort_values(by='year',ascending=False).plot(figsize=(20,10))

df[['NO2', 'City']].groupby(['City']).median().sort_values("NO2", ascending = False).plot.bar(figsize=(20,10))

df[['NO2','year','City']].groupby(["year"]).median().sort_values(by='year',ascending=False).plot(figsize=(20,10))

df[['Toluene', 'City']].groupby(['City']).median().sort_values("Toluene", ascending = False).plot.bar(figsize=(20,10))

df[['Toluene','year','City']].groupby(["year"]).median().sort_values(by='year',ascending=False).plot(figsize=(20,10))

fig, ax = plt.subplots(figsize=(20,10))
sns.heatmap(df.pivot_table('SO2', index='City',columns=['year'],aggfunc='median',margins=True),ax = ax,annot=True, linewidths=.5)

fig, ax = plt.subplots(figsize=(20,10))
sns.heatmap(df.pivot_table('NO2', index='City',columns=['year'],aggfunc='median',margins=True),ax = ax,annot=True, linewidths=.5)

fig, ax = plt.subplots(figsize=(20,10))
sns.heatmap(df.pivot_table('Toluene', index='City',columns=['year'],aggfunc='median',margins=True),ax = ax,annot=False, linewidths=.5)

temp = df.pivot_table('SO2', index='year',columns=['City'],aggfunc='median',margins=True).reset_index()
temp = temp.drop("All", axis = 1)
temp = temp.set_index("year")
temp.plot(figsize=(20,10))

temp = df.pivot_table('NO2', index='year',columns=['City'],aggfunc='median',margins=True).reset_index()
temp = temp.drop("All", axis = 1)
temp = temp.set_index("year")
temp.plot(figsize=(20,10))

temp = df.pivot_table('Toluene', index='year',columns=['City'],aggfunc='median',margins=True).reset_index()
temp = temp.drop("All", axis = 1)
temp = temp.set_index("year")
temp.plot(figsize=(20,10))

