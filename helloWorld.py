num = 1
while num <= 30:
    if num % 10 == 0:
        print(num)
    else:
        if num < 10:
            print(" " + str(num), end=" ")
        else:
            print(num, end=" ")
    num += 1
'''
num = 1
while num <= 30:
    numForm = num
    if num < 10:
        numForm = " " + str(num)
    if num % 10 == 0:
        print(numForm)
    else:
        print(numForm, end=" ")
    num += 1
'''