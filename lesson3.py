def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))

# def sum(n, n1):
#     if n == n1:
#         return n*2
#     if n == 0:
#         return n1
#     if n1 == 0:
#         return n 
#     else:
#         return (n+n1)
    
# def sum_of_numbers(n0, n1):
#     if n0 == n1:
#         return n0*2
#     if n0 > n1:
#         return n0 + sum_of_numbers(n0-1, n1)
#     else:
#         return n1 + sum_of_numbers(n0, n1-1)
    
# print(sum(1, 5))

def sumOfNumber(n):
    if n == 1 or n == 0:
        return n
    else:
        return n + sumOfNumber(n-1)
print(sumOfNumber(6))