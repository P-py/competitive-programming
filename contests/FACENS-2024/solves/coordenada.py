def truncate(x, n):
	return int(x * (10**n)) / (10**n)

while True:
	n = int(input())
	if (n == 0):
		break
		
	for _ in range(n):
		coords = input().split()
		results = []
		
		for coord in coords:
			g = int(coord.split("g")[0])
			m = int(coord.split("m")[0].split("g")[1])
			s = int(coord.split("s")[0].split("m")[1])
			
			dir = coord[-1]
			
			decimalValue = (g) + (m/60) + (s/3600)
			
			if dir in ['S', 'W']:
				decimalValue *= -1
				
			decimalValue = truncate(decimalValue, 2)
			
			results.append(f"{decimalValue:.2f}")
			
		print(' '.join(results))
