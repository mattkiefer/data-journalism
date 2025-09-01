# import requests to get data
# and pandas to analyze it
import requests, pandas

# get data from the data portal
# with no row limits
# in text format
data = requests.get('https://data.cityofchicago.org/resource/4njy-buzr.json?$limit=9999999').text 

# load the json string into a pandas dataframe
df = pandas.read_json(data)

# create a new column that converts 
# created date to a year
df['created_year'] = pandas.to_datetime(df['created_date']).dt.year

# aggregate by year
bird_counts = df.groupby('created_year')['sr_number'].count().reset_index(name='count')

# check what you've got
print(bird_counts)

# save to csv for humans 
bird_counts.to_csv('birds.csv',index=False)
# save to json for viz
bird_counts.to_json('birds.json',orient='values')
