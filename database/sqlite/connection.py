from sqlite3 import Connection, connect, Cursor
from os import getenv
from dotenv import load_dotenv
load_dotenv()
class SQLLiteConnection:
    con: Connection
    
    def __init__(self):
        self.con = connect(getenv("DB_SQLITE"), check_same_thread=False)
        print("Connection susccessfully")
        self.__create_tables()

    
    def __create_tables(self):
        try:
            self.con.cursor().execute("""
                                  CREATE TABLE IF NOT EXISTS dollar_values(
                                      id integer not null primary key AUTOINCREMENT,
                                      value text not null,
                                      page text null,
                                      page_name text null
                                  )
                                  """)
            self.con.commit()
        except Exception as e:
            print("Error to create tables", e)
            raise e
        
        
connection = SQLLiteConnection()