text_file = open("../input.txt", "r")
lines = [v.strip("\n") for v in text_file.readlines()]

def can_be_seen(thisone,prior,lines,i,j):
    if(i==0 or j==0): #if tree is in the first row or column
        return(True)
    elif(i==len(lines)-1 or j==len(lines[0])-1): #if tree is in the last row or column
        return(True)
    elif(len(prior)>0 and all([x<thisone for x in prior])): #if tree > all prior trees
        return(True)
    else:
        return(False)

outlist=[]
for i,line in enumerate(lines): #iterate over rows
    for j,char in enumerate(line): #iterate over each number in row
        thisone=list(line)[j] #current tree for comparison

        prior=list(line)[:j] #get all trees to the left
        if(can_be_seen(thisone,prior,lines,i,j)): #if current tree is > all trees to the left...
            outlist.append((i,j)) #append this point to list

        prior=list(line)[j+1:len(line)] #do it again using all trees to the right
        if(can_be_seen(thisone,prior,lines,i,j)):
            outlist.append((i,j))

        prior=[list(line)[j] for line in lines[0:i]] #do it again using all trees to the top
        if(can_be_seen(thisone,prior,lines,i,j)):
            outlist.append((i,j))
        
        prior=[list(line)[j] for line in lines[i+1:len(lines)]] #do it again using all trees to the bottom
        if(can_be_seen(thisone,prior,lines,i,j)):
            outlist.append((i,j))
        
print("Part 1:",len(list(set(outlist)))) #Find length of list of unique trees that can be seen