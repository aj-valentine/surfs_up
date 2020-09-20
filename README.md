# Surfs Up Analysis
Analysis Using Jupyter Notebooks, Python, Pandas, SQLite, and SQLAlchemy

## Overview of the Surfs Up Weather Data Analysis :surfing_woman:
This project was created for an investor about a surf and icecream shop. The analysis details weather patterns by month for the island of Oahu - more specifically for the months of June and December. Throughout the analysis, I have used Jupyter Notebooks and Python to summarize and manipulate data from an SQLite database called hawaii. In order to access this database, SQLAlchemy was used. 

Process of Analysis: create an engine to reflect into the SQLite database and convert the weather data into separate Pandas dataframes for June and December. Then statistical analysis is calculated for each month. This includes count, mean, std, min, 25% + 50% + 75% quartiles, and max for each dataframe. 

## Results 

1. Overall, Oahu doesn't have extreme variations in temperatures. Consistently it is 71-74 degrees between June and December months, noting that the temperature is consistently warm throughout the year. 
2. The lowest recorded temperature is 56 degrees in the month of December. This seems low, but since it does not fall even in the lowest 25% quartile of temperatures, this seems to be a true outlier - further supporting the hypothesis that Oahu weather is consistently warm. 
3. The max temperature recorded for both months is 85 degrees for June and 83 in December. This is also important data that proves Oahu has not only few low temperatures, but it is also not unbearably hot and doesn't reach the 90s or 100s. 

June Weather Results: 

<img width="128" alt="June_Weather" src="https://user-images.githubusercontent.com/67871338/93692623-7d8a3e00-fac3-11ea-9ecb-159e5505d1b1.PNG">

December Weather Results: 

<img width="114" alt="Dec_Weather" src="https://user-images.githubusercontent.com/67871338/93692618-719e7c00-fac3-11ea-8f7a-33734c17be36.PNG">

## Summary 

Overall, Oahu has an ideal climate year round. While looking at temperature data for the months of June and December, the climate is warm and not too hot or cold. Averaging 73 degrees, it presents a favorable climate for surfing and ice cream. 

### Additional Queries: 

1. In order to get a full picture of the weather, it is important to look at precipitation as well as temperature. When looking at the additional queries run for the temperatures and precipitation, we can see that on average there is a lot more rain during December with the average at 0.22 and the max at 6.42 compared to June with the average at 0.14 and the max at 4.43. 

June Temperatures + Precipitation:

<img width="170" alt="June_Weather_withprcp" src="https://user-images.githubusercontent.com/67871338/93692625-7fec9800-fac3-11ea-9a00-2fda02261df9.PNG">

December Temperatures + Precipitation: 

<img width="179" alt="Dec_Weather_withprcp" src="https://user-images.githubusercontent.com/67871338/93692621-76fbc680-fac3-11ea-99a5-91d631bb4fed.PNG">

2. In order to see true yearly temperature, and not just June and December, I ran a query for the last year (2017) for each month. As indicated by the screenshot below, the year round temperature does not vary significantly from June and December temperature. The average yearly temperature is 74 degrees, with the min at 58 degrees and max at 87 degrees. 

2017 Yearly Temperature: 

<img width="113" alt="2017_Year" src="https://user-images.githubusercontent.com/67871338/93692638-af9ba000-fac3-11ea-8064-afe5e247d3fc.PNG">


