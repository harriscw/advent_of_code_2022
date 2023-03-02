text_file = open("../input.txt", "r")
lines = [[int(x) for x in v.strip("\n").split(",")] for v in text_file.readlines()]

#after drawing some pictures the idea is to look at each point and see if it has any neighbors
#if it has a neighbor in the dataset that side is covered
#you can find all potential neighbors for a given point by +1 and -1 on each x,y,z coord
def get_neighbors(point):
    neighbors=[]
    x=point[0]
    y=point[1]
    z=point[2]
    neighbors.append([x+1,y,z])
    neighbors.append([x-1,y,z])
    neighbors.append([x,y+1,z])
    neighbors.append([x,y-1,z])
    neighbors.append([x,y,z+1])
    neighbors.append([x,y,z-1])
    return neighbors

outlist=[]
for line in lines:#go through each point
    potential_neighbors=get_neighbors(line) #find all its potential neighbors
    for pneighbor in potential_neighbors:
        if pneighbor not in lines:
            if all([coord in lines for coord in get_neighbors(pneighbor)]):
                if pneighbor not in outlist:
                    outlist.append(pneighbor)


lines+=outlist
acc=0
for line in lines:#go through each point
    potential_neighbors=get_neighbors(line) #find all its potential neighbors
    actual_neighbors=[x for x in potential_neighbors if x in lines] #find the potential neighbors in the dataset
    acc+=(6-len(actual_neighbors))#uncovered sides is 6 (total sides) - number of actual neighbors

print("Part 1:",acc)
