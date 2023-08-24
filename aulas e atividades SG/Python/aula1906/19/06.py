#import random
#c = random.randint(1,5)
#nj = int(input("escolha um número:"))
#ej = input("escolha par ou impar:")
#soma = nc+nj
#print("o computador jogou", nc)
#if(soma%2==0):
 #   print("par")
  #  resultado = "par"
#else:
 #   print("impar")
  #  resultado = "impar"
#if(ej == resultado ):
 #   print("deu",resultado,".Você ganhou!")
#else:
 #   print("deu",resultado,".Você perdeu :(")

import random
senha = random.randint(1,10)
for i in range(3):
    t=int(input("informe a senha:"))
    if(senha == t):
        print("voce acertou!")
        break
    else:
        print("voce errou, tente novamente")
print("a senha era", senha)