import sqlite3

connection = sqlite3.connect('Loja.db')
cursor = connection.cursor()
cursor.execute('PRAGMA foreign_keys = ON;')

# 1) Tratando erro ao inserir cliente com nome NULL
try:
    cursor.execute('INSERT INTO Clientes (nome, email, telefone) VALUES (?, ?, ?)', 
                   (None, 'semnome@email.com', '0000-0000'))
    connection.commit()
except sqlite3.IntegrityError as e:
    print("Erro de integridade ao inserir cliente:", e)

# 2) Tratando erro ao registrar venda com cliente_id inexistente
try:
    cursor.execute('INSERT INTO Pedidos (data, vendedor, clientes_id) VALUES (?, ?, ?)', 
                   ('2025-07-23', 'Vendedor Fantasma', 9999))  # cliente_id 9999 não existe por exemplo
    connection.commit()
except sqlite3.IntegrityError:
    print("Falha: Cliente não encontrado para registrar a venda.")

# 3) Tratando erro de digitação no SQL (OperationalError)
try:
    cursor.execute('UPDAT Clientes SET email = "erro@email.com" WHERE clientes_id = 1')
except sqlite3.OperationalError as e:
    print("Erro de operação SQL:", e)

connection.close()
