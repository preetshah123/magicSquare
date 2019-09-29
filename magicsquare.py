A=[]
import random
N = 0
M =0
while N <=1 or M<= 1: #ensures a matrix is bigger than 2x2
    N = int(input('how many rows do you want?'))
    M = int(input('how many columns do you want?'))
    if N <=1 or M <= 1:
        print('Matrix must be at least a 2x2'+'\n')

def solution(A):

    def rowSum(row,col,width): #adding up all the values in the row
        total = 0
        for a in range(width):
            total += A[row+a][col]
        return total
    def colSum (row,col,width): #adding up all the values in the columbs
        total = 0
        for a in range(width):
            total += A[row][col+a]
        return total
    def diagSum1(row,col,width): #adding up the values in the diagonal going down and to the right
        total = 0
        for a in range(width):
            total += A[row+a][col+a]
        return total
    def diagSum2(row,col,width): #adding up the values in the diagonal going down and to the left
        total = 0
        for a in range(width):
            total += A[row+a][col+width-1-a]
        return total
    def isMagicSqr(row,col,width):
        expected = diagSum1(row,col,width) #expected value is the initial sum and all others must match it for it to be a magic square
        if diagSum2(row,col,width) != expected:
            return False
        if rowSum(row,col,width) != expected or colSum(row,col,width) != expected:
            return False
        return True
    for numRows in range(N): #building a randomized NxM matrix A
        row = []
        for numCols in range(M):
            row.append(random.randint(1, 11))
        A.append(row)

    x = min(len(A), len(A[0]))
    maxSeen = 1
    rows = 0
    cols = 0
    for width in range(2,x+1):
        for startRow in range(len(A)-width+1):
            for startCol in range(len(A[0])-width+1):
                if isMagicSqr(startRow,startCol,width):
                    maxSeen = width
                    rows = startRow
                    cols = startCol

    square = []
    if maxSeen != 1:
        for magic in range(maxSeen): #outputting the magic square
            magicRow = []
            for final in range(maxSeen):
                magicRow.append(A[rows+magic][cols+final])
            square.append(magicRow)
        print(square)
    return maxSeen
magicSqr = solution(A)
failedTries = 0
while magicSqr == 1: #creating a new randomized NxM matrix if the previous one did not contain a magic square
    A=[]
    failedTries += 1
    magicSqr = solution(A)

print(magicSqr)
print('Failed ' + str(failedTries)+ ' times')
print(A)


