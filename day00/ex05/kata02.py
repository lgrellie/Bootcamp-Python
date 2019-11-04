t = (3, 30, 2019, 9, 25)

def date(hour, minutes, year, month, day):
	print(f'{month:02}/{day}/{year} {hour:02}:{minutes:02}')

date(*t)
