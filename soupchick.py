import requests
from bs4 import BeautifulSoup
url = requests.get('https://www.inbox.lv/')
soup = BeautifulSoup(url.text, 'html.parser')

# print(soup)
# print(soup.prettify)

# print(list(soup.children))
# print([type(item) for item in list(soup.children)])

html =list(soup.children)[2]
# print(list(html.children))

body = list(html.children)[3]
# print(body)

div = list(body.children)[1]
# print(list(div.children))

p = list(div.find_all('p'))
# print(p)
# print(p[0].get_text(),p[1].get_text())


# Super Viegla Metode Kā tikt tie "p"
print(soup.find_all('p')[1].get_text())