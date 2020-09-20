# Surfs Up Analysis
Analysis Using Jupyter Notebooks, Python, Pandas, SQLite, and SQLAlchemy

## Overview of the Surfs Up Weather Data Analysis :surfing_woman:
This project was created for an investor about a surf and icecream shake shop. The analysis is about weather patterns by month for the island of Oahu - more specifically for the months of June and December. Throughout the analysis, we use Jupyter Notebooks and Python to summarize and manipulate data from an SQLite database called hawaii. In order to access this database, we use SQLAlchemy. 

Process of Analysis: create an engine to reflect into the SQLite database and convert the weather data into separate Pandas dataframes for June and December. Then statistical analysis is calculated for each month. This includes count, mean, std, min, 25% + 50% + 75% quartiles, and max for each dataframe. 

## Results 

1. Overall, Oahu doesn't have extreme variations in temperatures. Consistently it is 71-74 degrees between June and December months, noting that the temperature is consistently warm throughout the year. 
2. The lowest recorded temperature is 56 degrees in the month of December. This seems low, but since it does not fall even in the lowest 25% quartile of temperatures, this seems to be a true outlier - further supporting the hypothesis that Oahu weather is consistently warm. 
3. The max temperature recorded for both months is 85 degrees for June and 83 in December. This is also important data that proves Oahu has not only few low temperatures, but it is also not unbearably hot and doesn't reach the 90s or 100s. 

June Weather Results: 
-- insert photo

December Weather Results: 
-- insert photo

## Summary 

Overall, Oahu has an ideal climate year round. While looking at temperature data for the months of June and December, the climate is warm and not too hot or cold. Averaging 73 degrees, it presents a favorable climate for surfing and ice cream. 

### Additional Queries: 

1. In order to get a full picture of the weather, it is important to look at precipitation as well as temperature. When looking at the additional queries run for the temperatures and precipitation, we can see that on average there is a lot more rain during December with the average at 0.22 and the max at 6.42 compared to June with the average at 0.14 and the max at 4.43. 

June Temperatures + Precipitation:
-- insert photo 

December Temperatures + Precipitation: 
-- insert photo 

2. In order to see true yearly temperature, and not just June and December, I ran a query for the last year (2017) for each month. As indicated by the screenshot below, the year round temperature does not vary significantly from June and December temperature. The average yearly temperature is 74 degrees, with the min at 58 degrees and max at 87 degrees. 

-- insert photo


