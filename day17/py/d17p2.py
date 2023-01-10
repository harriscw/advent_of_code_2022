text_file = open("../input.txt", "r")
lines = [v.strip("\n") for v in text_file.readlines()]
print(lines)
