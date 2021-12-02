"""
Hands-On Lab 14: Intro to Pandas
"""

import pandas as pd

#read data from CSV file
csv_path = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/TopSellingAlbums.csv'
df = pd.read_csv(csv_path)
#Print first 5 rows
df.head()
print(df.head())
#read data from EXCEL file

xlsx_path = r'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%204/Datasets/TopSellingAlbums.xlsx'
df2 = pd.read_excel(xlsx_path)
print(df2.head())
#access the column length as a dataframe
d = df[['Length']]
print(d)
#get the column as a series
e = df['Length']
print(e)
#get the Artist column as a dataframe
g = df[['Artist']]
print(type(g))
#access multiple columns as a dataframe
t = df[['Artist', 'Length', 'Genre']]
print(t)
#access value on the first row and 1st column ILOC
print(df.iloc[0,0])
#access the column using the name LOC
df.loc[1, 'Artist']