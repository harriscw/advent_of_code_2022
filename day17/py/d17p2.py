import matplotlib.pyplot as plt

text_file = open("../input.txt", "r")
line = [v.strip("\n") for v in text_file.readlines()][0]

final_rocks={0:[1,2,3,4,5,6,7]} #initialize with highestpoint, key is Y value is list of X
highestpoint=0
rocknum=0
rockcnt=0
instruction_pos=0
while rockcnt<1000000000000:
    rockcnt+=1
    rocks = {1:[[3,highestpoint+4],[4,highestpoint+4],[5,highestpoint+4],[6,highestpoint+4]],     # Set rock positions
             2:[[4,highestpoint+6],[3,highestpoint+5],[4,highestpoint+5],[5,highestpoint+5],[4,highestpoint+4]],
             3:[[5,highestpoint+6],[5,highestpoint+5],[3,highestpoint+4],[4,highestpoint+4],[5,highestpoint+4]],
             4:[[3,highestpoint+7],[3,highestpoint+6],[3,highestpoint+5],[3,highestpoint+4]],
             5:[[3,highestpoint+5],[4,highestpoint+5],[3,highestpoint+4],[4,highestpoint+4]]}

    rocknum+=1 #going circularly through the rocks
    if rocknum==6:
        rocknum=1
    therock=rocks[rocknum]

    if(rockcnt % 1000000==0):
        del_these=[x for x in final_rocks.keys() if x<highestpoint-1000]
        for thiskey in del_these:
            del final_rocks[thiskey]
        print("------- Rock Number:",rockcnt,"Tippy top",highestpoint,"Keys",len(final_rocks.keys()))

    while True:#fall until you hit the ground
        ### Move HORIZONTALLY
        instruction=line[instruction_pos] #get left right instruction
        if(instruction_pos==len(line)-1):#increment/reset position as needed
            instruction_pos=0
        else:
            instruction_pos+=1
        if(instruction==">"): #translate that to x movement
            increment=1
        else:
            increment=-1

        moveit=True
        movedrock=[[x+increment,y] for x,y in therock]#potential new position of rock based on wind
        x_coords=[x for x,y in movedrock if x<1 or x>7] #get all new x coordinates that are out of range
        if len(x_coords)>0:#If any new x coordinates out of range
            moveit=False #dont move it
        else: #otherwise check if its blocked at any position
            for x,y in movedrock:#for each coordinate of new rock position
                if y in final_rocks.keys():#check if the new y value exists in dict
                    if x in final_rocks[y]:#and the new x value also exists
                        moveit=False #if both exist dont move the rock
                        break
        if moveit:#if its not blocked move the rock
            therock=movedrock


        #MOVE VERTICALLY
        stophere=False #check all coordinates and see if there's a already a point right below it.  If so stop
        for x,y in therock:
            if y-1 in final_rocks.keys():
                if x in final_rocks[y-1]: #there's something directly below this position so can't drop
                    stophere=True

        if stophere: #if the rock comes to rest...
            for x,y in therock:#First add new the new coordinates
                if y in final_rocks.keys():
                    if x not in final_rocks[y]:
                        final_rocks[y].append(x)
                else:
                    final_rocks[y]=[x]
            highestpoint = max(highestpoint,max([y for x,y in therock])) #Then reset highestpoint
            break #Finally stop the current rock from falling
        else:
            therock=[[x,y-1] for [x,y] in therock] #else continue and subtract 1 from each y

print("Part 2:",highestpoint) 