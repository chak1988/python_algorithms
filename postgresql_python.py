from flask import Flask, render_template, request
import psycopg2

app = Flask(__name__)


class MyContextManagerPosgreSQL:

	def __init__(self, db_name, user, password, host = 'localhost'):
		self.db_name = db_name
		self.user = user
		self.password = password
		self.host = host

	def __enter__(self):
		self.connector = psycopg2.connect(dbname = self.db_name, user = self.user, password = self.password,
										  host = self.host)
		cursor = self.connector.cursor()
		return cursor

	def __exit__(self, exc_type, exc_val, exc_tb):
		self.connector.commit()
		self.connector.close()


with MyContextManagerPosgreSQL('northwind', 'bob', 'admin') as cursor:
	cursor.execute("SELECT product_name, unit_price,units_in_stock,\n"
	"CASE WHEN units_in_stock >= 100 THEN 'lots of'\n"
		"WHEN units_in_stock >= 50 AND units_in_stock <=100  THEN 'average'\n"
		"WHEN units_in_stock <= 50 THEN 'low number'\n"
		"ELSE 'unknown'\n"
	"END AS amount\n"
"FROM products\n"
"ORDER BY units_in_stock DESC")


@app.route('/northwind')
def some_info_from_northwind():
	with MyContextManagerPosgreSQL('northwind', 'bob', 'admin') as cursor:
		cursor.execute("SELECT product_name, unit_price,units_in_stock,\n"
					   "CASE WHEN units_in_stock >= 100 THEN 'lots of'\n"
					   "WHEN units_in_stock >= 50 AND units_in_stock <=100  THEN 'average'\n"
					   "WHEN units_in_stock <= 50 THEN 'low number'\n"
					   "ELSE 'unknown'\n"
					   "END AS amount\n"
					   "FROM products\n"
					   "ORDER BY units_in_stock DESC")
		res = list(cursor.fetchall())
		return render_template('page_1.html', data_set = res)

if __name__ == '__main__':
	app.run(debug = True, port = 8000)
# conn = psycopg2.connect(dbname ='northwind', user = 'bob', password = 'admin', host = 'localhost')
#
# cursor = conn.cursor()
#
# cursor.execute("SELECT product_name, unit_price,units_in_stock,\n"
# 	"CASE WHEN units_in_stock >= 100 THEN 'lots of'\n"
# 		"WHEN units_in_stock >= 50 AND units_in_stock <=100  THEN 'average'\n"
# 		"WHEN units_in_stock <= 50 THEN 'low number'\n"
# 		"ELSE 'unknown'\n"
# 	"END AS amount\n"
# "FROM products\n"
# "ORDER BY units_in_stock DESC")
#
# print((cursor.fetchone()))
# print([x for x in cursor])