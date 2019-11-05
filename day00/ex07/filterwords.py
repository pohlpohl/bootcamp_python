import sys

if len(sys.argv) != 3 or not sys.argv[2].isdigit() or sys.argv[1].isdigit():
    exit("ERROR")

plouf = []
lim = int(sys.argv[2])

for i in sys.argv[1].split():
    if len(i) > lim:
        plouf.append(i)

print(plouf)
