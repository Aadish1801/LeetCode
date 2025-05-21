class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # Get the dimensions of the matrix
        nrows, ncols = len(matrix), len(matrix[0])

        # Determine if the first row has any zeroes
        first_row_has_zero = any(value == 0 for value in matrix[0])
        # Determine if the first column has any zeroes
        first_col_has_zero = any(matrix[row][0] == 0 for row in range(nrows))

        # Use the first row and column as flags for zeroes
        # Start from 1 to avoid overwriting the first row and column flags
        for row in range(1, nrows):
            for col in range(1, ncols):
                # If an element is zero, mark its row and column in the first row and column
                if matrix[row][col] == 0:
                    matrix[row][0] = matrix[0][col] = 0

        # Set matrix elements to zero based on flags in the first row and column,
        # ignoring the first row and column themselves
        for row in range(1, nrows):
            for col in range(1, ncols):
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0

        # If the first row had zeroes, set all elements in the first row to zero
        if first_row_has_zero:
            for col in range(ncols):
                matrix[0][col] = 0

        # If the first column had zeroes, set all elements in the first column to zero
        if first_col_has_zero:
            for row in range(nrows):
                matrix[row][0] = 0