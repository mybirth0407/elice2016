#1
def sum_even_numbers(start, end):
    sum = 0
#2
    for x in range(start, end + 1):
        if x % 2 == 0:
            sum += x
    return sum

print(sum_even_numbers(1, 10))
