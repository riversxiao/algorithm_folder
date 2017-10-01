# Uses python3
import sys

def fib_mod(n):
    memo ={0:0,
           1:1}
    period = [0,1]
    for i in range(2,n+1):
        memo[i] = memo[i-1] + memo[i-2]
        period.append(memo[i]%10)
        if period[-2:] ==[0,1]:
            index = (n+1)%(len(period)-2)
            return period[index-1]
    return memo[n]%10
if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fib_mod(n))
