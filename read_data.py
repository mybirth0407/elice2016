import numpy

def main():
    (N, X, Y) = read_data()
    print(N)
    print(X)
    print(Y)

def read_data():
    # Implement here
    N = int(input())
    X = []
    Y = []
    for i in range(N):b
        input_data = input().strip().split(' ')
        X.append(float(input_data[0]))
        Y.append(float(input_data[1]))

    return (N, X, Y)

if __name__ == "__main__":
    main()
