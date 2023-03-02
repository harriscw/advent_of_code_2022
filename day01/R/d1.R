rm(list=ls())
input=readLines("../input.txt")

bundles = c()
acc=0
for(line in input){ #iterate over each line in input
  if(line != ""){ #if line is not missing then you're still on the same elf...
    acc=acc+as.numeric(line) #...so add value to the running sum
  }else{ #otherwise you've hit the end of the elf... 
    bundles=c(bundles,acc) #...so append to vector of sums per elf
    acc=0 #and reset running sum
  }
}

print(paste("Part 1:",max(bundles))) #max
print(paste("Part 2:",sum(tail(sort(bundles),3)))) #get sum of top 3