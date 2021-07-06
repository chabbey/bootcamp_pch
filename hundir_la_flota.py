# %%
import numpy as np

# GRID HUMANO
def grid():

    grid_blank_human = np.full((10, 10), ' ')

    grid_blank_bot = np.full((10, 10), ' ')

    grid_human = np.full((10, 10), ' ')

    grid_bot = np.full((10, 10), ' ')

    boat_size = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]

    N, S, E, W = [1, 2, 3, 4]

    for i in boat_size:

        initial_coordenate = np.random.randint(0, 10, size=2)

        orient = np.random.randint(1, 4, size=1)

        if orient == N and (
                grid_human[initial_coordenate[0] - i:initial_coordenate[0], initial_coordenate[1]] == ' ').all() and \
                initial_coordenate[0] - i >= 0:

            grid_human[initial_coordenate[0] - i:initial_coordenate[0], initial_coordenate[1]] = 'A'


        elif orient == S and (
                grid_human[initial_coordenate[0]:initial_coordenate[0] + i, initial_coordenate[1]] == ' ').all() and \
                initial_coordenate[0] + i < 10:

            grid_human[initial_coordenate[0]:initial_coordenate[0] + i, initial_coordenate[1]] = 'A'


        elif orient == W and (
                grid_human[initial_coordenate[0], initial_coordenate[1] - i:initial_coordenate[1]] == ' ').all() and \
                initial_coordenate[1] - i >= 0:

            grid_human[initial_coordenate[0], initial_coordenate[1] - i:initial_coordenate[1]] = 'A'


        elif orient == E and (
                grid_human[initial_coordenate[0], initial_coordenate[1]:initial_coordenate[1] + i] == ' ').all() and \
                initial_coordenate[1] + i < 10:

            grid_human[initial_coordenate[0], initial_coordenate[1]:initial_coordenate[1] + i] = 'A'

        else:
            boat_size.append(i)

# GRID BOT

    boat_size_bot = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]

    for i in boat_size_bot:

        initial_coordenate = np.random.randint(0, 10, size=2)

        orient = np.random.randint(1, 4, size=1)

        if orient == N and (
                grid_bot[initial_coordenate[0] - i:initial_coordenate[0], initial_coordenate[1]] == ' ').all() and \
                initial_coordenate[0] - i >= 0:

            grid_bot[initial_coordenate[0] - i:initial_coordenate[0], initial_coordenate[1]] = 'A'


        elif orient == S and (
                grid_bot[initial_coordenate[0]:initial_coordenate[0] + i, initial_coordenate[1]] == ' ').all() and \
                initial_coordenate[0] + i < 10:

            grid_bot[initial_coordenate[0]:initial_coordenate[0] + i, initial_coordenate[1]] = 'A'


        elif orient == W and (
                grid_bot[initial_coordenate[0], initial_coordenate[1] - i:initial_coordenate[1]] == ' ').all() and \
                initial_coordenate[1] - i >= 0:

            grid_bot[initial_coordenate[0], initial_coordenate[1] - i:initial_coordenate[1]] = 'A'


        elif orient == E and (
                grid_bot[initial_coordenate[0], initial_coordenate[1]:initial_coordenate[1] + i] == ' ').all() and \
                initial_coordenate[1] + i < 10:

            grid_bot[initial_coordenate[0], initial_coordenate[1]:initial_coordenate[1] + i] = 'A'

        else:
            boat_size_bot.append(i)

    return grid_human,grid_bot

     

grid_human,grid_bot=grid()



grid_blank_human = np.full((10, 10), ' ')

grid_blank_bot = np.full((10, 10), ' ')
print(' ')
print('<-----BARCOS COLOCADOS EN EL TABLERO----->')
print(grid_human)#Barcos del usuario
print(' ')

            

# DISPARO HUMANO

def shoot():

    
    human_lifes = 2
    bot_lifes = 2

    while human_lifes != 0 and bot_lifes != 0:

        try:
            coordenate_1 = int(input('Introduce la primera coordenada (las filas, del 0 al 9):  '))
            coordenate_2 = int(input('Introduce la segunda coordenada (las columnas, del 0 al 9):  '))

        except ValueError:

            pass

        print(' ')
        shoot_human = grid_bot[coordenate_1, coordenate_2]

        if shoot_human == 'A':
            grid_bot[coordenate_1, coordenate_2] = 'X'
            grid_blank_human[coordenate_1, coordenate_2] = 'X'
            bot_lifes -= 1

            print('Bingo! Has acertado')
            print('<---------------TUS DISPAROS--------------->')
            print(grid_blank_human)
            continue

        elif shoot_human != 'A':

            grid_bot[coordenate_1, coordenate_2] = '-'
            grid_blank_human[coordenate_1, coordenate_2] = '-'

            print('Agua! Has fallado')
            print('<---------------TUS DISPAROS--------------->')
            print(grid_blank_human)
            print("Aciertos para ganar: ", bot_lifes)
            print(' ')
        
    
        
        
    
# DISPARO BOT
    
        bot_coordenates = np.random.randint(0, 9, size=2)

        shoot_bot = grid_human[bot_coordenates[0], bot_coordenates[1]]

        if shoot_bot == 'A':
            grid_human[bot_coordenates[0], bot_coordenates[1]] = 'X'
            grid_blank_bot[bot_coordenates[0], bot_coordenates[1]] = 'X'
            human_lifes -= 1
            print('Bingo! El bot ha acertado')
            print('<---------------TUS BARCOS----------------->')
            print(grid_human)
            continue

        elif shoot_bot != 'A':

            grid_human[bot_coordenates[0], bot_coordenates[1]] = '-'
            grid_blank_bot[bot_coordenates[0], bot_coordenates[1]] = '-'
            print('Agua! El bot ha fallado')
            print('<---------------TUS BARCOS----------------->')
            print(grid_human)
            print("Aciertos del bot para perder: ", human_lifes)

        
    if bot_lifes <= 0:
            print("Has ganado, felicidades")
    
    elif human_lifes <= 0:
        print("El bot te ha ganado, lo siento")
    

       

        

        """print(' ')
        print('<---------------TUS DISPAROS--------------->')
        print(grid_blank_human)
        print('                                        ')
        print('<---------------TUS BARCOS----------------->')
        print(grid_human)"""
     


    # if human_lifes <= 0:
    #     print("El bot te ha ganado, lo siento")

    # elif bot_lifes <= 0:
    #     print("Has ganado, felicidades")

    
shoot()












# %%
