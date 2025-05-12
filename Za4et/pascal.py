'''
дано число rowIndex, верните rowIndexth (0-indexed) строку паскаль треугольника
В Паскаль треугольнике, каждое числов это сумма двух предыдущих над ним.
'''

def getRow(rowIndex):
    current_row = [1]
    for _ in range(rowIndex):
        current_row = [ left + right for left, right in zip([0] + current_row, current_row + [0])]
    return current_row

print(getRow(3))
print(getRow(0))
print(getRow(1))
print(getRow(4))

