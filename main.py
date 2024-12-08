numero_secreto = 7
tentativas = 3
tentativa_atual = 1

while tentativa_atual <= tentativas:
    palpite = int(input(f"Tentativa {tentativa_atual} de {tentativas}. Qual é o seu palpite? "))

    if palpite == numero_secreto:
        print(f"Parabéns! Você acertou o número {numero_secreto}!")
        break
    elif palpite < numero_secreto:
        print("O número secreto é maior. Tente novamente!")
    else:
        print("O número secreto é menor. Tente novamente!")
 
    tentativa_atual += 1
else:
    print(f"Que pena! Você não acertou o número {numero_secreto}. O jogo acabou.")