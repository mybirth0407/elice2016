import numpy

def matrix_tutorial(A):
    # 2
    B = A.transpose()

    C = None
    try:
        #3 - 1
        C = numpy.linalg.inv(B)
    except:
        #3 - 2
        return "not invertible"

    # 4
    return numpy.sum(C > 0)

def get_matrix():
    # 1
    mat = [] # define mat variable

    first_line = input().strip() # receice first line
    first_line_splitted = first_line.split(" ") # split line by space " "
    n = int(first_line_splitted[0]) # convert to integer
    m = int(first_line_splitted[1]) # convert to integer

    for i in range(n):
        line = input().strip() # receive each line ...
        row = line.split(" ")  # ... and split
        for j in range(m):
            row[j] = int(row[j]) # convert to integer
        mat.append(row)

    return numpy.array(mat)

if __name__ == "__main__":
    A = get_matrix()
    print(matrix_tutorial(A))
