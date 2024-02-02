import warnings

warnings.filterwarnings('ignore')


# Введите ваше решение ниже


class Matrix:

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0] * cols for _ in range(rows)]

    def __str__(self):
        matrix_str = "\n".join(" ".join(map(str, row)) for row in self.data)
        return matrix_str

    def __repr__(self):
        return f'Matrix({self.rows}, {self.cols})'

    def __eq__(self, other):
        if isinstance(other, Matrix):
            return self.rows == other.rows and self.cols == other.cols and self.data == other.data
        return False

    def __add__(self, other):
        if isinstance(other, Matrix) and self.rows == other.rows and self.cols == other.cols:
            result = Matrix(self.rows, self.cols)
            result.data = [[self.data[i][j] + other.data[i][j] for j in range(self.cols)] for i in range(self.rows)]
            return result
        else:
            raise ValueError("Matrices must have the same dimensions for addition.")

    def __mul__(self, other):
        if isinstance(other, Matrix) and self.cols == other.rows:
            result = Matrix(self.rows, other.cols)
            for i in range(self.rows):
                for j in range(other.cols):
                    result.data[i][j] = sum(self.data[i][k] * other.data[k][j] for k in range(self.cols))
            return result
        else:
            raise ValueError(
                "Number of columns in the first matrix must be equal to the number of rows in the second matrix for multiplication.")


# Создаем матрицы
matrix1 = Matrix(2, 3)
matrix1.data = [[1, 2, 3], [4, 5, 6]]

matrix2 = Matrix(2, 3)
matrix2.data = [[7, 8, 9], [10, 11, 12]]

# Выводим матрицы
print(matrix1)

print(matrix2)

# Сравниваем матрицы
print(matrix1 == matrix2)

# Выполняем операцию сложения матриц
matrix_sum = matrix1 + matrix2
print(matrix_sum)

# Выполняем операцию умножения матриц
matrix3 = Matrix(3, 2)
matrix3.data = [[1, 2], [3, 4], [5, 6]]

matrix4 = Matrix(2, 2)
matrix4.data = [[7, 8], [9, 10]]

result = matrix3 * matrix4
print(result)
