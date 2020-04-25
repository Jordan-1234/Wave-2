#Make list of all the numbers for red spaces
red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19 ,21, 23, 25, 27, 30, 32, 34 ,36]
num = int(input())

print("The spin results in", num)
print("Pay",num)

#If statements for the programs 
if num != 0 and num != 00:
    if num in red:
        print("Pay Red")
    else:
        print("Pay Black")

    if num % 2 == 0:
        print("Pay Even")
    else: 
        print("Pay Odd")

    if num in range(1, 19):
        print("Pay 1 to 18")
    else: 
        print("Pay 19 to 36")