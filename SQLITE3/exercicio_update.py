
import sqlite3 as sq

banco = sq.connect("dados_loja.db")
cursor = banco.cursor()

# ('Neosaldina', 202507, 'Pharma Brasil Distrib.', '30 comprimidos', 18.90)
cursor.execute("UPDATE produtos SET validade = 282808 WHERE validade = 202507")
banco.commit()
banco.close()

cursor.execute("SELECT * FROM produtos")
print(cursor.fetchall())

