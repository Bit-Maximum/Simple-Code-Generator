[print(x, end=' ') for x in range(2, 150) if all(x % i != 0 for i in range(2, int(x**0.5) + 1)) and x > 10]
