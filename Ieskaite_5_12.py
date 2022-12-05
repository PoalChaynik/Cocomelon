class Gig():
    def __init__(self):
        pass

from cryptography.fernet import Fernet

key = Fernet.generate_key()

a = Fernet(key)

teksts = b'Ieskaites laiks'

shifretsTeksts = a.encrypt(teksts)
print(shifretsTeksts)

atshifretsTeksts = a.decrypt(shifretsTeksts)
print(atshifretsTeksts)

from flask import Flask
from flask_cors import CORS
from datetime import datetime
import json

app = Flask(__name__)
app.config["JSON_AS_ASCII"]=False
CORS(app)

@app.route('/')
def index():
    return 'darbojas!'

@app.route('/datums')
def datums():
    laiks = datetime.now()
    return f'<h1>{str(laiks)[0:19]}<h1/>'

@app.route('/sutit/<vards>/<garastavoklis>')
def sutit(vards,garastavoklis):
    rinda = {
            'vards':vards,
            'garastavoklis':garastavoklis
        }

    with open('sutit.json','r',encoding='utf-8') as fails:
        vecasZinas = fails.read()
        vecieJson = json.loads(vecasZinas)

    vecieJson.append(rinda)

    with open('sutit.json','w',encoding='utf-8') as f:
        json.dump(vecieJson,f,indent=2,ensure_ascii=False)

    return 'ok'

@app.route('/lasitDatus')
def read():
    with open('sutit.json','r',encoding='utf-8') as r:
        msg = r.read()
    return msg

# app.run(host='0.0.0.0',port=81)


from bs4 import BeautifulSoup
import requests

url = requests.get('https://vvsprogramm.github.io/2021_debug/')

soup = BeautifulSoup(url.text,'html.parser')
print(soup.prettify())

url = requests.get('https://data.gov.lv/lv')

soup = BeautifulSoup(url.text, 'html.parser')
# print(soup)
print(soup.find_all("div", {"class": "datacat"})[4].get_text())