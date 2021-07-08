def shoot_random(grid_human, human_lifes):
    bot_coordenates = np.random.randint(0, 9, size=2)

    shoot_bot = grid_human[bot_coordenates[0], bot_coordenates[1]]

    if shoot_bot == 'Z':
        grid_human[bot_coordenates[0], bot_coordenates[1]] = 'X'
        human_lifes -= 1
        print(' ')
        print('Bingo! El bot ha acertado')
        print(' ')
        print('<---------------TUS BARCOS----------------->')
        print(grid_human)


    elif shoot_bot != 'Z':

        grid_human[bot_coordenates[0], bot_coordenates[1]] = '-'
        print('Agua! El bot ha fallado')
        print(' ')
        print('<---------------TUS BARCOS----------------->')
        print(grid_human)
        print(' ')
    print("Aciertos del bot para perder: ", human_lifes)
    print(' ')
    return human_lifes, bot_coordenates