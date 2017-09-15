# Uses python3
n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)
result = 0
s = sorted(a,reverse=True)
x,y = s[0:2]
result = x*y
print(result)
