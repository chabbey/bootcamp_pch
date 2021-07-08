def shoot_manual(grid_bot, grid_blank_human, bot_lifes):
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
        print(' ')
        print('<---------------TUS DISPAROS--------------->')
        print(grid_blank_human)
        print(' ')
        print("Aciertos para ganar: ", bot_lifes)
        print(' ')

    return bot_lifes, coordenate_1, coordenate_2