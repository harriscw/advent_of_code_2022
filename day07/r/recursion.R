#time to try to actually learn recursion

mylist=list(
  1,
  list(2,
       list(3,4)),
  list(5,6,
       list(7,
            list(8,9,10,
                 list(11)))),
  list(12)
)

acc<<-0
myfunc=function(thelist){
  for(i in 1:length(thelist)){#iterate over each element in the list
    if(is.numeric(thelist[[i]])){#if its numeric...
      acc<<-acc+thelist[[i]]#add to global count
      print(thelist[[i]])
    }else{
      myfunc(thelist[[i]])#otherwise its a list so recurse
      #recursion will eventually stop because it will only find numerics
    }
  }
}

myfunc(mylist)
acc
sum(1:12)