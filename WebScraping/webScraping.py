from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.newegg.ca/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20cards'

uClient = uReq(my_url)
page_html = uClient.read()

filename = "products.csv"
f = open(filename,"w")
headers = "brand, product_name, shipping_cost\n"
f.write(headers) 


uClient.close()

page_soup = soup(page_html, "html.parser")

containers = page_soup.findAll("div",{"class":"item-container"})
brands = []
names = []
shipping_costs = []
for container in containers:

	brand = container.div.div.a.img["title"]
	brands.append(brand)

	title_container = container.findAll("a",{"class":"item-title"})
	name = title_container[0].text.replace(",","|")
	names.append(name)

	shipping_container = container.findAll("li",{"class":"price-ship"})
	shipping = shipping_container[0].text.strip()
	shipping_costs.append(shipping)
	f.write(brand + "," + name + "," + shipping + "\n")

f.close()