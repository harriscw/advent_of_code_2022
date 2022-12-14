text_file = open("../input1.txt", "r")
lines = [v.strip("\n") for v in text_file.readlines()]

outlist=[] #first parse the input into a list of list, each sublift containing left and right
for i in range(0,len(lines)):
    if(i==0 or (i>0 and lines[i-1]=="")): #only append if the prior line was empty
        outlist.append([eval(lines[i]),eval(lines[i+1])])



def do_comp(left,right):
    if(isinstance(left, int)): #if input is an integer make it a list
        left=[left]
    if(isinstance(right, int)):
        right=[right]
        
    maxcomps=min(len(left),len(right))
    print("Left:",left,"Right:",right,maxcomps)
    for i in range(0,maxcomps): #iterate ove the min length of left and right
        print("i",i,maxcomps-1)
        new_left=left[i]
        new_right=right[i]
        print("Compare",new_left,"to",new_right)

        if(isinstance(new_left, int) and isinstance(new_right, int)):
            if(new_left<new_right):
                print("Left<Right, inputs in right order")
                res.append(True)
                return()
            elif(new_left>new_right):
                print("Left>Right, inputs in wrong order")
                res.append(False)   
                return()
            elif(i==maxcomps-1 and len(left)<len(right)):#if counter ran out and left is the shorter
                print("Left ran out")
                res.append(True)
                return()
            elif(i==maxcomps-1 and len(right)<len(left)):#if counter ran out and right is the shorter
                print("Right ran out")
                res.append(False)
                return()
           
        elif(isinstance(new_left, list) and isinstance(new_right, list)):
            if(len(new_right)==0 and len(new_left)>0):
                print("Right ran out")
                res.append(False)
                return()
            if(len(new_left)==0 and len(new_right)>0):
                print("Left ran out")
                res.append(True)
                return()   
            else:
                do_comp(new_left,new_right)
        elif(isinstance(left[i], list) and isinstance(right[i], int)):
            do_comp(left[i],[right[i]])
        elif(isinstance(left[i], int) and isinstance(right[i], list)):
            do_comp([left[i]],right[i])

        

res=[]
for i,line in enumerate(outlist):
    thislen=len(res)
    do_comp(left=outlist[i][0],right=outlist[i][1])
    if(len(res)==thislen):
        res.append(True)
    # if(i==6):
    #     break

acc=0
for i in range(1,len(res)):
    acc+=res[i-1]*i

print(acc)