def grid(x, y):
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