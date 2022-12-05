text_file = open("../input.txt", "r")
lines = [v.strip("\n").split(",") for v in text_file.readlines()]

acc=0
for line in lines:
    sec1=[int(x) for x in line[0].split("-")] #convert group 1 to list of integers
    sec2=[int(x) for x in line[1].split("-")] #convert group 2 to list of integers

    if(sec2[0]>=sec1[0] and sec2[1]<=sec1[1]): #check if 2 falls into 1
        acc+=1
    elif(sec1[0]>=sec2[0] and sec1[1]<=sec2[1]): #check if 1 falls into 2
        acc+=1

print("Part 1:",acc)