text_file = open("../input.txt", "r")
lines = [v.strip("\n") for v in text_file.readlines()]

outlist=[] #first parse the input into a list of list, each sublift containing left and right
for i in range(0,len(lines)):
    if(i==0 or (i>0 and lines[i-1]=="")): #only append if the prior line was empty
        outlist.append([eval(lines[i]),eval(lines[i+1])])

def do_comp(left,right): #recursion is always hard to wrap my brain around
    # print("Comparing:",left,"vs",right)
    for l,r in zip(left,right):#this makes a pairwise iterable of two objects.  
                               #iterating like this with zip() will make the loop naturally stop if left and right are not balanced, which is crazy.
                               #e.g. [1,1,1] vs. [1,1,1,1] will stop after 3 iterations
                               #Using list() instead won't do that.  Thats a pretty neat trick
        # print(l,r)
        if(isinstance(l, int) and isinstance(r, int)):#if values are integers then compare them...
            if(l<r): #Correct order
                # print("Left smaller!")
                return(True)
            elif(l>r): #incorrect order
                # print("Left bigger!")
                return(False)
            else: #otherwise move to the next iteration
                continue
        elif(isinstance(l, list) and isinstance(r, list)): #if both values are lists recurse
            res=do_comp(left=l,right=r)
            if(res in [True,False]): #"None" can be a valid output here (e.g. [1,1] vs [1,1])
                return(res)
            else:  #otherwise move to the next iteration
                continue
        elif(isinstance(l, int) and isinstance(r, list)):
            res=do_comp(left=[l],right=r)
            if(res in [True,False]): #"None" can be a valid output here (e.g. [1] vs [1])
                return(res)
            else:  #otherwise move to the next iteration
                continue
        elif(isinstance(l, list) and isinstance(r, int)):
            res=do_comp(left=l,right=[r])
            if(res in [True,False]): #"None" can be a valid output here (e.g. [1] vs [1])
                return(res)
            else:  #otherwise move to the next iteration
                continue
    if(len(left)<len(right)):#if it makes it to this point its iterated to the end
        return(True)
    elif(len(left)>len(right)):
        return(False)

#------------------- Begin part 2

resl=[[[2]],[[6]]] #Lets reshape outlist into a single list instead of a list of pairs.  Also add divider packets
for i,line in enumerate(outlist):
    resl+=line

round=1
while True: #We are going to apply the function we created in part 1 iteratively over our dataset to sort it
    round+=1
    newresl=[] #a list to keep results of this sorting round
    alltrue=True #This is a flag for "are all elements sorted?".  If we see it set to True later then stop the while loop
    for i in range(1,len(resl)): #iterate over each element in the list.  Skip the first element because we are going to be comparing i vs i-1
        l=resl[i-1] #set left
        r=resl[i] #set right
        if(do_comp(left=l,right=r)): #if already sorted (l<r)
            sortedpair=[l,r]
        else:
            alreadysorted=False #we found an unsorted pair so set flag to false in order for while loop to continue
            sortedpair=[r,l]
        if(i==1):#if its the first iteration just add the sorted pair as the first 2 elements of the list we are populating
            newresl+=sortedpair
        else: #otherwise insert the sorted pair into the newly populated list at the position of left
            pos=newresl.index(l)
            newresl=newresl[:pos]+sortedpair+newresl[pos+1:] #this was the hardest part of part 2.  I wanted to just append the pair after popping the last element.  That doesn't work.
    resl=newresl #reset list for next sort iteration
    if(alltrue): #if nothing got sorted, stop the while loop
        break

print("Part 2:",(resl.index([[2]])+1)*(resl.index([[6]])+1))