import requests
from bs4 import BeautifulSoup, Tag, NavigableString
from os import getenv
from src.helpers.fn import static_response_error


class BcvService:
    @staticmethod
    def values():
        URL = getenv("URL")
        response = requests.get(URL, timeout=100)
        if response.status_code != 200:
            return None, True

        hashMap = {
        }

        soup = BeautifulSoup(response.content, 'html5lib')
        containerElement: Tag | NavigableString | None = soup.find("div", {
            "class": "views-row views-row-1 views-row-odd views-row-first views-row-last row"
        })
        if containerElement is None:
            return None, True

        containerValuesElement: list[Tag | NavigableString | None] = containerElement.find_all("div", {
            "class": "row recuadrotsmc"
        })
        if len(containerValuesElement) == 0:
            return None, True

        for i1, containerValue in enumerate(containerValuesElement):
            v1 = containerValue.find_next('div', {
                "class": "col-sm-6 col-xs-6"
            })
            v2 = containerValue.find_next('div', {
                "class": "col-sm-6 col-xs-6 centrado"
            })
            v1_lower = v1.text.strip().lower()
            hashMap[v1_lower] = {}
            hashMap[v1_lower]['official'] = float(v2.text.strip().replace(',', '.'))

        return hashMap, None
