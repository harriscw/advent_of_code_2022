rm(list=ls())
input=readLines("../input.txt")

#paste it all together
res=paste(input,collapse="+")

#split on ++
res=unlist(strsplit(res,"\\+\\+"))

#evaluate each string in the vector
res = sapply(res,function(x){eval(parse(text=x))},simplify=TRUE)

paste("Part 1:",tail(sort(res),1))
paste("Part 2:",sum(tail(sort(res),3)))
