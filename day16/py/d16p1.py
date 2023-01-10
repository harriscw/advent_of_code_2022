import matplotlib.pyplot as plt
import networkx as nx
import itertools

text_file = open("../input1.txt", "r")
lines = [v.strip("\n") for v in text_file.readlines()]

d=dict()
for i,line in enumerate(lines):
    key=line.split(" has flow")[0].split("Valve ")[1]
    weight=int(line.split(";")[0].split("=")[1])
    edges=line.replace("valves","valve").split("valve ")[1].replace(",","").split(" ")
    print(line,key,weight,edges)
    d[key]={"weight":weight,"connections":edges}

print(d)

# G = nx.Graph()
# for key in d: #Add nodes
#     G.add_node(key, weight=d[key]["weight"])

# for key in d:
#     for edge in d[key]["edges"]:
#         G.add_edge(key,edge)

# # nx.draw(G,with_labels = True)
# # plt.savefig('G.png')

# all_paths = []
# for combo in itertools.permutations(G.nodes, 10):
#     if(combo[0]=="AA"):
#         print(combo)


# find all connections
# if a connection weight is 0, find non-zero subconnections
# keep going until all subconnections are not 0
# randomly pick one out of all the options
# record path and number of steps
# stop when steps hit 34 or whatever
# if score < top score set this as the winning path
# repeat a bunch of times


# stop when you've hit max steps or you hit yourself again
path=["AA"]
for node in path:
    print(d[node]["connections"])
    options=[]
    for connection in d[node]["connections"]:
        while connection,d[connection]["weight"]==0:
            print("weight 0")
        else:

