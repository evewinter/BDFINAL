import sqlite3

connection = sqlite3.connect('Loja.db')
cursor = connection.cursor()

resposta = input("Deseja alterar o e-mail de algum cliente? (s/n): ").strip().lower()

if resposta == 's':
    nome_cliente = input("Digite o nome do cliente cujo e-mail deseja alterar: ").strip()

    cursor.execute('SELECT clientes_id, email FROM Clientes WHERE LOWER(nome) = LOWER(?)', (nome_cliente,))
    cliente = cursor.fetchone()

    if cliente:
        novo_email = input(f"E-mail atual: {cliente[1]}\nDigite o novo e-mail: ").strip()
        cursor.execute('UPDATE Clientes SET email = ? WHERE clientes_id = ?', (novo_email, cliente[0]))
        connection.commit()
        print("E-mail atualizado com sucesso.")
    else:
        print("Cliente não encontrado.")
else:
         print("Ok.")

print("\nOpções de exclusão:")
print("1. Excluir pedido completo")
print("2. Excluir item de um pedido")
opcao = input("Escolha uma opção (1 ou 2): ").strip()

if opcao == '1':
    id_venda = input("Digite o ID do pedido a ser excluído: ").strip()

    # Primeiro exclui os itens relacionados ao pedido
    cursor.execute('DELETE FROM Itenspedidos WHERE compras_finais = ?', (id_venda,))
    # Depois exclui o pedido
    cursor.execute('DELETE FROM Pedidos WHERE id_venda = ?', (id_venda,))
    connection.commit()
    print("Pedido e seus itens foram excluídos com sucesso.")

elif opcao == '2':
    compras_finais = input("Digite o ID do pedido do item: ").strip()
    produto_id = input("Digite o ID do produto a ser removido do pedido: ").strip()

    cursor.execute('''
        DELETE FROM Itenspedidos
        WHERE compras_finais = ? AND produto_id = ?
    ''', (compras_finais, produto_id))
    connection.commit()
    print("Item removido do pedido com sucesso.")

else:
    print("Opção inválida.")

connection.close()
