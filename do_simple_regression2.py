import io
import numpy
import statsmodels.api

def main():
    (N, X, Y) = read_data()
    results = do_simple_regression(N, X, Y)
    print(results.summary())

def read_data():
    # 1
    # Copy-and-paste your code from the previous exercise
    N = int(input())
    X = []
    Y = []
    for x in range(N):
        input_data = input().strip().split(' ')
        X.append(int(input_data[0]))
        Y.append(int(input_data[1]))

    return (N, X, Y)

def do_simple_regression(N, X, Y):
    # 2
    # Copy-and-paste your code from the previous exercise
    X = numpy.array(X).T
    X = statsmodels.api.add_constant(X)
    results = statsmodels.api.OLS(Y, X).fit()

    return results

if __name__ == "__main__":
    main()
