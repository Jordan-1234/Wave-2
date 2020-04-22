#User inputs the coordinates
letter, num = list(input(("Input the letter and number: ")))
num = int(num)
row = num % 2 
#For each letter, if statements to determine black or white square
if letter == "a":
    if row == 1: print("The square is black")
    else: print("The square is white")
elif letter == "b":
    if row == 1: print("The square is white") 
    else: print("The square is black")
elif letter == "c":
    if row == 1: print("The square is black")
    else: print("The square is white")
elif letter == "d":
    if row == 1: print("The square is white")
    else: print("The square is black")
elif letter == "e":
    if row == 1: print("The square is black")
    else: print("The square is white")
elif letter == "f":
    if row == 1: print("The square is white")
    else: print("The square is black")
elif letter == "g":
    if row == 1: print("The square is black")
    else: print("The square is white")
elif letter == "h":
    if row == 1: print("The square is white")
    else: print("The square is black")
#Incorrect input by user
else: print("The input is not valid")