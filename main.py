from Magazin import *
from Tableta import Tableta
from Smartphone import Smartphone
from Laptop import Laptop

connector = MYSQLConnector()
magazin = Magazin(connector)


produs1=Tableta(3, 'tableta', 'ipad', 2019, 2300, 'disponibil', 'restransa')
produs2=Smartphone(2, 'smartphone', 'iphone14', 2022, 4100, 'disponibil', 'albastru')
produs3=Laptop(1, 'laptop', 'macbook', 2020, 4000, 'disponibil', 256)

magazin.addProduct(produs1)
magazin.addProduct(produs2)
magazin.addProduct(produs3)
magazin.printProduct()

magazin.updateProduct(4000, 5000)
magazin.deleteProduct(2500)
print(magazin.vanzare(3))