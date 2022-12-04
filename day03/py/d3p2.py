text_file = open("../input.txt", "r")
lines = [v.strip("\n") for v in text_file.readlines()]

outlist=[]
groups=[]
acc=0
for i,line in enumerate(lines): #iterate over each line ...
    acc+=1
    if(acc in [1,2,3]): #...and store every 3 lines into a list
        groups.append(line)
    if(acc == 3): # If you hit the end of the group...
        outlist+=list(set(groups[0]) & set(groups[1]) & set(groups[2])) #...find the intersection between the 3 lines in the group
        acc = 0 #now reset these objects
        groups=[]

outdict=dict() #Then just reuse code from part 1 verbatim
acc=0
for letter in list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'): #make a dictionary of each letter's value
    acc+=1
    outdict[letter]=acc

acc=0
for letter in outlist: #iterate over each letter, look up value, add it to the total
    acc+=outdict[letter]

print("Part 2:",acc)