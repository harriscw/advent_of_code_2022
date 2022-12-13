import networkx as nx
from networkx.algorithms.shortest_paths.weighted import single_source_dijkstra #https://stackoverflow.com/a/56313003/3667133

text_file = open("../input.txt", "r")
lines = [list(v.strip("\n")) for v in text_file.readlines()]

letter_val={"S":0,"E":27}
acc=0
for letter in list('abcdefghijklmnopqrstuvwxyz'): #make a dictionary of each letter's value, reused day2 code
    acc+=1
    letter_val[letter]=acc

G = nx.DiGraph() #Make a directional graph
S=[]
for i,row in enumerate(lines): #Now populate graph edges by iterating over each point and looking U/D/L/R to if step is 1 or less
    for j,col in enumerate(row):
        thischar=lines[i][j]
        if(thischar=="a"): #----------------------Modified for part 2, save all starting points
            S.append(str(i)+","+str(j))
        elif(thischar=="E"):
            E=str(i)+","+str(j)

        if(j <len(row)-1): #right
            nextchar=lines[i][j+1]
            if(letter_val[nextchar]-letter_val[thischar] <=1): #if its <=1 step to move to the next point, add edge
                G.add_edge(str(i)+","+str(j),str(i)+","+str(j+1))
        if i < len(lines)-1: #down
            nextchar=lines[i+1][j]
            if(letter_val[nextchar]-letter_val[thischar] <=1):
                G.add_edge(str(i)+","+str(j),str(i+1)+","+str(j)) 
        if j >0: #left
            nextchar=lines[i][j-1]
            if(letter_val[nextchar]-letter_val[thischar] <=1):
                G.add_edge(str(i)+","+str(j),str(i)+","+str(j-1))
        if i > 0: #up
            nextchar=lines[i-1][j]
            if(letter_val[nextchar]-letter_val[thischar] <=1):
                G.add_edge(str(i)+","+str(j),str(i-1)+","+str(j))

outlist=[] # For part 2, loop over all starting points
for thisS in S:
    try:#Need try-catch here since not all starting points connect to the end point
        outlist.append(single_source_dijkstra(G,thisS,E)[0]) #used this algorithm in previous years
    except: #we should ignore those
        continue
print("Part 2:",min(outlist))