import mysql.connector

connection = mysql.connector.connect(
    user='root',
    password='GCruUsgoPnknKFPZLewtKKWftSVPNYtD',
    host='http://interchange.proxy.rlwy.net',
    port= 45565,
    database= 'railway',
    ssl_disabled= True
)
    
    

cursor = connection.cursor()

query = """
      SELECT *
      FROM evaluation
      WHERE evaluation.ranking == 'A';
"""

cursor.execute(query)

results = []
for i, data in enumerate(cursor):
     results.append(data)

cursor.close()
connection.close()

compras_positivas = len(results)