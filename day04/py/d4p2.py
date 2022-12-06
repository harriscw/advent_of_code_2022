text_file = open("../input.txt", "r")
lines = [v.strip("\n").split(",") for v in text_file.readlines()]

acc=0
for i,line in enumerate(lines):
    sec1=[int(x) for x in line[0].split("-")] #convert group 1 to list of integers
    sec2=[int(x) for x in line[1].split("-")] #convert group 2 to list of integers

    overlap=list(set(range(sec1[0],sec1[1]+1)) & set(range(sec2[0],sec2[1]+1))) #find the intersection

    if(len(overlap)>0): #incrememnt if >0
        acc+=1
        # print(line,overlap)

print("Part 2:",acc)