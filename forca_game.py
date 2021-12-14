import random
import lasvegas_game

def jogar_forca():
    #Introdução do jogo
    print("*****************************")
    print("Sejam bem vindos a Forca")
    print("*****************************")

    # Seleção e exibição da palavra secreta
    palavra_secreta = input("Entre com a palavra secreta").strip()
    tamanho = len(palavra_secreta)
    lista = ["_"for letras in palavra_secreta]
    print(lista)

    # Configuração de rodadas
    if(tamanho <= 6):
        tentativas = 3
    elif(tamanho > 6 and tamanho <= 10):
        tentativas = 6
    else:
        tentativas = 10

    # Motor principal
    print("Escolha {0} letras".format(tentativas))
    for rodada in range (1, tentativas+1):
        chute = input("letra {0} de {1}".format(rodada,tentativas))

        index = 0
        for letra in palavra_secreta:
            if(chute==letra):
                lista[index] = letra
            index = index + 1

        print(lista)

    # Final
    momento = input("Qual é palavra?")
    if(momento == palavra_secreta):
        print("Você ganhou")
    else:
        print("você perdeu")


if(__name__ == "__main__"):
    jogar_forca()


