import psycopg2

conn = psycopg2.connect(dbname ='northwind', user = 'bob', password = 'admin', host = 'localhost')

cursor = conn.cursor()

cursor.execute("SELECT product_name, unit_price,units_in_stock,\n"
	"CASE WHEN units_in_stock >= 100 THEN 'lots of'\n"
		"WHEN units_in_stock >= 50 AND units_in_stock <=100  THEN 'average'\n"
		"WHEN units_in_stock <= 50 THEN 'low number'\n"
		"ELSE 'unknown'\n"
	"END AS amount\n"
"FROM products\n"
"ORDER BY units_in_stock DESC")

print((cursor.fetchone()))
print([x for x in cursor])