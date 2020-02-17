### TEST DE CONEXION A LA BASE DE DATOS ###

import pyodbc
#libreria que ayuda a la conexion con la base de datos

#server = 'sqlbit.database.windows.net'
#database = 'db_bit'
#username = 'azureuser'
#password = 'Bitpass123'
#conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+"sqlbit.database.windows.net"+';DATABASE='+"db_bit"+';UID='+"azureuser"+';PWD='+ "Bitpass123")
db = conn.cursor()

#Como hacer un query
db.execute("select * from db_bit.dbo.arrendador")
for row in db:
    print(row)
