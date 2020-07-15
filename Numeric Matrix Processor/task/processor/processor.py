def show_menu():
    print('1. Add matrices')
    print('2. Multiply matrix by a constant')
    print('3. Multiply matrices')
    print('4. Transpose matrix')
    print('5. Calculate a determinant')
    print('6. Inverse matrix')
    print('0. Exit')
    return int(input('Your choice: '))

def add_matrics(row, column, matrix1, matrix2):
    sum = [[float(matrix1[r][c]) + float(matrix2[r][c]) for c in range(column)] for r in range(row)]
    print('The result is:')
    for group in sum:
        print(*group)

def choice_one():
    row1, column1 = [ int(n) for n in input('Enter size of first matrix: ').split(' ')]
    print('Enter first matrix:')
    matrix1 = [ input().split(' ') for i in range(row1)]
    row2, column2 = [ int(n) for n in input('Enter size of second matrix: ').split(' ')]
    print('Enter second matrix:')
    matrix2 = [ input().split(' ') for i in range(row2)]
    if row1 != row2 or column1 != column2:
        print('The operation cannot be performed.')
    else:
        add_matrics(row1, column1, matrix1, matrix2)

def multiply_matrix(row, column, matrix1, multiple):
    sum = [[float(matrix1[r][c]) * multiple for c in range(column)] for r in range(row)]
    print('The result is:')
    for group in sum:
        print(*group)

def choice_two():
    row, column = [int(n) for n in input('Enter size of matrix: ').split(' ')]
    print('Enter matrix:')
    matrix = [ input().split(' ') for i in range(row)]
    multiple = float(input('Enter constant: '))
    multiply_matrix(row, column, matrix, multiple)

def multiply_matrices(row1, column1, row2, column2, matrix1, matrix2):
    result = []
    for r in range(row1):
        result.append([])
        for c in range(column2):
            element = 0
            for n in range(column1):
                element += (float(matrix1[r][n]) * float(matrix2[n][c]))
            result[r].append(element)
    #result = [[int(matrix1[r][c]) * int(matrix2[r][c]) + int(matrix1[r][c+1]) * int(matrix2[r+1][c]) + int(matrix1[r][c+2]) * int(matrix2[r+2][c]) for c in range(column2)] for r in range(row1)]
    print('The result is:')
    for group in result:
        print(*group)

def choice_three():
    row1, column1 = [ int(n) for n in input('Enter size of first matrix: ').split(' ')]
    print('Enter first matrix:')
    matrix1 = [ input().split(' ') for i in range(row1)]
    row2, column2 = [ int(n) for n in input('Enter size of second matrix: ').split(' ')]
    print('Enter second matrix:')
    matrix2 = [ input().split(' ') for i in range(row2)]
    if column1 == row2:
        multiply_matrices(row1, column1, row2, column2, matrix1, matrix2)

def choice_four():
    print('1. Main diagonal')
    print('2. Side diagonal')
    print('3. Vertical line')
    print('4. Horizontal line')
    choice = int(input('Your choice: '))
    row, column = [int(n) for n in input('Enter matrix size: ').split(' ')]
    print('Enter matrix:')
    matrix = [input().split(' ') for r in range(row)]
    if choice == 1:
        main_diagonal(row, column, matrix)
    elif choice == 2:
        side_diagonal(row, column, matrix)
    elif choice == 3:
        vertical_line(row, column, matrix)
    elif choice == 4:
        horizontal_line(row, column, matrix)

def main_diagonal(row, column, matrix):
    result = [[ matrix[r][c] for r in range(row)] for c in range(column)]
    print('The result is:')
    for group in result:
        print(*group)

def main_diagonal_matrix(row, column, matrix):
    result = [[ matrix[r][c] for r in range(row)] for c in range(column)]
    return result

def side_diagonal(row, column, matrix):
    result = [[ matrix[r][c] for r in range(row-1, -1, -1)] for c in range(column-1, -1, -1)]
    print('The result is:')
    for group in result:
        print(*group)

def vertical_line(row, column, matrix):
    result = [[ matrix[r][c] for c in range(column-1, -1, -1)] for r in range(row)]
    print('The result is:')
    for group in result:
        print(*group)

def horizontal_line(row, column, matrix):
    result = [[ matrix[r][c] for c in range(column)] for r in range(row-1, -1, -1)]
    print('The result is:')
    for group in result:
        print(*group)

def choice_five():
    row, column = [int(n) for n in input('Enter matrix size: ').split(' ')]
    print('Enter matrix:')
    matrix = [[float(n) for n in input().split(' ')] for i in range(row)]
    if row == column:
        print('The result is:')
        print(calculate_determinant(row, matrix))

def calculate_determinant(n, matrix):
    if n == 2:
        return round(matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0], 9)
    if n == 1:
        return matrix[0][0]
    det = 0
    for c in range(n):
        matrix_M = calculate_matrix_M(n, matrix, 0, c)
        det += matrix[0][c] * ((-1)**(1 + c + 1)) * calculate_determinant(n-1, matrix_M)
    return round(det, 9)

def calculate_matrix_M(n, matrix, i, j):
    return [[matrix[r][c] for c in range(n) if c != j] for r in range(n) if r != i]

def choice_six():
    row, column = [int(n) for n in input('Enter matrix size: ').split(' ')]
    print('Enter matrix:')
    matrix = [[float(n) for n in input().split(' ')] for i in range(row)]
    if row == column:
        inverse_matrix(row, matrix)

def inverse_matrix(n, matrix):
    cofactor_matrix = []
    for r in range(n):
        cofactor_matrix.append([])
        for c in range(n):
            cofactor = (-1)**(r+1+c+1) * calculate_determinant(n-1, calculate_matrix_M(n, matrix, r, c))
            cofactor_matrix[r].append(cofactor)
    transposed_cofactor_matrix = main_diagonal_matrix(n, n, cofactor_matrix)
    det_matrix = calculate_determinant(n, matrix)
    if det_matrix == 0:
        print("This matrix doesn't have an inverse.")
    else:
        multiply_matrix(n, n, transposed_cofactor_matrix, 1 / det_matrix)

    # 1 / calculate_determinant(n, matrix) * main_diagonal_matrix(n, n, [[(-1)**(r+1+c+1) * calculate_determinant(n-1, calculate_matrix_M(n, matrix, r, c)) for c in range(n)] for r in range(n)])

def main():
    while True:
        choose = show_menu()
        if choose == 0:
            break
        elif choose == 1:
            choice_one()
            print()
            continue
        elif choose == 2:
            choice_two()
            print()
            continue
        elif choose == 3:
            choice_three()
            print()
            continue
        elif choose == 4:
            choice_four()
            print()
            continue
        elif choose == 5:
            choice_five()
            print()
            continue
        elif choose == 6:
            choice_six()
            print()
            continue

main()

