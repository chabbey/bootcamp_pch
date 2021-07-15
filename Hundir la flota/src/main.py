import numpy as np
from funcion_tablero import grid
from funcion_tablero_vacio import grid_blank
from funcion_tiro_manual import shoot_manual
from funcion_tiro_random import shoot_random



#Bienvenida del juego e instrucciones 

print('  \n ')

print('BIENVENIDO A HUNDIR LA FLOTA, DISFRUTE DE SU EXPERIENCIA. \n \n Instrucciones: Cada jugador tiene asociado dos'
      ' tableros, \n uno con tus barcos distribuidos de forma aleatoria donde \n se ven los disparos realizados'
      ' por el rival, y otro tablero \n donde se ven tus disparos. Una vez los tableros están distribuidos,'
      ' \n procedemos a empezar con los disparos, si el disparo logra dar en un \n barco, repetiremos. Si por el'
      ' contrario el disparo da en agua, será \n el turno de disparar de nuestro rival. El juego concluye'
      ' cuando uno \n de los jugadores se queda sin barcos en el tablero')

#Creación de los tableros y colocación de los barcos de manera aleatoria

grid_human = grid(11, 11)
grid_bot = grid(11, 11)
grid_blank_human = grid_blank(11, 11)
bot_lifes = 20
human_lifes = 20

print(' ')
print('<------------------Tus Barcos----------------->')
print(grid_human)
print(' ')
print('<-----------------Tus Disparos---------------->')
print(grid_blank_human)

#Interacción de los disparos de los jugadores hasta la finalización de la partida

while human_lifes != 0 and bot_lifes != 0:

    try:

        bot_lifes, coordenate_1, coordenate_2 = shoot_manual(grid_bot, grid_blank_human, bot_lifes)
        if grid_bot[coordenate_1, coordenate_2] == 'X':
            continue

    except ValueError:
        print(' ')
        print('No has introducido las coordenadas correctamente, \nNo has aprovechado tu turno, lo siento.')
        print(' ')
        pass

    human_lifes, bot_coordenates = shoot_random(grid_human, human_lifes)
    if grid_human[bot_coordenates[0], bot_coordenates[1]] == 'X':
        continue

    if bot_lifes == 0:
        print("Has ganado, felicidades")

    elif human_lifes == 0:
        print("El bot te ha ganado, lo siento")