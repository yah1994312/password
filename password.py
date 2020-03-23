x = 3
while True:
	passward = input('請輸入密碼：')
	if passward == 'a123456':
		print('登錄成功')
		break
	else:
		x = x - 1
		print('密碼錯誤！還有', x ,'次機會')
		if x == 0:
			print('密碼全錯')
			break