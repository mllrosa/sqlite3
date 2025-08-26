

# 1- O BANCO QUE CRIAMOS EM SALA DE AULA, É UM BANCO RELATIVO?
import sqlite3 as sq

# 2- CRIE UM BANCO DE DADOS DE UMA loja
banco = sq.connect("dados_loja.db")

cursor = banco.cursor()

# 3- COLOQUE AO MENOS 5 COLUNAS
cursor.execute("CREATE TABLE produtos (marca text, validade integer, fornecedor text, quantidade de comp text, preço integer)")

cursor.execute("INSERT INTO produtos VALUES ('Dell' 2026, 'TechCorp', '100 unidades', 5000)")
cursor.execute("INSERT INTO produtos VALUES ('Lenovo', 2027, 'Global Supply', '50 caixas', 4500)")
cursor.execute("INSERT INTO produtos VALUES ('HP', 2025, 'Prime Distributors', '200 peças', 6000)")

banco.commit()

cursor.execute("SELECT * FROM produtos")
print(cursor.fetchall())