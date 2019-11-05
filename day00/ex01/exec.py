import sys
result = ""
for i in range(1, len(sys.argv)):
    result += sys.argv[i].swapcase()
    if i < len(sys.argv) - 1:
        result += " "
print(result[::-1])
