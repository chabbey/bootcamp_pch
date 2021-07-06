#Funciones
#%%
#Grid creation 

import numpy as np 

def grid(x,y):

    grid = np.full((x, y), ' ')

    boat_size = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]

    N, S, E, W = [1, 2, 3, 4]

    for i in boat_size:

        initial_coordenate = np.random.randint(0, 10, size=2)

        orient = np.random.randint(1, 4, size=1)

        if orient == N and (
                grid[initial_coordenate[0] - i:initial_coordenate[0], initial_coordenate[1]] == ' ').all() and \
                initial_coordenate[0] - i >= 0:

            grid[initial_coordenate[0] - i:initial_coordenate[0], initial_coordenate[1]] = 'Z'


        elif orient == S and (
                grid[initial_coordenate[0]:initial_coordenate[0] + i, initial_coordenate[1]] == ' ').all() and \
                initial_coordenate[0] + i < 10:

            grid[initial_coordenate[0]:initial_coordenate[0] + i, initial_coordenate[1]] = 'Z'


        elif orient == W and (
                grid[initial_coordenate[0], initial_coordenate[1] - i:initial_coordenate[1]] == ' ').all() and \
                initial_coordenate[1] - i >= 0:

            grid[initial_coordenate[0], initial_coordenate[1] - i:initial_coordenate[1]] = 'Z'


        elif orient == E and (
                grid[initial_coordenate[0], initial_coordenate[1]:initial_coordenate[1] + i] == ' ').all() and \
                initial_coordenate[1] + i < 10:

            grid[initial_coordenate[0], initial_coordenate[1]:initial_coordenate[1] + i] = 'Z'

        else:
            boat_size.append(i)
        
    return grid

def shoot_manual(grid_bot,grid_blank_human,bot_lifes):


    coordenate_1 = int(input('Introduce la primera coordenada (las filas, del 0 al 9):  '))
    coordenate_2 = int(input('Introduce la segunda coordenada (las columnas, del 0 al 9):  '))

    
    print(' ')
    shoot_human = grid_bot[coordenate_1, coordenate_2]

    if shoot_human == 'Z':
        grid_bot[coordenate_1, coordenate_2] = 'X'
        grid_blank_human[coordenate_1, coordenate_2] = 'X'
        bot_lifes -= 1
       
        print('Bingo! Has acertado')
        print('<---------------TUS DISPAROS--------------->')
        print(grid_blank_human)
        

    elif shoot_human != 'Z':

        grid_bot[coordenate_1, coordenate_2] = '-'
        grid_blank_human[coordenate_1, coordenate_2] = '-'
    
        print('Agua! Has fallado')
        print('<---------------TUS DISPAROS--------------->')
        print(grid_blank_human)
        print("Aciertos para ganar: ", bot_lifes)
        print(' ')

    return bot_lifes,coordenate_1,coordenate_2

def shoot_random(grid_human,human_lifes):


    bot_coordenates = np.random.randint(0, 9, size=2)

    shoot_bot = grid_human[bot_coordenates[0], bot_coordenates[1]]

    if shoot_bot == 'Z':
        grid_human[bot_coordenates[0], bot_coordenates[1]] = 'X'
        human_lifes -= 1 
        print('Bingo! El bot ha acertado')
        print('<---------------TUS BARCOS----------------->')
        print(grid_human)
        

    elif shoot_bot != 'Z':

        grid_human[bot_coordenates[0], bot_coordenates[1]] = '-'
        print('Agua! El bot ha fallado')
        print('<---------------TUS BARCOS----------------->')
        print(grid_human)
        print("Aciertos del bot para perder: ", human_lifes)
    return human_lifes,bot_coordenates

def grid_blank(x,y):

    grid = np.full((x, y), ' ')

    return grid


#%%

grid_human = grid(11,11)
grid_bot = grid(11,11)
grid_blank_human = grid_blank(11,11)
bot_lifes =2
human_lifes =2

while human_lifes != 0 and bot_lifes != 0:

    try:

        bot_lifes,coordenate_1, coordenate_2= shoot_manual(grid_bot,grid_blank_human,bot_lifes)
        if grid_bot[coordenate_1, coordenate_2] == 'X':
            continue

    except ValueError:

        pass

    human_lifes,bot_coordenates = shoot_random(grid_human,human_lifes)
    if grid_human[bot_coordenates[0], bot_coordenates[1]] == 'X':
            continue

    if bot_lifes <= 0:
            print("Has ganado, felicidades")
    
    elif human_lifes <= 0:
        print("El bot te ha ganado, lo siento")


# %%
