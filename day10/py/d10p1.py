text_file = open("../input.txt", "r")
lines = [v.strip("\n") for v in text_file.readlines()]

cycle=0
X=1
future_adds=[]
strength=0
while True:
    if(cycle+1 in [20,60,100,140,180,220]):#cycles of interest
        newstrength=(cycle+1)*X #calculate cycle strength
        strength+=newstrength # add to total
        print("Start of iteration:",(cycle+1),"X:",X,"Strength:",newstrength)

    if(cycle<len(lines)): #add new instructions to be executed
        line=lines[cycle]
        if(line=="noop"): #Append 0 to list if "noop"
            future_adds+=[0]
        else:
            future_adds+=[0,int(line.split(" ")[1])] #else append [0,val]

    X+=future_adds[0] #Sum first list item to X every cycle, just will add 0 a bunch
    future_adds=future_adds[1:] #remove first list item
    
    if(cycle>len(lines) and len(future_adds)==0): #execute until both instructions and future adds are over
        break
    
    cycle+=1
        
print("Part 1:",strength)