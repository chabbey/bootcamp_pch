
# %%
import numpy as np 

grid_human          = np.full((10,10),' ') 
grid_bot            = np.full((10,10),' ') 
boat_size           = [4,3,3,2,2,2,1,1,1,1]
N,S,E,W         	= [1,2,3,4]

# GRID HUMANO

for i in boat_size:

    initial_coordenate         = np.random.randint(0,10,size=2)

    orient      = np.random.randint(1,4,size=1)

    if orient   == N and (grid_human[initial_coordenate [0]-i:initial_coordenate [0],initial_coordenate [1]]   == ' ').all() and initial_coordenate [0]-i >= 0    :

        grid_human[initial_coordenate [0]-i:initial_coordenate [0],initial_coordenate [1]] = 'A'
        

    elif orient == S and (grid_human[initial_coordenate [0]:initial_coordenate [0]+i,initial_coordenate [1]] == ' ').all()  and initial_coordenate [0]+i < 10     :

        grid_human[initial_coordenate [0]:initial_coordenate [0]+i,initial_coordenate [1]] = 'A'
        

    elif orient == W and (grid_human[initial_coordenate [0],initial_coordenate [1]-i:initial_coordenate [1]] == ' ').all()  and initial_coordenate [1]-i >= 0     :          

        grid_human[initial_coordenate [0],initial_coordenate [1]-i:initial_coordenate [1]] = 'A'                                                
        

    elif orient == E and (grid_human[initial_coordenate [0],initial_coordenate [1]:initial_coordenate [1]+i] == ' ').all()  and initial_coordenate [1]+i < 10     :

        grid_human[initial_coordenate [0],initial_coordenate [1]:initial_coordenate [1]+i] = 'A'
        
    else: 
        boat_size.append(i)
     
# GRID BOT

for i in boat_size:

    initial_coordenate         = np.random.randint(0,10,size=2)

    orient      = np.random.randint(1,4,size=1)

    if orient   == N and (grid_bot[initial_coordenate [0]-i:initial_coordenate [0],initial_coordenate [1]]   == ' ').all() and initial_coordenate [0]-i >= 0    :

        grid_bot[initial_coordenate [0]-i:initial_coordenate [0],initial_coordenate [1]] = 'A'
        

    elif orient == S and (grid_bot[initial_coordenate [0]:initial_coordenate [0]+i,initial_coordenate [1]] == ' ').all()  and initial_coordenate [0]+i < 10     :

        grid_bot[initial_coordenate [0]:initial_coordenate [0]+i,initial_coordenate [1]] = 'A'
        

    elif orient == W and (grid_bot[initial_coordenate [0],initial_coordenate [1]-i:initial_coordenate [1]] == ' ').all()  and initial_coordenate [1]-i >= 0     :          

        grid_bot[initial_coordenate [0],initial_coordenate [1]-i:initial_coordenate [1]] = 'A'                                                
        

    elif orient == E and (grid_bot[initial_coordenate [0],initial_coordenate [1]:initial_coordenate [1]+i] == ' ').all()  and initial_coordenate [1]+i < 10     :

        grid_bot[initial_coordenate [0],initial_coordenate [1]:initial_coordenate [1]+i] = 'A'
        
    else: 
        boat_size.append(i)
     
 # DISPARO HUMANO
coordenate_1 = int(input('1ª coordenate'))

coordenate_2 = int(input('2ª coordenate'))

shoot_human =  grid_bot[coordenate_1,coordenate_2]

grid_blank_human            = np.full((10,10),' ') 

grid_blank_bot              = np.full((10,10),' ') 



if shoot_human == 'A':

	grid_bot[coordenate_1,coordenate_2] = 'X'
	grid_blank_human[coordenate_1,coordenate_2] = 'X'
	print('Hit')

else:

	grid_bot[coordenate_1,coordenate_2] = '-'
	grid_blank_human[coordenate_1,coordenate_2] = '-'
	print('Water')

 # DISPARO BOT
bot_coordenates      = np.random.randint(0,9,size=2)

shoot_bot =  grid_human[bot_coordenates[0],bot_coordenates[1]]

if shoot_bot  == 'A':

	grid_human[bot_coordenates[0],bot_coordenates[1]] = 'X'
	grid_blank_bot[bot_coordenates[0],bot_coordenates[1]] = 'X'
	print('Hit')

else:

	grid_human[bot_coordenates[0],bot_coordenates[1]] = '-'
	grid_blank_bot[bot_coordenates[0],bot_coordenates[1]] = '-'
	print('Water')


print(grid_blank_human)
print(grid_blank_bot)
# %%

