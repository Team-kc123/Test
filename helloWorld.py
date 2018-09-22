def is_one_digit(num):
    result = num
    if num < 10:
        result = " " + str(num)
    return result

num = 1
while num <= 30:
    numForm = num
    numForm = is_one_digit(numForm)
    if num % 10 == 0:
        print(numForm)
    else:
        print(numForm, end=" ")
    num += 1
