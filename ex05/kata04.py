from decimal import Decimal

t = (0, 4, 132.42222, 10000, 12345.67)

print('day_{:02}, '.format(t[0]) + 'ex_{:02} : '.format(t[1]) + '{}, '.format(round(t[2], 2)) + '{:.2e}, '.format(t[3]) + '{:.2e}, '.format(t[4]))
