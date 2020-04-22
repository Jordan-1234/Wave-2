#User inputs the coordinates
letter, num = list(input((Input the coordinates)))
num = int(num)
row = num % 2 
#For each letter, state black or white
if letter == "a":
    if row == 1: print("black")
    else print("white")
elif letter == "b":
    if row == 1: print("white") 
    else print("black")
elif letter == "c":
    if row == 1: print("black")