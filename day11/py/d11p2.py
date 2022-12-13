text_file = open("../input.txt", "r")
lines = [v.strip("\n") for v in text_file.readlines()]

m_d=dict()
for i,line in enumerate(lines): #Parse the input into a dictionary
    if("Monkey " in line):
        m_num=int(line.split(" ")[1].replace(":",""))
        m_d[m_num]={"inspections":0}
    if("Starting items" in line):
        m_d[m_num]["items"]=[int(x) for x in line.split("items: ")[1].split(",")]
    if("Operation:" in line):
        m_d[m_num]["operation"]=line.split(" Operation: new = ")[1]
    if("Test:" in line):
        m_d[m_num]["test"]="new % "+line.split(" by ")[1] + " == 0"
    if("If true:" in line):
        m_d[m_num]["true"]=int(line.split("to monkey ")[1])
    if("If false:" in line):
        m_d[m_num]["false"]=int(line.split("to monkey ")[1])

#------------begin cheat portion
testpart=[int(m_d[key]["test"].split(" ")[2]) for key in m_d.keys()]
prod=1
for x in testpart:
    prod*=x
#-------------end cheat portion

num_monkeys=len(m_d.keys())
monkey=0
theround=1
while theround<=10000: #go for 10000 rounds
    if(theround % 50==0 and monkey==0):
        print(theround)
    for old in m_d[monkey]["items"]:
        m_d[monkey]["inspections"]+=1 #keep track of inspections
        new=eval(m_d[monkey]["operation"]) #evaluate operation
        new, d = divmod(new, 1) #get floor
        
        #------------begin cheat portion
        new=new % prod
        #------------end cheat portion
        if(eval(m_d[monkey]["test"])): #test true
            m_d[m_d[monkey]["true"]]["items"].append(new)
        else: #test failed
            m_d[m_d[monkey]["false"]]["items"].append(new)
    m_d[monkey]["items"]=[] #reset monkey list to empty after all items inspected
    
    monkey+=1
    if monkey==num_monkeys: #if we hit the last monkey
        monkey=0 #rest to 0
        theround+=1 #start a new round

outlist=[m_d[key]["inspections"] for key in m_d.keys()] #get a list of the inspection counts
outlist.sort() #sort it
print("Part 1:",outlist[-2:][0]*outlist[-2:][1]) #multiply highest two elements together