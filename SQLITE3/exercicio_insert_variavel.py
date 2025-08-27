

import sqlite3 as sq

banco = sq.connect("dados_loja.db")
cursor = banco.cursor()

cursor.execute("CREATE TABLE produtos (marca text, validade integer, fornecedor text, quantidade_comp text, preço integer)")

cursor.execute("INSERT INTO produtos VALUES ('Tylenol', 202609, 'Farmadistribuidora Ltda', '20 comprimidos', 12.50)")
# AAAAAAAAAAAAAAAAAAAAAAAAAAAAA
banco.commit()

cursor.execute("SELECT * FROM produtos")
print(cursor.fetchall())

