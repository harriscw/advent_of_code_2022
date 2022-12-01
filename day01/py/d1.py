text_file = open("../input.txt", "r")
lines = [v.strip("\n") for v in text_file.readlines()]

sumlist=[]
acclist=[]

for i,line in enumerate(lines):
    if line != "" or i==len(lines): #you're not at the end of the elf, so append to list
        acclist.append(int(line))
    else: #you're at the end of the elf, so sum the list, append it, and reset it
        sumlist.append(sum(acclist))
        acclist=[]

print("Part 1:",max(sumlist))
sumlist.sort()
print("Part 2:",sum(sumlist[-3:]))