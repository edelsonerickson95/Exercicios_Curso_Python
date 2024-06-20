'''
90. Exercício - crie uma lista de compras com listas'''
'''
Exercício
Fça uma lista de compras com listas
O usuário deve ter a possibilidade de inserir, apagar, e listar os valores da
sua lista
Não permita que o programa quebre com  erros de índices inexistente na lista.
'''
import os 

lista_de_compras = []
print('Lista de compras supermercado\n')


while True:
    print('Escolha uma opção\n')
    opção_escolhida =  input(
        'digite [ 1 ] para adicionar item à lista.\n'
        'digite [ 2 ] para ver a lista de compras.\n'
        'digite [ 3 ] para remover o item da lista.\n'
        )
    

    if opção_escolhida == '1':
        os.system('cls')
        item = input('Digite o nome do item para ser adiconado a lista: ')

        if item in lista_de_compras:
            print('Você já colocou este produto')
            continue

        lista_de_compras.append(item)
        

    elif opção_escolhida =='2':
        os.system('cls')
        print('Sua lista de compras')
        for nunmero, produto in enumerate(lista_de_compras, start=1):
            print(nunmero, produto)

    elif opção_escolhida == '3' and lista_de_compras == []:
        os.system('cls')
        print('Sua lista está vazia nesse momento. Não há nada a remover')

    elif opção_escolhida == '3':
        os.system('cls')

        print('Sua lista de compras')
        for nunmero, produto in enumerate(lista_de_compras, start=1):
            print(nunmero, produto)

        remover_item = input('digite o numero do produto que deseja remover: ')
        
        try:
            indince_a_remover = int(remover_item) - 1
            lista_de_compras.pop(indince_a_remover)

            if lista_de_compras == []:
                print('Sua lista está vazia nesse momento')


        except ValueError:
            os.system('cls')
            print('por favor, digite apenas numeros')

        except IndexError:
            os.system('cls')
            print('Não existe produro nesse número')

        except Exception:
            print("Erro desconhecido")
    else:
        os.system('cls')
        print('Por favor, escolha uma opção válida')

