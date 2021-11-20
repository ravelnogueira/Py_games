import random
def jogar_las_vegas():
    #Introdução do jogo


    asteristicos = "*****************************"
    print(asteristicos)
    print("Sejam bem vindos a Las Vegas")
    print(asteristicos)

    #Parte 1: Valor do chute, e número de tentativas

    secreto = random.randrange(1,21)
    tentativas_total = 3

    #parte 2: Selecionando dificuldade

    i = 1>0
    while (i > 0):
        level = int(input("Defina a dificuldade. (1)Fácil (2)Médio (3)Dificil:"))

        if(level ==1):
            tentativas_total = 10
            break
        if(level ==2):
            tentativas_total = 5
            break
        if(level ==3):
            tentativas_total = 3
            break


    #Parte 3: Lógica do game
    for rodada in range(1,tentativas_total+1):
        print("Você possui {0} Tentativas. Tentativa {1} de {0}".format(tentativas_total, rodada))
        Chute = input("Insira um número de 1 a 20:")
        chuteINT = int(Chute)


        acertou = secreto == chuteINT
        maior = chuteINT>secreto
        menor =chuteINT<secreto

        if(acertou):
            print("Você acertou")
            rodada = rodada - 1
            break

        else:
            if(maior):
                print("Seu chute foi maior que o número")

            elif(menor):
                print("Seu chute foi menor que o número")

    #Parte 4: Lógica do encerramento do Game
    game_over = rodada >= tentativas_total
    if(game_over):
        print("GAME OVER, VOCÊ FALIU")
        print("O número correto era", secreto)
    else:
        print("PARABÉNS, VOCÊ FICOU MILIONÁRIO")

    print(asteristicos)
    print("FIM DE JOGO")
    print(asteristicos)