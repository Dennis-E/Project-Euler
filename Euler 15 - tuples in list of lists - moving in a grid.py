solutions=[]
solutions.append(1)
for i in range(440): solutions.append(0)			#A list of 400 representing the 21*21 grid
interim_solutions=[]
for i in range(0,440): interim_solutions.append(0)	#temporary calculation help
a=0

for round in range(40):								#40 steps to move until 20*20
	print(round)
	interim_solutions=list(solutions)
	for i in range(0,440):							#For every field in grid
		n=solutions[i]								#n=How many paths led to the respective field
		interim_solutions[i]-=n
		
		if (i+1)%21==0:
			pass
		else:
			interim_solutions[i+1]+=n				#Horizontal move
		
		if (i+1)>(440-21):	
			pass
		else:
			interim_solutions[i+21]+=n				#Vertical move
	
	solutions=list(interim_solutions)
	print(solutions)

print("Final:"+str(solutions))
print(len(solutions))
print(max(solutions))


"""
start_coordinate=(0,0,0)
grid=[]
interim_grid=[]
i=0

#preparing the 20*20 grid
for x in range(1,21):
	for y in range(1,21):
		grid.append((x,y,0))
grid[1]=(1,1,1)
interim_grid=list(grid)

#40 steps
for round in range(1,5):
	print("round"+str(round))
	for i in range(399,-1,-1):
		n=grid[i][2]
		if grid[i][1]==20:
			pass
		else:
			interim_grid[i+1]=(interim_grid[i+1][0],interim_grid[i+1][1],interim_grid[i+1][2]+n)		#vertical moves
			
		if grid[i][0]==20:
			pass
		else:
			interim_grid[i+20]=(interim_grid[i+20][0],interim_grid[i+20][1],interim_grid[i+20][2]+n)	#horizontal moves
		grid[i]=(grid[i][0],grid[i][1],0)
		interim_grid[i]=(interim_grid[i][0],interim_grid[i][1],0)
		
	grid=list(interim_grid)
	for x in range(1,21):
		for y in range(1,21):
			interim_grid.append((x,y,0))

print("final"+str(grid))
"""

"""
	for x in range(1,21):
		for y in range(1,21):
			i+=1
			n=grid[i][2]											#read number of occurences on coordinate
			#move n's horizontally
			grid[i]
		
		
		if grid[i][0]<20:										#The next horizontal step=twig
			grid[i]=(grid[i][0]+1,grid[i][1],grid[i][2])		
		else:
			pass
			
		if grid[i][1]<20:										#The next vertical step=twig
			grid[i]=(grid[i][0],grid[i][1]+1,grid[i][2])
		else:
			pass
	
	#Merge twigs
	
		
print(grid)
"""

"""
start_coordinate=[(0,0,0)]
pathes=[start_coordinate]
new_pathes=[]

#Moving along the grip starting from coordinate (0,0) in a logic tree step-by-step. From every position two new twigs origin. If still within (20,20) grid.

for i in range(1,41):
	print(i)
	for coordinate in pathes:
		new_coordinate=list(coordinate)									#create new twig
		newest_coordinate=list(coordinate)								#create second twig
		if (coordinate[i-1][1]+1)<=20:
			new_coordinate.append((coordinate[i-1][0],(coordinate[i-1][1])+1))	#add next step horizontally
			new_pathes.append(new_coordinate)								#interim saving so that it doesnt loop over it
		else:
			pass
		if (coordinate[i-1][0]+1)<=20:
			newest_coordinate.append(((coordinate[i-1][0]+1),coordinate[i-1][1]))	#add next step vertically
			new_pathes.append(newest_coordiante)
		else:
			pass		
	pathes=new_pathes
	
	#check if coordinate already exists and then count in 3rd tuple dimension
	for coordinate in new_pathes:
		for counter_horizontal in range(1,i):
			for counter_vertical in range(1,i):
				if coordinate[0][0]==i and coordinate[0][1]==j:				#first triple, horizontal dimension and vertical dimension
					coordinate[0][2]+=1
	new_pathes=[]
	print(len(pathes))

print(len(pathes))
"""
