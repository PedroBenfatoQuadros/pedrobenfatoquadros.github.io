lista = []
while true:
    x = int(input('''
    1-adicionar um item
    2-remover item 
    3-visualizar lista
    4-sair                        
'''))
    if(x == 1):
        item = input('qual item quer adicionar?')
        list.append(item)
    elif(x == 2):
        print('')
    elif(x == 3):
        print(f'lista completa: (lista)')
    elif(x == 4):
        print('')
    else:
        print('opção invalida')