import mysql.connector

class Books():

    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host = "localhost",
                username = "root",
                password = "1234",
                database = "library"
            )
            self.cur = self.conn.cursor(dictionary = True)
            print ("connected successfluuuuu")
        except Exception as e:
            print (f"Could not connect sad {e}")


    def display_books(self):
        self.cur.execute("select * from Transactions")
        res=self.cur.fetchall()
        return res
    
