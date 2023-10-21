import requests
from bs4 import BeautifulSoup
from time import sleep
from fastapi import FastAPI
from dotenv import load_dotenv
from os import getenv
load_dotenv()

app = FastAPI()

@app.get("/api/bcv")
def bcv():
    URL = getenv("URL")
    response = requests.get(URL)
    if response.status_code != 200:
        return {
            "status": 400,
            "message": "An error ocurred. You can report this with a issue in https://github.com/gustavosantaella/bcv-api.git"
        }
    hashMap = {
        "dollar": {
            "currency": "VES/BS",
            "paralelo": 0,
            "bcv": 0
        },
        "euro": {
            "currency": "VES/BS",
            "paralelo": 0,
            "bcv": 0
        },
        "petro": {
            "currency": "VES/BS",
            "compra": 0,
            "venta": 0
        }
    }

    soup = BeautifulSoup(response.content, 'html5lib')
    els: list = soup.findAll('span', attrs={
        "class": "light"
    })

    for i, el in enumerate(els):
        if i == 0 or i == len(els):
            continue

        if i == 1:
            hashMap["petro"]['compra'] = el.text.split()[1]

        if i == 2:
            hashMap["petro"]['venta'] = el.text.split()[1]

        if i == 3:
            hashMap["dollar"]['bcv'] = el.text.split()[1]
        
        if i == 4:
            hashMap["euro"]['bcv'] = el.text.split()[1]
            
    print(hashMap)
    return {
        "status": 200,
        "data": hashMap
    }


    
