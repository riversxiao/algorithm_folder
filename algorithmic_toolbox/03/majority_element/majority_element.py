# Uses python3
import sys

def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]

    half = (right - left) // 2
    ml = get_majority_element(a, left, left + half)
    mr = get_majority_element(a, left + half, right)

    mlc = mrc = 0
    for v in a[left:right]:
        if v == ml:
            mlc += 1
        if v == mr:
            mrc += 1

    if mlc > half:
        return ml
    if mrc > half:
        return mr

    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
