text_file = open("../input.txt", "r")
lines = [v.strip("\n") for v in text_file.readlines()]

outlist=[]
for i,line in enumerate(lines): #divide each line into 2, then append the intersection of the two lines
    first=list(line[0:int(len(line)/2)])
    second=list(line[int(len(line)/2):])
    outlist+=list(set(first) & set(second))

outdict=dict()
acc=0
for letter in list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'): #make a dictionary of each letter's value
    acc+=1
    outdict[letter]=acc

acc=0
for letter in outlist: #iterate over each letter, look up value, add it to the total
    acc+=outdict[letter]

print("Part 1:",acc)