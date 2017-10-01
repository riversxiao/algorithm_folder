# Uses python3
import sys

def optimal_sequence(number):
    if number <= 0:
        return reversed([0])
    MinNumSteps = {1:[0,0]}
    for i in range(2, number +1):
        MinNumSteps[i] = [float('inf'),[]]
        operations = [[1,1],[2,0],[3,0]]
        for operation in operations:
            if i%operation[0]==0 and i-operation[1]>= 1:
                NumSteps = MinNumSteps[i//operation[0] -operation[1]][0] + 1
                if NumSteps < MinNumSteps[i][0]:
                    MinNumSteps[i][0] = NumSteps
                    MinNumSteps[i][1] = i//operation[0] -operation[1]
    result = [number]
    start = result[-1]
    for i in range(MinNumSteps[number][0]):
        t = start
        result.append(MinNumSteps[t][1])
        start = result[-1]

    return reversed(result)

input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
