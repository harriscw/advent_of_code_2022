text_file = open("../input.txt", "r")
lines = [v.strip("\n") for v in text_file.readlines()]

def sub_score(thisone,prior,lines,i,j):#how many other trees can you see from a given tree
    if(len(prior)>0):
        seeable_trees=[]
        for tree in prior: #iterate over trees in the prior list
            if(tree<thisone): #if the tree is < your tree you can see it, so append
                seeable_trees.append(tree)
            else: #you've hit a tree >= your tree, append it then stop the loop
                seeable_trees.append(tree)
                break
        return(len(seeable_trees)) #return the number of trees you can see in this direction

    else:
        return(0) #edges always return 0 I guess, score should just sum seeable trees

scores=[]
for i,line in enumerate(lines): #iterate over rows
    for j,char in enumerate(line): #iterate over each number in row

        thisone=list(line)[j] #current tree for comparison

        prior=list(line)[:j] #get all trees to the left
        prior.reverse() #need to reverse the slice above when iteratively looking left
        from_left=sub_score(thisone,prior,lines,i,j)

        prior=list(line)[j+1:len(line)] #do it again using all trees to the right
        from_right=sub_score(thisone,prior,lines,i,j)

        prior=[list(line)[j] for line in lines[0:i]] #do it again using all trees to the top
        prior.reverse() #need to reverse the slice above when iteratively looking up
        from_top=sub_score(thisone,prior,lines,i,j)
        
        prior=[list(line)[j] for line in lines[i+1:len(lines)]] #do it again using all trees to the bottom
        from_bottom=sub_score(thisone,prior,lines,i,j)
    
        this_score=from_left*from_right*from_top*from_bottom #get score and append
        scores.append(this_score)

print("Part 2:",max(scores)) #get max
