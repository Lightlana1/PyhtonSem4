# Напишите функцию для транспонирования матрицы
def tranponse_matrix(matrix: list[list]) -> list[list]:
    trans_matrix = list(map(list, zip(*matrix)))

    return trans_matrix

matrix = [
    [1, 1, 1, 1],
    [2, 2, 2, 2],
    [3, 3, 3, 3],
    [4, 4, 4, 4],
]

print(tranponse_matrix(matrix))
