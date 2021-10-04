#Work on converting html to json and dumping to a json file

import requests
from bs4 import BeautifulSoup
from datetime import datetime
import json
import xmltojson

URL = 'https://www.eventhubs.com/tiers/tekken7/'
page = requests.get(URL)
file_path = 'C:\\Users\\green\\Desktop\\WorkSpaces\\Python\\EventHubs\\'
test_file = 'TierList_Tekken7'
file_fmt = '.html' #.txt
soup = BeautifulSoup(page.content, 'html.parser')

time_format = '%Y-%m-%d %I:%M %p'
timestamp_format = '%m%d%Y%H%M%S'
current_date = datetime.now()

results = soup.find(id='tiers1')
r1 = str(results)
#print(results.prettify())

time_content = current_date.strftime(time_format)

#json_ = xmltojson.parse(results)

#For Testing
#Add error checking for: finding file, opening and closing file, error in writing to a file, file not found, special character found issue, URL not reachable or found (HTTP codes)
print('Printed results to file: ',file_path + test_file + file_fmt)
with open(file_path + test_file + current_date.strftime(timestamp_format) + file_fmt, 'w') as fl:
    #sys.stdout = fl
    #print(URL)
    #print('Last ran timestamp: ',current_date.strftime(time_format))
    print('Scraper results:')
    print(results.prettify())
    fl.write(r1)
