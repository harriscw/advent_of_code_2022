text_file = open("../input.txt", "r")
lines = [v.strip("\n") for v in text_file.readlines()]

cycle=0
future_adds=[]
crt=0
sprite=[0,1,2]
crt_row=""
while True:
    if(cycle<len(lines)): #add new instructions to be executed
        line=lines[cycle]
        if(line=="noop"): #Append 0 to list if "noop"
            future_adds+=[0]
        else:
            future_adds+=[0,int(line.split(" ")[1])] #else append [0,val]

    if(crt in sprite): #if CRT position is one of the sprite positions
        crt_row+="#" #light up
    else:
        crt_row+="." #dark

    sprite[0]+=future_adds[0] #add current value to each sprite position
    sprite[1]+=future_adds[0]
    sprite[2]+=future_adds[0]
    future_adds=future_adds[1:] #remove first list item

    crt+=1
    if(crt>39):#if you hit the end of row
        print(crt_row) #display for final answer
        crt=0 #reset crt position and row
        crt_row=""

    if(cycle>len(lines) and len(future_adds)==0): #execute until both instructions and future adds are over
        break
        
    cycle+=1