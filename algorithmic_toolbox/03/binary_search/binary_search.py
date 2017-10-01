# Uses python3
import sys

def binary_search(a, x,left=0,right=None):

    if right is None:
        right = len(a)
    middle = left + (right-left)//2
    if right <= left:
        return -1
    elif x == a[middle]:
        return middle
    elif x > a[middle]:
        return binary_search(a,x,middle+1,right)
    else:
        return binary_search(a,x,left,middle)



def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, x), end = ' ')
