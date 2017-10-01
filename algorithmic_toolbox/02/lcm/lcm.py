# Uses python3
import sys

def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x
# least common multiplier
# large number intger division
def lcm(a, b):
    result = a*b//gcd(a,b)
    return int(result)

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm(a, b))
