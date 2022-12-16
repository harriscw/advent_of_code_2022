import matplotlib.pyplot as plt
import sys

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
for key in s_and_b.keys(): #The big ideas here are to 1. store coordinates in a dictionary 2. Store x values as ranges instead of individual points to try to make things faster
    print(key,"/",len(s_and_b.keys())-1)
    
    if(s_and_b[key]["sensor"][1] not in nobeacons.keys()):
        nobeacons[s_and_b[key]["sensor"][1]]=[[s_and_b[key]["sensor"][0],s_and_b[key]["sensor"][0]]] #if its a sensor it cant be a beacon
    else:
        nobeacons[s_and_b[key]["sensor"][1]].append([s_and_b[key]["sensor"][0],s_and_b[key]["sensor"][0]])

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


#---------- Part 2: Piece fragments back together.  If I find a place where there's a gap of 1 point, stop.
#---------- This feels like a heuristic but I was happy to see it worked.
#---------- Looking at the sample input pic it should be possible to have multiple regions with a gap of 1.
#---------- But I guess even then it would've helped narrow the search space.

nobeacons = {k: v for k,v in nobeacons.items() if k>0 and k<4000000} #get rid of keys <0 or >4million
acc=0
for key in nobeacons.keys(): #iterate over each key
    if(acc % 100000==0):
        print(acc,"/",len(nobeacons.keys()))
    for i,segment in enumerate(sorted(nobeacons[key])): #iterate over each segment for the given key.  I'm going to make the entire span for the key.
        if(i==0): #set the span to grow to the first segment on iteration 1
            span=segment
        elif(segment[0]<=span[1]+1 and segment[1]>span[1]): #otherwise if the new segment's start is <= the span (or the next number) and its not wholly contained in the growing span...
            span[1]=segment[1] #set the growing span end to the segment end
        elif(segment[0]-span[1]==2): #else if we see a single point gap stop everything and calculate the final answer
            print("length 1 Non-consecutive found:",key,span,segment)
            print("Part 2:",4000000*(span[1]+1)+key)
            sys.exit()
    acc+=1

if(False): #---------- Part 2: This is to make a plot with the sample input, don't think it would work on the full input
    yb=[]
    xb=[]
    ys=[]
    xs=[]
    for key in s_and_b.keys(): #Save sensors and beacons into lists for plotting
        thex=s_and_b[key]["beacon"][0]
        they=s_and_b[key]["beacon"][1]
        yb.append(-they)
        xb.append(thex)
        thex=s_and_b[key]["sensor"][0]
        they=s_and_b[key]["sensor"][1]
        ys.append(-they)
        xs.append(thex)     

    y=[]
    x=[]
    acc=1
    for key in sorted(nobeacons.keys()):#Save no beacon positions into list for plotting
        acc+=1
        print(acc,"/",len(nobeacons.keys()),"key:",key)
        for therange in nobeacons[key]: #get all the non-beacon points for given y value
            for thex in range(therange[0],therange[1]+1):
                y.append(-key)
                x.append(thex)

    plt.scatter(x,y,color="black",marker=".") #Make the plot
    plt.scatter(xb,yb,color="red",marker="p")
    plt.scatter(xs,ys,color="green",marker="p")
    plt.savefig('sample.png')