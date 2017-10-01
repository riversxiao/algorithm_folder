# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    curWeight = 0.
    total = 0.
    utilities = sorted([(x/y,y) for x,y in zip(values,weights)])
    count = 0
    while curWeight < capacity and utilities:
        count +=1
        if utilities[-1][1] <= capacity-curWeight:
            curWeight += utilities[-1][1]
            total += utilities[-1][0]*utilities[-1][1]
            utilities.pop()
        elif utilities[-1][1] > capacity-curWeight:
            total += utilities[-1][0]*(capacity-curWeight)
            curWeight += capacity-curWeight
    return total


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
