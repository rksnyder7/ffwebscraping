from webScrapeSetup import simple_get
from bs4 import BeautifulSoup


# Enter url of page to be scraped and name of file for data output
webURL = "https://www.fantasypros.com/nfl/rankings/dst-cheatsheets.php"
outputName = "TempScrape.html"

# Do Not Touch
html = BeautifulSoup(simple_get(webURL), 'html.parser')
# outputSite = open(outputName, 'w')

dataArray = []
# Pick data to be scraped
hold = 0


# for td in html.find_all('td'):
#     print(td.text)
for x in html.select(".full-name"):
    dataArray.append(x.text)



print(dataArray)
print(len(dataArray))

# for tr in html.select('tr'):
#     hold = 0
#     for td in tr:
#         if hold == 5:
#             dataArray.append(td.text)
#             break
#         hold += 1

# dataArray = dataArray[1:]
# # print(dataArray)

# finalArray = []


# for x in range(len(dataArray)):
#     hold = dataArray[x].index(',')
#     finalArray.append(dataArray[x][hold+2:] + ' ' + dataArray[x][:hold])

# print(finalArray)
# print(len(finalArray))


# for td in html.select('td.tbdy1'):
#     dataArray.append(td.text)

# print(len(dataArray))
# print(dataArray)

    # dataArray.append(td.text)
    # hold = 0
    # for td in tr:
        # if hold == 3:
        # dataArray.append(td)
            # break
        # hold += 1  
    # outputSite.write(p.text)
# hold = 0
# for x in range(len(dataArray)):
#     hold = dataArray[x].index(' ')
    # dataArray[x] = dataArray[x][hold + 1:]
# dataArray = dataArray[1:]
# # for x in range(228,248):
# #     holdArray.append(dataArray[x])

# for x in range(len(dataArray)):
#     hold = dataArray[x].index(' ')
#     dataArray[x] = dataArray[x][hold + 1:]
# print(dataArray)
# print(len(dataArray))

#Do Not Touch
# outputSite.close()
