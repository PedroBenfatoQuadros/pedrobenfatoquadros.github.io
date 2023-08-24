while True:
    menu = int(input("1:cadastro, 2:login, 3:fechar"))
    if(menu == 1):
        print("cadastro")
        nome = input("Informe seu nome:")
        senha = input("informe sua senha:")
        print("Cadastro realizado.")

    elif(menu == 2):
        print("Login")
        t_nome = input("Informe seu nome:")
        t_senha = input("Informe sua senha:")
        if(t_nome == nome and t_senha == senha):
            print("Boas-vindas!")
        else:
            print("login incorreto.")

    elif(menu == 3):
        break
    else:
        
        print("o programa fechará")

print("Fim do programa")