import sqlite3 as sq

banco = sq.connect("AA2/bloco.db")
cursor = banco.cursor()

# 1. UPDATE – Aumentando salário Em 10%
# cursor.execute("UPDATE funcionarios SET salario = salario * 110")
# banco.commit()
# cursor.execute("SELECT salario FROM funcionarios")
# print(cursor.fetchall())

# 2. UPDATE – Alterando telefone de 15967994960 para (11) 98888-7777
# raiane id 15:
# cursor.execute("UPDATE funcionarios SET telefone = '(11) 98888-7777' WHERE telefone = '(50) 92068-7554' ")
# banco.commit()
# cursor.execute("SELECT telefone FROM funcionarios")
# print(cursor.fetchall())

# 3. UPDATE – Mudança de departamento Ana Athayde foi para o RH
# cursor.execute("UPDATE funcionarios SET departamento ='TI' WHERE id = 1")
# banco.commit()
# cursor.execute("SELECT * FROM funcionarios WHERE pnome = 'Ana' and snome = 'Athayde'")
# print(cursor.fetchall())

# 4. UPDATE – Corrigindo cargo, Um funcionário do cargo Estagiário foi promovido a Analista.
# 👉 Atualize o campo cargo de pelo menos um estagiário para Analista.