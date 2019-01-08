from urllib.request import urlopen , Request
from bs4 import BeautifulSoup as soup

my_url = 'https://stockx.com/sneakers'

headerz = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '
                      'AppleWebKit/537.11 (KHTML, like Gecko) '
                      'Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive'}

req = Request(url=my_url, headers=headerz)

page_html = urlopen(req).read()

filename = "shoeScrape.csv"
f = open(filename,"w")
headers = "Account Name, Tweets, Followers, Following\n"
f.write(headers)


page_soup = soup(page_html, "html.parser")
containers = page_soup.findAll('a', attrs={'class': 'tile browse-tile'})


for container in containers:
    foo = container.find('div', attrs={'class': 'name'})
    print(foo.text)
    print()



f.close()
