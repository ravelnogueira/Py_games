import random
import lasvegas_game
def jogar_forca():
    #Introdução do jogo


    asteristicos = "*****************************"
    print(asteristicos)
    print("Sejam bem vindos a Forca")
    print(asteristicos)


if(__name__ == "__main__"):
    jogar_forca()

    palavra_secreta1 = input("Entre com a palavra secreta").strip()
    letras = len(palavra_secreta1)
    erros = 0
    lista = ["_"for letras in palavra_secreta1]
    enforcou = erros >=6
    contagem = 6 - erros
    print(lista)



    while (not enforcou):
        print("Jogando...")
        print("restam", contagem, "tentativas")
        chute = input("Qual é a palavra com {} letras".format(letras))
        index = 0
        for letra in palavra_secreta1:

            if(chute==letra):
                lista[index] = letra




            index += + 1







        print(lista)



