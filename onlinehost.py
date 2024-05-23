import psycopg2
from psycopg2 import sql

hostname='SG-horn-vase-6540-5373-pgsql-master.servers.mongodirector.com'
database='checkup'
username='sgpostgres'
pwd='cg@G2qt8fahc2Iso'
port_id='5432'


# cnx = psycopg2.connect(host="SG-neat-dream-3695-5372-pgsql-master.servers.mongodirector.com" 
#                        user="<user>" password="<password>" dbname="<your-database-name>" port=5432)

try:

    conn = psycopg2.connect(
        host = hostname,
        dbname = database,
        user = username,
        password = pwd,
        port = port_id
)
    
    cur = conn.cursor()


   

    insert_script = 'INSERT INTO client_id (id) VALUES(%s)'
    insert_values = [('1234'),('8736'),('3623'),('9831'),('13571')]
    for record in insert_values:
        cur.execute(insert_script, (record,))



   


    # cur.execute(f"""
    #        DELETE FROM public.credentials_data
    #     """)



    conn.commit()
    conn.close()

except Exception as error:
    print(error)
