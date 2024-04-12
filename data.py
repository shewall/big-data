import pandas as pd
import csv

data_distance=pd.read_csv("Trips_by_Distance.csv")
data_full=pd.read_csv("Trips_Full_Data.csv")



data_distance.dropna(inplace=True)
data_full.dropna(inplace=True)

data_distance.drop_duplicates(inplace=True)
data_full.drop_duplicates(inplace=True)


data_full = data_full[['Month of Date', 'Week of Date', 'Year of Date', 'Level', 'Date', 'Week Ending Date', 'Trips <1 Mile', 'People Not Staying at Home', 'Population Staying at Home', 'Trips', 'Trips 1-25 Miles', 'Trips 1-3 Miles', 'Trips 10-25 Miles', 'Trips 100-250 Miles', 'Trips 100+ Miles', 'Trips 25-100 Miles', 'Trips 25-50 Miles', 'Trips 250-500 Miles', 'Trips 3-5 Miles', 'Trips 5-10 Miles', 'Trips 50-100 Miles', 'Trips 500+ Miles']]
data_distance = data_distance[['Level', 'Date', 'State FIPS', 'State Postal Code', 'County FIPS', 'County Name', 'Population Staying at Home', 'Population Not Staying at Home', 'Number of Trips', 'Number of Trips <1', 'Number of Trips 1-3', 'Number of Trips 3-5', 'Number of Trips 5-10', 'Number of Trips 10-25', 'Number of Trips 25-50', 'Number of Trips 50-100', 'Number of Trips 100-250', 'Number of Trips 250-500', 'Number of Trips >=500', 'Row ID', 'Week', 'Month']]


data_full['Date'] = pd.to_datetime(data_full['Date'])
data_full['Week Ending Date'] = pd.to_datetime(data_full['Date'])

data_full['Month of Date'] = data_full['Date'].dt.month
data_full['Year of Date'] = data_full['Date'].dt.year

data_distance['Date'] = pd.to_datetime(data_distance['Date'])

data_distance['Month of Date'] = data_distance['Date'].dt.month
data_distance['Year'] = data_distance['Date'].dt.year




data_full.to_csv("Processed_Trips_Full_Data.csv", index=False)
data_distance.to_csv("Processed_Trips_by_Distance.csv", index=False)




data =pd.concat([data_full, data_distance])



