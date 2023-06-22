import random
rn = random.randint(1, 5)
gn = int(input("랜덤 숫자를 추측해보세요: "))
if rn == gn:
	print("정답입니다!")
else:
	print(f"틀렸습니다! 정답은 {rn}입니다!")
