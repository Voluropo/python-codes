JESTER = 'SIMPLE'
print(JESTER.lower())

jester = 'simple'
print(jester.upper())

print(jester.strip())

price1 = 12000
price2 = 69000
total = sum([price1,price2])
report = ' total{},others{},more{} '
print(report.format(total,price1,price2))

price1 = 30000
price2 = 50000
price3 = 150000
total = sum([price1,price2,price3])
report= ' at end of the day activities the total deposit that came in is {},mr.ade deposited {} mrs.nkechi {} mr.sola{}   '
print(report.format(total,price1,price2,price3))
print(f'at end of the day activities the total deposit that came in is {total},mr.ade deposited {price1} mrs.nkechi {price2} mr.sola{price3}')

