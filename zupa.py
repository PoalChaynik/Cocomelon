from bs4 import BeautifulSoup as bs
import requests
 
def apstrada_lapu(url):
    r = requests.get(url)
    html = r.text
    soup = bs(html, 'html.parser')
    return soup
 
html = apstrada_lapu("https://www.tvnet.lv")
print(html.head.title.text)

def virsraksts(site):
    result = requests.get(site)
    resultHtml=result.text
    zupa=bs(resultHtml, 'html.parser')
    return zupa

eKlaseTitle = virsraksts('https://my.e-klase.lv/Family/Diary')
print(eKlaseTitle.head.title.text)


result = requests.get('https://www.tvnet.lv')
resultHtml=result.text
sup=bs(resultHtml, 'html.parser')
print("\nVisi virsraksti lapai TVNET: ")
for title in sup.find_all('title'):
    print(title.get_text())
