import mysql.connector
class MYSQLConnector:
    def __init__(self):
        self.mydb=mysql.connector.connect(host='localhost', user='root', password='root', database='electronice')
        self.cursor=self.mydb.cursor() #am initiat cursorul pt a l folosi 
    def selectQueries(self, query, values=None):
        self.cursor.execute(query,values)
        return self.cursor.fetchall()
    def insertQueries(self,query, values):
        self.cursor.execute(query, values)
        self.mydb.commit()#dam commit ca sa vedem modificarile fct
        return self.cursor.rowcount #se insereaza pe fecare rand o inreg noua    
    def updateQueries(self, query,values):
        self.cursor.execute(query,values)
        self.mydb.commit() #cu commit modificam diversele chestii pe care le avem in baza de date
    def deleteQueries(self, query, values):
        self.cursor.execute(query, values)
        self.mydb.commit()
class Produs:
    def __init__(self, id, produs, tip, an, pret, stoc):
        self.id=id
        self.produs=produs
        self.tip=tip
        self.an=an
        self.stoc=stoc
        self.pret=pret
class Magazin:
    def __init__(self, connector):
        self.connector=connector
    def addProduct(self, product):
        query="""
        INSERT INTO electronice.electronice (`id`, `produs`, `tip`, `an`, `pret`, `stoc`)
        VALUES (%s, %s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
        produs = VALUES(produs),
        tip = VALUES(tip),
        an = VALUES(an),
        pret = VALUES(pret),
        stoc = VALUES(stoc)
    """
        values=(product.id, product.produs, product.tip, product.an, product.pret, product.stoc)
        self.connector.insertQueries(query,values)

    def printProduct(self):
        query="SELECT * FROM electronice"
        product=self.connector.selectQueries(query,())
        for produs in product:
            print(produs)
    
    def updateProduct(self, pret_nou, pret_vechi):
        query="UPDATE electronice SET pret=%s WHERE pret>%s"
        variables=(pret_nou, pret_vechi)
        self.connector.updateQueries(query, variables)

    def deleteProduct(self, pret_dat):
        query="DELETE FROM electronice WHERE pret<%s"
        variable=(pret_dat,)
        self.connector.deleteQueries(query, variable)

    def vanzare(self, id_produs):
        query="SELECT * FROM electronice WHERE id=%s"
        values=(id_produs,)
        params = self.connector.selectQueries(query, values)
        if params: #este alcatuit din interogare, valori obtinute
            produs=params[0]#id=produs este primul in lista de electronice
            if produs[5]=='disponibil':
                if produs[4]>4000:
                    return f'pentru produsul {produs[1]} exista cativa clienti interesati'
                else:
                    return f'pentru produsul {produs[1]} exista numerosi clienti'
            else:
                return f'stocul pentru {produs[1]} tb reumplut'
        else:
            return f'produsul nu exista'
    