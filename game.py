import random
rn = random.randint(1, 5)

gn = int(input("랜덤 숫자를 추측해주세요 : "))
num = 0

while num != gn:
	if rn == gn:
		print("정답입니다")
		num += 1
		break
	gn = int(input("랜덤 숫자를 추측해주세요 : "))