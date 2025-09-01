import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# connect to db
conn = sqlite3.connect('db.sqlite3')

# modify or create new queries as needed
query = "select * from stops where AgencyName = 'CHICAGO POLICE' and year = 2024"

# load exec'd query into df
df = pd.read_sql_query(query,conn)

# show
print(df)

# Group by beat and count stops
beat_counts = df['BeatLocationOfStop'].value_counts()

# Show the beat with the most stops
print("Most active beat:", beat_counts.idxmax())


# Count stops by driver race
race_counts = df['driver_race'].value_counts()

# Show racial breakdown
print("Racial breakdown of stops:")
print(race_counts)

# Plot pie chart of driver race with default settings
df['driver_race'].value_counts().plot.pie()


# Convert stop date to datetime
df['DateOfStop'] = pd.to_datetime(df['DateOfStop'])

# Count stops per month and plot
df['DateOfStop'].dt.to_period('M').value_counts().sort_index().plot(kind='bar')


