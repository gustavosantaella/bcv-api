import easyocr
from bs4 import BeautifulSoup
from requests import get
from os import getenv
from database import sqllite


class MonitorDolarService:

    page_name = 'dolar-today'
    
    @staticmethod
    def check_price_of_dolar(need_update = False):
        if need_update == True:
            print("Üpdating price of dollar")
            
        cur = sqllite.con.cursor().execute(
            "SELECT * FROM dollar_values WHERE page_name='dolar-today'")
        response1 = get(getenv("DOLAR_TODAY_URL"), timeout=100)
        data = cur.fetchone()
        print(data)
        cur.close()
        paralelo = ""
        if data == None or need_update == True:            
            soup = BeautifulSoup(response1.content, 'html5lib')

            img = soup.find("img", {
                "id": "wp-horizontal-image-home"
            })

            src = img.get("src")
            response = get(src, timeout=100)

            reader = easyocr.Reader(['en'])
            result: list = reader.readtext(response.content, detail=0)

            i = 0
            for i, item in enumerate(result):
                if 'paralelo' in item:
                    break

                i += 1

            paralelo :str= result[i + 3]
            paralelo = paralelo.strip().split('.')[1]
            paralelo = paralelo.replace(",", '.')
            
            if need_update == True and data[1] != paralelo:
                print("price has been updated")
                cur = sqllite.con.cursor().execute("UPDATE dollar_values SET value = ? WHERE page_name = ?", [paralelo, MonitorDolarService.page_name])
                cur.close()
            else:
                cur = sqllite.con.cursor().execute("INSERT INTO dollar_values (value, page, page_name) VALUES (?, ?, ?)", [paralelo, response1.url, MonitorDolarService.page_name])
                cur.close()
            
            sqllite.con.commit()
        else:
            print("price has been taken from memory")
            paralelo = data[1]
        
        
        return float(paralelo), None
