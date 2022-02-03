from bs4 import BeautifulSoup
import requests
import re

url = 'https://www.google.com'
url_EL = 'https://www.gasbuddy.com/station/195230'
url_COM = 'https://www.gasbuddy.com/station/24786'

# Types of gas: Regular and Premium
# Site also displays prices at other gas stations
# I can add some logic(conditionals) to find whether Costco is cheapest and by how much
# download info from gasbuddy's website 
# I want to know the gas prices at two locations
# I want to be able to get both gas prices from the two locations
# scrape through with beautiful soup
# I want to be able to do this on my phone through a website I make

# I get a response by issuing this request
response = requests.get(url_EL, headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1'}) 
soup = BeautifulSoup(response.text,"html.parser")
#print(soup.prettify())
#print(type(soup.prettify()))

""" 
Top line creates text file, last two lines captures 
response.text and converts input as the file response.txt

f = open("myfile.txt", "w") # this creates a text file
with open('response.txt', 'w') as x:
    x.write(response.text)
"""
location = soup.find("title")
price = soup.find_all("span", class_="FuelTypePriceDisplay-module__price___3iizb")
type = soup.find_all("span", class_= "GasPriceCollection-module__fuelTypeDisplay___eE6tM")

span = soup.find("span", class_="FuelTypePriceDisplay-module__price___3iizb") # only finds the first gas price


print(location.text)
for i in range(len(price)):
    print(type[i].text,price[i].text)

#print(location.text)
#print(type[0].text,price[0].text)
#print(type[1].text,price[1].text)


#pattern = re.compile(".\d.\d\d")
#print(pattern.search())


# Price: >$\d.\d\d< - $ int . int int
# Type: >\l\l\l\l\l\l\l< - 7 alpha
