# 9以下の場合空白を足す関数
def is_one_digit(_num):
	result = _num
	if _num < 10:
		result = "  " + str(_num)
	elif _num < 100:
		result = " " + str(_num)
	return result


# 初期化
x = input("Please Enter Number: ")
maxNum = int(x)
num = 1

# 1から30までコンソールに出力する処理
while num <= maxNum:
	numForm = num
	numForm = is_one_digit(numForm)
	if num % 10 == 0:
		print(numForm)
	else:
		print(numForm, end=" ")
	num += 1
