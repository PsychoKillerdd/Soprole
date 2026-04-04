def fibonacci(n):
    count = 0
    a, b = 0, 1
    while count < n:
        print(a, end = ' ')
        a, b = b, a + b
        count += 1


fibonacci(20)