#User inputs the coordinates
letter, num = list(input((Input the coordinates)))
num = int(num)
row = num % 2 
#For each letter, if statement for black or white
if letter == "a":
    if row == 1: print("black")
    else print("white")
elif letter == "b":
    if row == 1: print("white") 
    else print("black")
elif letter == "c":
    if row == 1: print("black")
    else print("white")
elif letter == "d":
    if row == 1: print("white")
    else print("black")
elif letter == "e":
    if row == 1: print("black")
    else print("white")
elif letter == "f":
    if row == 1: print("white")
    else print("black")
elif letter == "g":
    if row == 1: print("black")
    else print("white")
elif letter == "f":
    if row == 1: print("white")
    else print("black")