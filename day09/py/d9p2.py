text_file = open("../input.txt", "r")
lines = [(v.strip("\n").split(" ")[0],int((v.strip("\n").split(" ")[1]))) for v in text_file.readlines()]

snake=dict() #Refactored a bunch from part 1.  Decided to store snake coordinates in a dictionary
for i in range(0,10):
    snake[i]=[0,0]

def simple_move(obj,line): #kept this the same from p1, needed to move the head
    if(line[0]=="R"):
        obj[0]+=1
    elif(line[0]=="L"):
        obj[0]-=1
    elif(line[0]=="U"):
        obj[1]+=1
    elif(line[0]=="D"):
        obj[1]-=1
    return(obj)

def sign(a): #helpful function I stole from the internet to get the sign of a number
    return ((a > 0) - (a < 0))

def move_tail(tail,head): #ugh this was the tricky part.  It took me a lot of time to think of this and then a lot of unit testing to get it right.

    diffx=head[0] - tail[0] #difference in x
    diffy=head[1] - tail[1] #difference in y
    distance = abs(diffx) + abs(diffy) #manhattan distance

    if(abs(diffx)>0 and abs(diffy)>0 and distance>=3): #difference in both x and y means segment is diagonal from prior one.
        tail[0]+=sign(diffx) #increment both x and y in the apropriate direction
        tail[1]+=sign(diffy) #sign function is handy!
    elif(abs(diffx)>0 and abs(diffy)==0 and distance==2): #else there's only a difference in x
        tail[0]+=sign(diffx) #so increment x
    elif(abs(diffx)==0 and abs(diffy)>0 and distance==2): #else there's only a difference in y
        tail[1]+=sign(diffy) #so increment y

    return(tail)

coord_list=[(0,0)]#keep a list of coordinates tail has visited.  Initialize with origin
for i,line in enumerate(lines): ## OK now move the snake
    print("--------- Instruction:",line)
    for j in range(line[1]):#execute each step of instruction...
        for k in snake.keys(): #...for each segment of the snake
            if(k==0): #first move the head
                snake[0]=simple_move(obj=snake[0],line=line) 
            else: #now iteratively move the segments
                snake[k]=move_tail(tail=snake[k],head=snake[k-1])
        
        coord_list.append((snake[9][0],snake[9][1])) #add tail coordinate to list of coordinates tail has visited

print("Part 2:",len(list(set(coord_list))))

# Do a visualization
x=[coord[0] for coord in coord_list]
y=[coord[1] for coord in coord_list]

import matplotlib.pyplot as plt

plt.plot(x,y)
plt.plot(0,0,"x",markersize=15)
plt.savefig('snaketail.png')