import sys
result = ""
for i in range (1, len(sys.argv)):
    result += sys.argv[i].swapcase()
print(result[::-1])
