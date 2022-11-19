# First Script

import requests
from bs4 import BeautifulSoup

country = input("Enter a Country to search: ")

data = requests.get(r"https://www.worlddata.info/{0}/{0}/index.php".format(country))
soup = BeautifulSoup(data.text, 'html.parser')

print(soup.prettify())