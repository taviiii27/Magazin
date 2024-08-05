import mysql.connector
class MYSQLConnector:
    def __init__(self):
        self.mydb=mysql.connector.connect(host='localhost', user='root', password='root', database='electronice')
        self.cursor=self.mydb.cursor() #am initiat cursorul pt a l folosi 
    def selectQueries(self, query, values):
        self.cursor.execute(query,values)
        return self.cursor.fetchall()
    def insertQueries(self,query, values):
        self.cursor.execute(query, values)
        self.mydb.commit()#dam commit ca sa vedem modificarile fct
        return self.cursor.rowcount() #se insereaza pe fecare rand o inreg noua    
    def updateQueries(self, query,values):
        self.cursor.execute(query,values)
        self.mydb.commit() #cu commit modificam diversele chestii pe care le avem in baza de date
    def deletQueries(self, query):
        self.cursor.execute("delete from electronice where pret<{pret}")