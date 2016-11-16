def matrix_scale(mat,num):
    '''
    (list, int) --> (list)
    Given a matrix and an integer, return the matrix multiplied
    by the the scalar integer.
    '''
    
    for i in range(len(mat)): #Iterates through each row in 'mat'.
        for j in range(len(mat[0])): #Iterates through each column in 'mat'.
            mat[i][j] = mat[i][j] * num
    return mat

def matrix_sum(mat1,mat2):
    '''
    (list, list) --> (list or None)
    Given two matrices, return the sum of the two matrices. Return None if the
    sum cannot be calculated.
    '''
    
    if (len(mat1) != len(mat2)) or (len(mat1[0]) != len(mat2[0])):
    #Condition ensures same dimensions.
        return None
    new_matrix = []
    for i in range(len(mat1)): #Iterates through each row in 'mat1'.
        row = []
        for j in range(len(mat1[0])): #Iterates through each column in 'mat1'.
            row.append(mat1[i][j] + mat2[i][j])
        new_matrix.append(row)
    return new_matrix

def matrix_sym(mat):
    '''
    (list) --> (True or None)
    Given a matrix, determine whether the matrix is symmetrical. Return None if
    matrix is not square. Return True if matrix is symmetrical. 
    '''
    
    if len(mat) != len(mat[0]):
        return None
    for i in range(len(mat)): #Iterates through each row in 'mat1'.
        for j in range(len(mat)): #Iterates through each column in 'mat1'.
            if mat[i][j] == mat[j][i]: #Condition to ensure symmetrical nature.
              continue
            else:
              return False
    return True
            
def matrix_mul(mat1,mat2):
    '''
    (list, list) --> (list)
    Given two matrices, return the multiplication of mat1 and mat2. Return None
    if matrix multiplication is not possible.
    '''
    
    if len(mat1[0]) != len(mat2):
        return None
    new_matrix = []
    for j in range(len(mat1)): #Iterates through each row in 'mat1'.
        row = []
        for i in range(len(mat2[0])): #Iterates through each column in 'mat2'.
            sum = 0
            for k in range(len(mat2)):
            #Iterates through each row in column 'i' in 'mat2'.
                sum += mat1[j][k]*mat2[k][i]
            row.append(sum)
        new_matrix.append(row)
    return new_matrix

def column_sum_square(mat):
    '''
    (list) --> (list)
    Given a matrix, return a row vector with the sum of the elements in their
    respective columns.
    '''
    
    new_matrix = []
    for i in range(len(mat[0])):
        sum = 0
        for j in range(len(mat)):
            sum += (mat[j][i])**2
        new_matrix.append(sum)
    return new_matrix
