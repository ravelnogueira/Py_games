import lasvegas_game
import forca_game

asteristicos = "*****************************"
print(asteristicos)
print("Escolha seu jogo")
print(asteristicos)

i = 1 > 0
while (i > 0):
    escolha = int(input("Escolha o jogo. (1)Las Vegas (2)Forca:"))

    if (escolha == 1):
        lasvegas_game.jogar_las_vegas()
        break
    if (escolha == 2):
        forca_game.jogar_forca()
        break
