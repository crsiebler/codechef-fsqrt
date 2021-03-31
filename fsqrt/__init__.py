import sys
import math

input()
print("\n".join([str(int(math.sqrt(int(x)))) for x in sys.stdin.readlines()]))
