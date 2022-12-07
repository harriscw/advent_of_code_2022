text_file = open("../input.txt", "r")
lines = [v.strip("\n") for v in text_file.readlines()]

cwd=""
filelist=[] #create a dictionary with each file
dirlist=["/"] #create list of unique directories, initialized with root
child_dict=dict() #for each unique directory, create a dictionary of children
for i,line in enumerate(lines): #iterate over each commands

    if(cwd not in ["","/"]): #handle seperator, root doesn't need a "/"
        thesep="/"
    else:
        thesep=""

    if("$ cd" in line and line !="$ cd .."): #if you are going up a dir
        cwd+=thesep+line.split("$ cd ")[-1] #add to dir to cwd
    elif(line =="$ cd .."): #if you go down a dir
        cwd="/"+"/".join(cwd.split("/")[1:-1]) #split the cwd, remove last item, join backtogether by "/",add "/" to front
    elif("dir " in line[0:4]): #if you observe a directory...
        thedir=line.split("dir ")[-1] #split on 'dir " to get dir name
        dirlist.append(cwd+thesep+thedir) #then add full path to list of unique directories.  Previous versions I didnt account for "/a" and "/a/a" as distinct
     
        if(cwd not in child_dict.keys()): #Add new dir to dictionary keeping track of children for each dir
            child_dict[cwd]=[cwd+thesep+thedir]
        else:
            child_dict[cwd].append(cwd+thesep+thedir)

    elif(line != "$ ls"): #else record non-directory files in a file list
        filename=line.split(" ")[1]
        filesize=int(line.split(" ")[0])
        filelist.append((cwd,filename,filesize))


outdict=dict() #dictionary containing sums for each unique directory
for dir in dirlist: #iterate over each unique directory
    outdict[dir]=sum([file[2] for file in filelist if(dir == file[0])]) #First sum up all files in each directory
            
#Next we have to sum directories in each directory.  But since directories are nested we have to start at the deepest level
numslash=dict() #get dirlist ordered by number of "/"
for dir in dirlist:
    if(dir=="/"):
        numslash[dir]=0
    else:
        numslash[dir]=dir.count("/")

ordered_dirs=list({k: v for k, v in sorted(numslash.items(), key=lambda item: item[1])}.keys()) #I googled how to order keys by values
ordered_dirs.reverse()

for dir in ordered_dirs: #Now iterate over all directories starting from most to least nested
    if(dir in child_dict.keys()): #if the unique dir has children
        outdict[dir]+=sum([outdict[child] for child in child_dict[dir]]) #add value of each subdirectory to prior sum for the directory
            
print("Part 1:",sum([outdict[x] for x in outdict.keys() if outdict[x]<=100000]))
print("Part 2:",min([outdict[x] for x in outdict.keys() if outdict[x]>=30000000-(70000000-outdict["/"])])) #unused=total-used at root.  more needed=need(30K)-unused