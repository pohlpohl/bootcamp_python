from decimal import Decimal

t = (0, 4, 132.42222, 10000, 12345.67)

print('day_{:02}, ex_{:02} : {}, {:.2e},\
 {:.2e}'.format(t[0], t[1], round(t[2], 2), t[3], t[4]))
