text_file = open("../input.txt", "r")
string = text_file.readlines()[0]

# string="bvwbjplbgvbhsrlpgdmjqwftvncz"
# string="nppdvjthqldpwncqszvftbrmjlhg"
# string="nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
# string="zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"

# string="mjqjpqmgbljsphdztnvjfqwrcgsmlb"
# string="bvwbjplbgvbhsrlpgdmjqwftvncz"
# string="nppdvjthqldpwncqszvftbrmjlhg"
# string="nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
# string="zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"

def solve(string,num):
    for i in range(0,len(string)): #iterate over each character in string
        substring=list(set(string[i:num+i])) #slice to number of desired characters, find unique chars in slice
        if(len(substring)==num): #if there's repeats the length of the set will be less than the dsired characters
            return(i+num) #return the position at the end of the slice

print("Part 1",solve(string=string,num=4))
print("Part 2",solve(string=string,num=14))