"""
Program: suppliers.py
Author: Bobby Parsons

Contains classes that handle scraping supplier websites in order to get information about the provided part numbers
"""
from bs4 import BeautifulSoup
import urllib.request
from abc import ABC, abstractmethod

class ItemNotFoundException(Exception):
    pass

class supplier_item(ABC):
    @abstractmethod
    def __init__(self):
        self._url = None
        self._name = None
        self._price = None

    def get_url(self):
        return self._url

    def get_price(self):
        return self._price

    def get_name(self):
        return self._name

class andymark_item(supplier_item):
    def __init__(self, partnumber):
        self._url = 'https://www.andymark.com/'+ partnumber
        try:
            r = urllib.request.urlopen(self._url).read()
            soup = BeautifulSoup(r, 'html.parser')
            
            self._name = soup.title.get_text()[:-15] # trim supplier name

            prices = soup.find_all('p', {'class' : 'product-prices__price'}) #get all prices on the page
            stripped_price_str = prices[0].text.strip('\n $') #strips all but the actual price
            self._price = float(stripped_price_str)
        except:
            raise ItemNotFoundException


class rev_item(supplier_item):
    def __init__(self, partnumber):
        self._url = 'https://www.revrobotics.com/'+ partnumber
        try:
            r = urllib.request.urlopen(self._url).read()
            soup = BeautifulSoup(r, "html.parser")
            
            self._name = soup.title.get_text()[:-15] # trim supplier name

            prices = soup.find_all("span", {"class" : "price"}) #get all prices on the page
            stripped_price_str = prices[0].text.strip("$") #strips all but the actual price
            self._price = float(stripped_price_str)
        except:
            raise ItemNotFoundException
    