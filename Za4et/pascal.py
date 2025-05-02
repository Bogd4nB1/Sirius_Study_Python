'''
дано число rowIndex, верните rowIndexth (0-indexed) строку паскаль треугольника
В Паскаль треугольнике, каждое числов это сумма двух предыдущих над ним.
'''

def getRow(rowIndex):
    row = [1]
    for _ in range(rowIndex):
        row = [x + y for x, y in zip([0]+row, row+[0])] # 1 iteration => [0,1] [1,0] -> (0,1) (1,0)
        print(row)
    return row

print(getRow(3))
print(getRow(0))
print(getRow(1))
print(getRow(4))

