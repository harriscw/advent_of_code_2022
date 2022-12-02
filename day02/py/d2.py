text_file = open("../input.txt", "r")
lines = [v.strip("\n").split(" ") for v in text_file.readlines()]

# lines = [["A","Y"],["B","X"],["C","Z"]]
def get_val(val):
    if(val in ["A","X"]):
        return(1)
    elif(val in ["B","Y"]):
        return(2)
    elif(val in ["C","Z"]):
        return(3)

score=0
for i,line in enumerate(lines):
    if(line in [["C","X"],["A","Y"],["B","Z"]]):
        score+=get_val(line[1])+6
        res="I win"
    elif(line in [["B","X"],["C","Y"],["A","Z"]]):
        score+=get_val(line[1])
        res="I lose"
    else:
        score+=get_val(line[1])+3
        res="I tie"
    # print(line,res,score)

print("Part 1:",score)

def i_lose(theythrew): #returns the value of my throw when I lose
    if(theythrew=="A"):
        ithrow="C"
    elif(theythrew=="B"):
        ithrow="A"
    elif(theythrew=="C"):
        ithrow="B"
    return(get_val(ithrow))

def i_win(theythrew): #returns the value of my throw when I win
    if(theythrew=="A"):
        ithrow="B"
    elif(theythrew=="B"):
        ithrow="C"
    elif(theythrew=="C"):
        ithrow="A"
    return(get_val(ithrow))

score=0
for i,line in enumerate(lines):
    if(line[1])=="X":
        score+=i_lose(line[0])
        res="I lose"
    elif(line[1]=="Z"):
        score+=i_win(line[0])+6
        res="I win"
    else:
        score+=get_val(line[0])+3
        res="I tie"
    # print(line,res,score)

print("Part 2:",score)