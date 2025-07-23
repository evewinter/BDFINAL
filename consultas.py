import sqlite3

connection = sqlite3.connect('Loja.db')
cursor = connection.cursor()

# 1) JOIN entre Pedidos e Clientes usando clientes_id (cliente que fez o pedido)
print("\n1) JOIN entre Pedidos e Clientes usando clientes_id:")
cursor.execute('''
    SELECT Pedidos.id_venda, Pedidos.data, Pedidos.vendedor, Clientes.nome, Clientes.email, Clientes.cidade
    FROM Pedidos
    JOIN Clientes ON Pedidos.clientes_id = Clientes.clientes_id;
''')
for row in cursor.fetchall():
    print(row)

# 2) JOIN entre ItensPedidos, Produtos e Pedidos
print("\n== JOIN entre ItensPedidos, Produtos e Pedidos ==")
cursor.execute('''
    SELECT Produtos.nome_produto, Pedidos.data, Itenspedidos.quantidade
    FROM Itenspedidos
    JOIN Produtos ON Itenspedidos.produto_id = Produtos.produto_id
    JOIN Pedidos ON Itenspedidos.compras_finais = Pedidos.id_venda;
''')
for row in cursor.fetchall():
    print(row)

# 3) WHERE com filtro do pedido por nome do cliente:
nome_cliente = input("\nDigite o nome do cliente para buscar pedidos: ")

cursor.execute('SELECT clientes_id FROM Clientes WHERE LOWER(nome) = LOWER(?)', (nome_cliente,))
cliente = cursor.fetchone()

if cliente is None:
    print(f"Cliente '{nome_cliente}' não encontrado.")
else:
    clientes_id = cliente[0]
    cursor.execute('''
        SELECT Pedidos.id_venda, Pedidos.data, Pedidos.vendedor
        FROM Pedidos
        WHERE clientes_id = ?
    ''', (clientes_id,))
    resultados = cursor.fetchall()
    if resultados:
        for row in resultados:
            print(row)
    else:
        print(f"Nenhum pedido encontrado para o cliente '{nome_cliente}'.")

# 4) WHERE com filtro do pedido por data 
data_filtrada = input("\nDigite a data desejada (AAAA-MM-DD): ")
cursor.execute('''
    SELECT * FROM Pedidos
    WHERE data = ?
''', (data_filtrada,))
for row in cursor.fetchall():
    print(row)

# 5) LIKE com nome do produto 
nome_parcial = input("\nDigite parte do nome do produto: ")
cursor.execute('''
    SELECT * FROM Produtos
    WHERE nome_produto LIKE ?
''', ('%' + nome_parcial + '%',))
for row in cursor.fetchall():
    print(row)

# 6) LIMIT para mostrar apenas os 5 primeiros produtos 
print("\n== Mostrando apenas os 5 primeiros produtos cadastrados ==")
cursor.execute('''
    SELECT * FROM Produtos
    LIMIT 5
''')
for row in cursor.fetchall():
    print(row)

connection.close()