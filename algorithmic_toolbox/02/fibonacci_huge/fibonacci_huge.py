# Uses python3
import sys

# def fib_mod(n,m):
#     memo ={0:0,
#            1:1}
#     period = [0,1]
#     for i in range(2,n+1):
#         memo[i] = memo[i-1] + memo[i-2]
#         period.append(memo[i]%m)
#         if period[-2:] ==[0,1]:
#             index = (n+1)%(len(period)-2)
#             return period[index-1]
#     return memo[n]%m
def fib_mod(n,m):
    v1, v2, v3 = 1, 1, 0
    for rec in bin(n)[3:]:
        calc = (v2*v2) % m
        v1, v2, v3 = (v1*v1+calc) % m, ((v1+v3)*v2) % m, (calc+v3*v3) % m
        if rec == '1': v1, v2, v3 = (v1+v2) % m, v1, v2
    return v2

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(fib_mod(n, m))
