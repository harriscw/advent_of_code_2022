text_file = open("../input.txt", "r")
lines = [(v.strip("\n").split(" ")[0],int((v.strip("\n").split(" ")[1]))) for v in text_file.readlines()]

head=[0,0]
tail=[0,0]

def simple_move(obj,line):
    if(line[0]=="R"):
        obj[0]+=1
    elif(line[0]=="L"):
        obj[0]-=1
    elif(line[0]=="U"):
        obj[1]+=1
    elif(line[0]=="D"):
        obj[1]-=1
    return(obj)

coord_list=[(tail[0],tail[1])]#keep a list of coordinates tail has visited.  Initialize with origin
for i,line in enumerate(lines):
    print("--------- Instruction:",line)
    for j in range(line[1]):#need to keep track of head and tail for every move executed
        #first move head
        simple_move(obj=head,line=line)#new coord for head

        #now move tail - need manhattan distance and slope for this
        distance = abs(tail[0] - head[0]) + abs(tail[1] - head[1])
        if(tail[0] != head[0]):
            slope=(tail[1] - head[1])/(tail[0] - head[0])
        else:
            slope=0 #avoid divide by 0
        
        #now do the move
        if(abs(distance)==2 and slope==0):#if they aren't adjacent and moving on same axis
            simple_move(obj=tail,line=line)#new coord 
        elif(abs(distance)>2 and slope != 0):#else if they aren't adjacent and are diagonal
            if(line[0] in ["U","D"]): #if head is moving up/down reset tail x to be same column as head
                tail[0]=head[0]
            else: #if head is moving left/right reset tail y to be same row as head
                tail[1]=head[1]
                
            simple_move(obj=tail,line=line) #tail then executes the move command to reduce the distance
        coord_list.append((tail[0],tail[1])) #add coordinate to list of coordinates tail has visited
        print("Step:",i,j,head,tail)
     
print("Part 1:",len(list(set(coord_list))))