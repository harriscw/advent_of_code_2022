import matplotlib.pyplot as plt

text_file = open("../input.txt", "r")
lines = [v.strip("\n") for v in text_file.readlines()]

def get_points_between_coords(start,end): #function to parse initial input
    coord_list=[]
    if(start[0]==end[0] and start[1]<=end[1]):#x coordinate is the same, iterate right
        for i in range(start[1],end[1]+1,1):
            coord_list.append([start[0],i])

    elif(start[0]==end[0] and start[1]>=end[1]):#x coordinate is the same, iterate left
        for i in range(start[1],end[1]-1,-1):
            coord_list.append([start[0],i])

    elif(start[1]==end[1] and start[0]<=end[0]):#y coordinate is the same, iterate right
        for i in range(start[0],end[0]+1,1):
            coord_list.append([i,end[1]])  

    elif(start[1]==end[1] and start[0]>=end[0]):#y coordinate is the same, iterate left
        for i in range(start[0],end[0]-1,-1):
            coord_list.append([i,end[1]])   
    return(coord_list)    

def convert_for_plot(coords): #function to plot x and y vals stored as a dictionary
    x=[]
    y=[]
    for xi in coords.keys():
        for yi in coords[xi]:
            x.append(xi)
            y.append(-yi)
    return((x,y))

def do_one_sand(acc): #get the final coordinate of a given piece of sand being drop
    x=500 #starting point
    y=0
    round=1
    while True:
        # print("Round:",round,x,y)
        if(y+1 not in coords[x]): #if nothing below go there
            y+=1
        elif(x-1 in coords.keys() and y+1 not in coords[x-1]):   #if nothing down & left go there
            x-=1
            y+=1
        elif(x+1 in coords.keys() and y+1 not in coords[x+1]): #if nothing down & right go there
            x+=1
            y+=1
        elif(500 in coords.keys() and 0 in coords[500]): #---------------Part 2: New stopping criteria - stop if sand origin has sand
            return(False)
        else: #otherwise youre finished
            return([x,y])
        round+=1

def make_a_plot(x,y,orig_coords,acc): #make a plot of the current state
    x,y=convert_for_plot(coords)
    plt.scatter(x,y,color="yellow",marker="X")
    plt.scatter(orig_coords[0],orig_coords[1],color="black",marker="o")
    plt.savefig('round'+str(acc)+'.png')

coords=dict() #keys are x values
acc=0
for i,line in enumerate(lines):#--------------First lets parse input into all the rock coordinates and store them into a dictionary
    newline=line.split(" -> ")
    for j in range(1,len(newline)):#iterate over list of split items this line
        acc+=1
        res=get_points_between_coords([int(x) for x in newline[j-1].split(",")],[int(x) for x in newline[j].split(",")]) #get all coordinates between start and end
        for x,y in res: #add to dictionary
            if(x not in coords.keys()):
                coords[x]=[y]
            elif(y not in coords[x]):
                coords[x].append(y)


miny=0 #-------------- Part 2:  Add the floor
for key in coords.keys(): #Find the min y value of all the rocks
    thismin=max([y for y in coords[key]])
    miny=max(miny,thismin)

for key in range(300,700): #add the new floor for part 2. did 0 to 1000 first, shortened to make gif better
    if(key in coords.keys()):
        coords[key].append(miny+2)
    else:
        coords[key]=[miny+2] #-------------- 

orig_coords=convert_for_plot(coords) #save these for plotting later

acc=0
while True: #Now continuously drop sand until the abyss is hit
    acc+=1
    res=do_one_sand(acc)
    if(acc % 250==0): #plot state every x iterations
        print("Sand #:",acc)
        x1,y1=convert_for_plot(coords)
        make_a_plot(x1,y1,orig_coords,acc)
    if(res==False): #Function outputs False when an edge is hit
        print("Part 2: Full at",acc-1)
        x1,y1=convert_for_plot(coords)
        make_a_plot(x1,y1,orig_coords,acc-1)
        break
    elif(res[0] not in coords.keys()): #make a new key if it doesn't exist
        coords[res[0]]=[res[1]]
    elif(res[1] not in coords[res[0]]): #else append to existing key
        coords[res[0]].append(res[1])