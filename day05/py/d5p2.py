text_file = open("../input.txt", "r")
lines = [v.strip("\n") for v in text_file.readlines()]

## We need to separate the columns from the instructions
the_inds=list(range(1,len(lines[0])+1,4)) #We can find the column numbers at these indexes

instrux_section=False
outdict=dict()
instrux=[]
for i,line in enumerate(lines): #iterate over all input
    if(line==""): #Flag for when we've moved from columns to instructions
        instrux_section=True
    this_row=[]
    if(not instrux_section): #if we're still iterating over the column portion...
        # print(line)
        for ind in the_inds:# ...this makes a dictionary of rows which needs to be rehaped later
            this_row.append(line[ind])
        outdict[i+1]=this_row
    elif(line != ""): #Else we've moved onto the instructions
        thesplit=line.split(" ")
        instrux.append((int(thesplit[1]),int(thesplit[3]),int(thesplit[5]))) #parse them into a tuple with 3 elements:  0:how many, 1:from, 2:to

del outdict[max(outdict.keys())] #remove the dictionary entry with column numbers
# print(outdict)

cols=dict() #OK create a dictionary where each entry is a column
for i in range(0,len(outdict[1])): 
    acc_list=[]
    for j in outdict.keys():
        # print(i,j,outdict[j])
        if(outdict[j][i] != " "):
            acc_list.append(outdict[j][i])
    acc_list.reverse()
    cols[i+1]=acc_list

acc=0
while acc <len(instrux): #finally, execute each instruction
    inst=instrux[acc]
    acc+=1
    dest=inst[2]
    origin=inst[1]
    num=inst[0]
    cols[dest]+=cols[origin][-num:]
    del cols[origin][-num:]

# print(cols)

outstring=""
for key in cols.keys(): #get the last element in each dictionary entry
    outstring+=cols[key][-1:][0]

print(outstring)