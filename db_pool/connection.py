from mysql import connector

connect=connector.connect(
    user='root', 
    password='2005',
    host='localhost',
    database='management_db'
    
)


    
cursor=connect.cursor()