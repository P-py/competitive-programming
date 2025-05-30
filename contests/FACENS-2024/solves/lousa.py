import math
import sys

input = sys.stdin.readline

while True:
	# A = largura
	# B = altura
	# C = D1
	# D = D2
	A, B, C, D = map(int, input().split())
	if (A, B, C, D) == (0, 0, 0, 0):
		break
		
	try:
		cosAngle1 = (math.pow(C, 2)) + (math.pow(A, 2)) - (math.pow(D, 2))
		cosAngle1 = cosAngle1 / (2 * C * A)
		
		angleValue = math.acos(cosAngle1)
		
		angleSin = math.sin(angleValue)
		angleCos = math.cos(angleValue)

		x = round(angleCos * C)
		y = round(angleSin * C)
				
		if (0 <= x <= A) and (0 <= y <= B):
			print(f"{x} {y}")
		else:
			print("DEFEITO")
	except:
		print("DEFEITO")
