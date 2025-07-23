import sqlite3

connection = sqlite3.connect('Loja.db')
cursor = connection.cursor()

cursor.execute('DROP TABLE IF EXISTS Itenspedidos;')
cursor.execute('DROP TABLE IF EXISTS Pedidos;')
cursor.execute('DROP TABLE IF EXISTS Produtos;')
cursor.execute('DROP TABLE IF EXISTS Clientes;')

cursor.execute('''
    CREATE TABLE Clientes (
        clientes_id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL, 
        email TEXT,          
        cidade TEXT,
        telefone INTEGER
    );
''')

cursor.execute('''
    CREATE TABLE Produtos (
        produto_id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome_produto TEXT NOT NULL,
        preco NUMERIC(4, 2) NOT NULL,
        categoria TEXT
    );
''')

cursor.execute('''
    CREATE TABLE Pedidos (
        id_venda INTEGER PRIMARY KEY AUTOINCREMENT,
        data DATE NOT NULL,
        vendedor TEXT NOT NULL,
        produto_comprado INTEGER,
        clientes_id INTERGER,
        FOREIGN KEY (clientes_id) REFERENCES Clientes(clientes_id),
        FOREIGN KEY (produto_comprado) REFERENCES Produtos(produto_id)
    );
''')

cursor.execute('''
    CREATE TABLE Itenspedidos (
        id_compra INTEGER PRIMARY KEY AUTOINCREMENT,
        quantidade INTEGER NOT NULL,
        valor_unitario INTEGER,
        compras_finais INTEGER NOT NULL,
        produto_id INTEGER NOT NULL,
        FOREIGN KEY (compras_finais) REFERENCES Pedidos(id_venda),
        FOREIGN KEY (produto_id) REFERENCES Produtos(produto_id)
    );
''')

connection.commit()
connection.close()