def merge(left, right):
    result = []
    a, b = 0, 0
    inversions = 0
    while a < len(left) and b < len(right):
        if left[a] <= right[b]:
            result.append(left[a])
            a += 1
        else:
            result.append(right[b])
            inversions += len(left)-a
            b += 1
    result += left[a:]
    result += right[b:]
    return result, inversions
def sort(seq):
    if len(seq) <= 1:
        return seq, 0
    middle = int(len(seq) / 2)
    left, left_inversions = sort(seq[:middle])
    right, right_inversions = sort(seq[middle:])
    sorted_seq,inter_inversions = merge(left, right)
    return sorted_seq, inter_inversions+left_inversions+right_inversions
