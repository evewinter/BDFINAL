import sqlite3
from datetime import datetime

connection = sqlite3.connect('Loja.db')
cursor = connection.cursor()

Clientes = [
    ("Maria", "maria@email.com", "Fortaleza", "934675239"),
    ("João", "joao@email.com", "Juazeiro do Norte", "909786543"),
    ("Marta", "marta@email.com", "Crato", "987654323"),
    ("Pedro", "pedro@email.com", "Sobral", "934567890"),
    ("Ana", "ana@email.com", "Maracanaú", "912345678"),
    ("Carlos", "carlos@email.com", "Caucaia", "988765432"),
    ("Fernanda", "fernanda@email.com", "Iguatu", "923456789"),
    ("Bruno", "bruno@email.com", "Quixadá", "919876543"),
    ("Juliana", "juliana@email.com", "Russas", "935678901"),
    ("Lucas", "lucas@email.com", "Canindé", "918273645"),
    ("Patrícia", "patricia@email.com", "Crateús", "927364182"),
    ("Rafael", "rafael@email.com", "Tianguá", "901928374"),
    ("Camila", "camila@email.com", "Aracati", "936281745"),
    ("Gustavo", "gustavo@email.com", "Pacajus", "902345671"),
    ("Larissa", "larissa@email.com", "Limoeiro do Norte", "948291736"),
    ("Felipe", "felipe@email.com", "Horizonte", "917263849"),
    ("Aline", "aline@email.com", "Acopiara", "903948576"),
    ("Tiago", "tiago@email.com", "Icó", "905678342"),
    ("Vanessa", "vanessa@email.com", "Morada Nova", "937182645"),
    ("Rodrigo", "rodrigo@email.com", "Barbalha", "946271839"),
    ("Beatriz", "beatriz@email.com", "Itapipoca", "901736281"),
    ("Eduardo", "eduardo@email.com", "Aquiraz", "910273645"),
    ("Tatiane", "tatiane@email.com", "Eusébio", "929384756"),
    ("André", "andre@email.com", "Camocim", "915738291"),
    ("Débora", "debora@email.com", "Baturité", "944556678"),
    ("Marcelo", "marcelo@email.com", "Trairi", "913849203"),
    ("Natália", "natalia@email.com", "Maranguape", "918273940"),
    ("Wesley", "wesley@email.com", "Granja", "936284756"),
    ("Sabrina", "sabrina@email.com", "Pentecoste", "901827364"),
    ("Igor", "igor@email.com", "Redenção", "908172635")
]

Produtos = [
    ("Microfone", "50", "Som"),
    ("Violão", "700", "Música"),
    ("Guitarra", "1000", "Música"),
    ("Teclado", "850", "Música"),
    ("Bateria", "2500", "Música"),
    ("Caixa de Som", "300", "Som"),
    ("Fone de Ouvido", "120", "Som"),
    ("Amplificador", "900", "Som"),
    ("Cabo P10", "40", "Acessórios"),
    ("Pedal de Guitarra", "250", "Acessórios"),
    ("Palheta", "5", "Acessórios"),
    ("Suporte para Microfone", "80", "Acessórios"),
    ("Violino", "1500", "Música"),
    ("Cavaquinho", "450", "Música"),
    ("Ukulele", "300", "Música"),
    ("Mesa de Som", "1300", "Som"),
    ("Equalizador", "600", "Som"),
    ("Metronomo", "90", "Acessórios"),
    ("Afinador", "70", "Acessórios"),
    ("Encordoamento Violão", "35", "Acessórios"),
    ("Encordoamento Guitarra", "45", "Acessórios"),
    ("Case para Violão", "200", "Acessórios"),
    ("Case para Guitarra", "220", "Acessórios"),
    ("Estante de Partitura", "110", "Acessórios"),
    ("Banqueta para Música", "180", "Acessórios"),
    ("Adaptador P2/P10", "25", "Acessórios"),
    ("Cabo XLR", "55", "Acessórios"),
    ("Filtro Pop", "60", "Acessórios"),
    ("Gravador Portátil", "750", "Som"),
    ("Interface de Áudio", "1100", "Som")
]

cursor.executemany('''
    INSERT INTO Clientes (nome, email, cidade, telefone)
    VALUES (?, ?, ?, ?);
''', Clientes)

cursor.executemany('''
    INSERT INTO Produtos (nome_produto, preco, categoria)
    VALUES (?, ?, ?);
''', Produtos)

resposta = input("Deseja adicionar mais clientes? (s/n): ").lower()
while resposta == "s":
    nome = input("Nome: ")
    email = input("Email: ")
    cidade = input("Cidade: ")
    telefone = input("Telefone: ")
    cursor.execute('INSERT INTO Clientes (nome, email, cidade, telefone) VALUES (?, ?, ?, ?);',
                   (nome, email, cidade, telefone))
    resposta = input("Deseja adicionar outro cliente? (s/n): ").lower()

resposta = input("Deseja adicionar mais produtos? (s/n): ").lower()
while resposta == "s":
    nome_produto = input("Nome do Produto: ")
    preco = float(input("Preço: "))
    categoria = input("Categoria: ")
    cursor.execute('INSERT INTO Produtos (nome_produto, preco, categoria) VALUES (?, ?, ?);',
                   (nome_produto, preco, categoria))
    resposta = input("Deseja adicionar outro produto? (s/n): ").lower()

pedidos = []
itenspedidos = []

print("\nCadastro de 10 pedidos:")
for i in range(1, 11):
    print(f"\nPedido {i}:")
    data = input("Data do pedido (AAAA-MM-DD): ")
    vendedor = input("Nome do vendedor: ")
    cliente_id = int(input("ID do cliente (confira na tabela Clientes): "))

    cursor.execute('''
        INSERT INTO Pedidos (data, vendedor, produto_comprado, clientes_id)
        VALUES (?, ?, NULL, ?);
    ''', (data, vendedor, cliente_id))
    
    pedido_id = cursor.lastrowid

    qtd_itens = int(input("Quantos itens neste pedido? "))
    for j in range(qtd_itens):
        print(f"  Item {j+1}:")
        produto_id = int(input("  ID do produto: "))
        quantidade = int(input("  Quantidade: "))
        valor_unitario = float(input("  Valor unitário: "))
        itenspedidos.append((pedido_id, produto_id, quantidade, valor_unitario))

cursor.executemany('''
    INSERT INTO Itenspedidos (compras_finais, produto_id, quantidade, valor_unitario)
    VALUES (?, ?, ?, ?);
''', itenspedidos)

connection.commit()
connection.close()