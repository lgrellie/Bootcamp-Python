t = (0, 4, 132.42222, 10000, 12345.67)

def kata_four(day, ex, a, b, c):
	print(f'day_{day:02}, ex_{ex:02} : {a:.2f}, {b:.2e}, {c:.2e}')

kata_four(*t)
