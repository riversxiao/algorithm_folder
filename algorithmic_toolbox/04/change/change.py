# Uses python3
import sys

def get_change(m):
    numTen = m//10
    numFive = m%10//5
    numOne = m%10%5/1
    result = numTen + numFive + numOne
    return int(result)

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
