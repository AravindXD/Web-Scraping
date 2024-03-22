# Overview
This project aims to fetch recent earthquake data for keeping a machine learning model up to date for predicting earthquakes. 


## Data Collection
To get started with this project, follow these steps:
- Send a GET request to the website.
- Parse the content with BeautifulSoup.
- Find the list items containing the earthquake data.
- Extract relevant data such as place, time, latitude, longitude, magnitude, and depth.
- Store the data in a CSV file (liveearthquakedata.csv).


## Clone the repository
```
$ git clone https://github.com/AravindXD/Web-Scraping
```


### Install the required Python packages: 
```
$ pip install -r requirements.txt
```


## Scraping Earthquake Data

The refresh.py script is used to scrape earthquake data from the website. It extracts data such as place, time, latitude, longitude, magnitude, and depth of earthquakes and stores it in a CSV file [liveearthquakedata.csv](liveearthquakedata.csv). The data is scraped from the [RiseQ Seismo](https://riseq.seismo.gov.in/riseq/earthquake) website primarily using Requests and BeautifulSoup4 Python Library. The extracted CSV file is used for feeding the Machine Learning models' train set.
