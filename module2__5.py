def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(value)
        matrix.append(row)
    return matrix
result1 = get_matrix(7,5,6)
result2 = get_matrix(3, 9, 4)
result3 = get_matrix(5, 4, 3)

print(result1)
print(result2)
print(result3)