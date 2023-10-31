from fastapi import APIRouter
import requests
from bs4 import BeautifulSoup
from os import getenv

router = APIRouter(
    prefix="/bcv"
)


@router.get("")
def get():
    URL = getenv("URL")
    response = requests.get(URL, timeout=100)
    
    hashMap = {
        "dollar": {
            "currency": "VES/BS",
            "paralelo": 0,
            "official": 0
        },

    }

    soup = BeautifulSoup(response.content, 'html5lib')
    els = soup.find_all("div", {
        "class": "border-2 rounded-lg shadow p-2 text-center overflow-hidden"
    })
    print(soup)
    return {
        "status": 200,
        "data": hashMap
    }
