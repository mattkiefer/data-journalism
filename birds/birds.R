# load required libraries
library(httr)
library(jsonlite)
library(dplyr)
library(lubridate)

# get data from the data portal
data <- GET("https://data.cityofchicago.org/resource/4njy-buzr.json?$limit=9999999")

# parse JSON content into a dataframe
df <- fromJSON(content(data, "text"))

# create a new column with year from created_date
df$created_year <- year(ymd_hms(df$created_date))

# aggregate by year
bird_counts <- df %>%
  group_by(created_year) %>%
  summarise(count = n())

# check what you've got
print(bird_counts)

# array of arrays for Plot
array_output <- unname(split(as.matrix(bird_counts), row(bird_counts)))


# save to csv for humans
write.csv(array_output, "birds.csv", row.names = FALSE)

# save to json for viz
write_json(bird_counts, "birds.json")
