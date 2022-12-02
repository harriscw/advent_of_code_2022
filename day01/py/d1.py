text_file = open("../input.txt", "r")
lines = [v.strip("\n") for v in text_file.readlines()]

sumlist=[]
acc=0

for i,line in enumerate(lines):
    if line != "" or i==len(lines): #you're not at the end of the elf, so keep summing
        acc += int(line)
    else: #you're at the end of the elf, so append the sum and reset it
        sumlist.append(acc)
        acc=0

print("Part 1:",max(sumlist))
sumlist.sort()
print("Part 2:",sum(sumlist[-3:]))