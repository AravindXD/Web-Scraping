import requests
from bs4 import BeautifulSoup
import json
import csv

# URL of the website
url = "https://riseq.seismo.gov.in/riseq/earthquake"

# Send a GET request to the website
response = requests.get(url)

# Parse the content with BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Find the list items with the earthquake data
list_items = soup.find_all('li', {'class': 'list-view-item event_list'})

with open('liveearthquakedata.csv', 'w+', newline='') as file:
    writer = csv.writer(file)
    field = ["Place", "Time", "Latitude","Longitude","Magnitude","Depth"]
    writer.writerow(field)

# Loop through the list items and print the data
for item in list_items:
    # The data-json attribute contains a JSON string with the data we're interested in
    json_data = json.loads(item['data-json'])
    # Extract the data
    place = json_data['event_name']
    time = json_data['origin_time']
    lat= json_data['lat_long'].split(',')[0]
    long = json_data['lat_long'].split(',')[1]
    magnitude = json_data['magnitude_depth'].split(',')[0].split(':')[1].strip()
    depth=json_data['magnitude_depth'].split(',')[1].split(':')[1].strip()
    with open('liveearthquakedata.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([place[9:],time,lat,long,magnitude,depth])
    
    # Print the data
    print(f'''
          Place: {place[9:]}
          Time: {time}
          Latitude: {lat} Longitude: {long}
          Magnitude: {magnitude}
          Depth: {depth}''')
