import numpy

def matrix_tutorial():
    A = numpy.array([[1,4,5,8], [2,1,7,3], [5,4,5,9]])
    # 1
    B = A.reshape(6, 2)
    # 2
    B = numpy.concatenate((B, numpy.array([[2, 2], [5, 3]])), axis=0)
    # 3
    slice_Y_equal_size = numpy.split(B, 2, axis=0)
    C = slice_Y_equal_size[0]
    D = slice_Y_equal_size[1]
    # 4
    E = numpy.concatenate((C, D), axis=1)
    # 5
    return E

print(matrix_tutorial())
