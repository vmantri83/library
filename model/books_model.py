import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()
class Books():

    def __init__(self):
        
        try:
            self.conn = mysql.connector.connect(
                host = os.getenv("DBHOST"),
                username =os.getenv("DBUSERNAME") ,
                password = os.getenv("DBPASSWORD"),
                database = os.getenv("DB")
            )
            self.cur = self.conn.cursor(dictionary = True)
            print ("connected successfluuuuu")
        except Exception as e:
            print (f"Could not connect sad {e}")


    def display_books(self):
        self.cur.execute("select * from Transactions")
        res=self.cur.fetchall()
        return res
    
