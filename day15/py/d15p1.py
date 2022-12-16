text_file = open("../input.txt", "r")
lines = [v.strip("\n") for v in text_file.readlines()]

def manhattan(s,b):
    distance = abs(b[0] - s[0]) + abs(b[1] - s[1]) 
    return(distance)

def get_length(nobeacons,beacons,yind):
    pointlist=[]
    for therange in nobeacons[yind]: #get all the non-beacon points for given y value
        for x in range(therange[0],therange[1]+1):
            pointlist.append(x)
    pointlist=[x for x in pointlist if x not in beacons[yind]] #remove becon points
    return(len(set(pointlist))) #return length of unique x values for given y

s_and_b=dict()#Parse input into a dictionary. 
for i,line in enumerate(lines): # Dict key is sensor number.  Value is dict with sensor and nearest beacon location
    line_=line.replace("x=","").replace("y=","").replace('Sensor at ',"").split(": closest beacon is at ")
    s_and_b[i]={"sensor":[int(x) for x in line_[0].split(", ")], "beacon":[int(x) for x in line_[1].split(", ")]}

nobeacons=dict()#dictionary for non-beacon locations.  key is y value
beacons=dict()#dictionary for beacon locations.  key is y value
for key in s_and_b.keys(): #The big ideas here are to 1. store coordinates in a dictionary 2. Store x values as ranges instead of individual points to try to make things faster
    print(key,"/",len(s_and_b.keys())-1)
    
    if(s_and_b[key]["sensor"][1] not in nobeacons.keys()):
        nobeacons[s_and_b[key]["sensor"][1]]=[[s_and_b[key]["sensor"][0],s_and_b[key]["sensor"][0]]] #if its a sensor it cant be a beacon
    else:
        nobeacons[s_and_b[key]["sensor"][1]].append([s_and_b[key]["sensor"][0],s_and_b[key]["sensor"][0]])

    if(s_and_b[key]["beacon"][1] not in beacons.keys()): #add beacon to beacon dictionary
        beacons[s_and_b[key]["beacon"][1]]=[s_and_b[key]["beacon"][0]]
    else:
        beacons[s_and_b[key]["beacon"][1]].append(s_and_b[key]["beacon"][0])

    dist=manhattan(s_and_b[key]["sensor"],s_and_b[key]["beacon"]) #calculate manhattan distance between sesnor and beacon

    startx=s_and_b[key]["sensor"][0] #now find all positions the given manhattan distance from sensor
    endx=s_and_b[key]["sensor"][0]
    for y in range(s_and_b[key]["sensor"][1]-dist,s_and_b[key]["sensor"][1]+dist+1): #do this by iterating from s-8 to s+8
        if(y not in nobeacons.keys()): #add x positions to dict
            nobeacons[y]=[[startx,endx]]
        else:
            nobeacons[y].append([startx,endx])

        if(y<s_and_b[key]["sensor"][1]): #increment x positions correctly to create diamond pattern
            startx-=1
            endx+=1
        else:
            startx+=1
            endx-=1

print("Part 1:",get_length(nobeacons,beacons,yind=2000000))