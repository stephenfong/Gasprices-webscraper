from bs4 import BeautifulSoup
import requests

# Types of gas: Regular and Premium
# Site also displays prices at other gas stations
# I can add some logic(conditionals) to find whether Costco is cheapest and by how much
# download info from gasbuddy's website 
# I want to know the gas prices at two locations
# I want to be able to get both gas prices from the two locations
# scrape through with beautiful soup
# I want to be able to do this on my phone through a website I make

urllist = ['https://www.gasbuddy.com/station/195230','https://www.gasbuddy.com/station/24786']

for i in urllist:
    response = requests.get(i, headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1'}) 

    soup = BeautifulSoup(response.text,"html.parser")

    location = soup.find("title")
    price = soup.find_all("span", class_="FuelTypePriceDisplay-module__price___3iizb")
    type = soup.find_all("span", class_= "GasPriceCollection-module__fuelTypeDisplay___eE6tM")
    break # ends the for loop here
    print(location.text)
    for i in range(len(price)):
        print(type[i].text,price[i].text)
    print("-------------")


def gas_scraper(urllist): # With the input of list of urls from gasbuddy

    for i in urllist:
        response = requests.get(i, headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1'}) 

        soup = BeautifulSoup(response.text,"html.parser")

        location = soup.find("title")
        price = soup.find_all("span", class_="FuelTypePriceDisplay-module__price___3iizb")
        type = soup.find_all("span", class_= "GasPriceCollection-module__fuelTypeDisplay___eE6tM")

        print(location.text)
        for i in range(len(price)):
            print(type[i].text,price[i].text)
        print("-------------")
 
list = ['https://www.gasbuddy.com/station/202941']
gas_scraper(urllist)
