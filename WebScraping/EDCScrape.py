from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import re

my_url = 'https://www.edc.ca/en/country-info.html'

uClient = uReq(my_url)
page_html = uClient.read()

filename = "edcData.csv"
f = open(filename,"w+")
headers = "Country, EDC-Position, Risk-Rating\n"
f.write(headers)


uClient.close()

soup = soup(page_html, "html.parser")

country = []
position = []
riskRating = []


data_box = soup.findAll('li', attrs={'class': 'country'})

pos_box = soup.findAll('span', attrs={'class': 'mobile-value'})

for x in range(0,len(pos_box)):
	p = pos_box[x].text.strip()
	if (x % 2) == 0:
		position.append(p)
	else:
		riskRating.append(p)
	#p = x.get('data-position')

	'''r = x.get('data-rating')
	position.append(p)
	riskRating.append(r)'''

country_box = soup.findAll('h3', attrs={'class': 'country-name'})

for x in country_box:
	a = x.a.text.split()
	a = ''.join(a)
	a = re.sub('([A-Z])', r' \1', a)
	country.append(a)

for x in range(0,len(position)):
	try:
		f.write(country[x] + "," + position[x] + "," + riskRating[x] + "\n")
	except TypeError:
		f.write(country[x] + "," + "No Information" + "," + "No Information" + "\n")

f.close()
