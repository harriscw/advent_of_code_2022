text_file = open("../input.txt", "r")
lines = [v.strip("\n") for v in text_file.readlines()]

outlist=[] #first parse the input into a list of list, each sublift containing left and right
for i in range(0,len(lines)):
    if(i==0 or (i>0 and lines[i-1]=="")): #only append if the prior line was empty
        outlist.append([eval(lines[i]),eval(lines[i+1])])

def do_comp(left,right): #recursion is always hard to wrap my brain around
    print("Comparing:",left,"vs",right)
    for l,r in zip(left,right):#this makes a pairwise iterable of two objects.  
                               #iterating like this with zip() will make the loop naturally stop if left and right are not balanced, which is crazy.
                               #e.g. [1,1,1] vs. [1,1,1,1] will stop after 3 iterations
                               #Using list() instead won't do that.  Thats a pretty neat trick
        print(l,r)
        if(isinstance(l, int) and isinstance(r, int)):#if values are integers then compare them...
            if(l<r): #Correct order
                print("Left smaller!")
                return(True)
            elif(l>r): #incorrect order
                print("Left bigger!")
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

res=[]
for i,line in enumerate(outlist):#iterate over each line
    res.append(do_comp(left=outlist[i][0],right=outlist[i][1])*(i+1)) #multiply function result by pair number

print("Part 1:",sum(res))