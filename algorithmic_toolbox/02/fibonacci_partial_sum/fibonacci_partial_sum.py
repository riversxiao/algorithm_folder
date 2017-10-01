# Uses python3
import sys



def fib_sum(n):
    memo ={0:0,
           1:1}
    period = [0,1]
    if n == 0:
        return 0
    if n == 1:
        return 1
    for i in range(2,n+1):
        memo[i] = memo[i-1] + memo[i-2]
        period.append(memo[i]%10)
        if period[-2:] ==[0,1]:
            freq = (len(period)-2)
            inner_sum = sum(period[:-2])
            times = n//freq
            index = n % freq
            return (inner_sum * times + sum(period[:index+1]))%10
    return sum(period)%10

def fib_sum_p(from_, to):
    if from_ ==0 :
        return fib_sum(to)

    result =fib_sum(to)+10-fib_sum(from_-1)

    return result%10
if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fib_sum_p(from_, to))
