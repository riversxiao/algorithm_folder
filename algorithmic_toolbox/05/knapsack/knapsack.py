# Uses python3
import sys
from collections import defaultdict
def optimal_weight(W, w):
    z = [0] * (n + 1)
    K = []
    for i in range(W + 1):
        K.append(list(z))
    for j in range(1, n + 1):
        wj = w[j - 1]
        vj = wj
        for x in range(1, W + 1):
            if wj > x:
                K[x][j] = K[x][j - 1]
            else:
                K[x][j] = max(K[x][j - 1], K[x - wj][j - 1] + vj)
    return K[W][n]

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
