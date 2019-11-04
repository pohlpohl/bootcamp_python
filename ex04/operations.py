import sys

def error_output(msg = ""):
    if msg:
        exit(msg + "\nUsage: python operations.py\nExample:\n    python operations.py 10 3")
    else:
        exit("Usage: python operations.py\nExample:\n    python operations.py 10 3")


if len(sys.argv) == 1:
    error_output()
if len(sys.argv) < 3:
    error_output("InputError: not enough arguments")
if len(sys.argv) > 3:
    error_output("InputError: too many arguments")
if not sys.argv[1].isdigit() or not sys.argv[2].isdigit():
    error_output("InputError: only numbers")

a = int(sys.argv[1])
b = int(sys.argv[2])

print("Sum:\t" + str(a + b))
print("Difference: " + str(a - b))
print("Product:\t" + str(a * b))
if b:
    print("Quotient:\t" + str(float(a) / float(b)))
    print("Remainder: " + str(a % b))
else:
    print("Quotient:    ERROR (div by zero)\nRemainder: ERROR (modulo by zero)")

