from webScrapeSetup import simple_get
from bs4 import BeautifulSoup
import json


# Enter url of page to be scraped and name of file for data output
webURL = "http://fantasy.nfl.com/research/rankings?offset=101&position=O&sort=average&statType=draftStats"
outputName = "TempScrape.html"

# Do Not Touch
html = BeautifulSoup(simple_get(webURL), 'html.parser')

dataArray = []
# Pick data to be scraped

hold = 1

for td in html.select('.playerNameFull'):
	dataArray.append(td.text)

# # 	if hold == 4:
# # 		dataArray.append(td.text)
# # 		hold = -1
# # 	hold += 1

# print(dataArray)
# print(len(dataArray))



# for x in range(len(test)):
# 	try:
# 		pos = test[x].index(',')
# 	except:
# 		pos = test[x].index(' D/')
# 	test[x] = test[x][:pos]


# print(test)


# for x in html.select("td a"):
#     if hold == 1:
#         dataArray.append(x.text)
#         hold = -2
#     hold += 1





