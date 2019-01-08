from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://stockx.com/sneakers'

uClient = uReq(my_url)
page_html = uClient.read()

filename = "instaScrape.csv"
f = open(filename,"w")
headers = "Account Name, Tweets, Followers, Following\n"
f.write(headers)

uClient.close()

page_soup = soup(page_html, "html.parser")
containers = page_soup.findAll('div', attrs={'class': 'browse-grid'})
print(containers)
for container in containers:
    print(container)

#FPmhX notranslate _0imsa

f.close()
