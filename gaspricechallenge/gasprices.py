#!/usr/bin/env python3

import requests
import csv, json, sys

print("Accessing Daily Gas Price API")
#======Loading API responce============================================================
response = requests.get('http://api.eia.gov/series/?api_key=a96c9f12609754e047275c901636aed6&series_id=NG.RNGWHHD.D')
if response.status_code != 200: #checks if json was properly downloaded
	print("Promblem retreiving data from API, status code: "+response.status_code)
#=======intializing variables==========================================================
jsondata = json.loads(response.text)
series = jsondata['series']	#choosing the 'series' dictionary from the available data
for t in series: #loading details of the series
#====== Creating Data Details List ====================================================
	if 'data' in t: #checks if there is any data in the response
		csvdata = t['data'] #pulling the data out of the series
	else: # no relevant data was found
		print("No data found")

print("Creating Daily Price CSV File")

# field names  
fields = ['  Date ' '  Price ']  
    
# name of csv file  
filename = "daily_gas_prices_1.csv"

#writing to csv file  
with open(filename, 'w') as csvfile:  
#  creating a csv writer object  
    csvwriter = csv.writer(csvfile)  
    csvwriter.writerow(fields)     
    csvwriter.writerows(csvdata)

print("CSV File Creation Complete")
      