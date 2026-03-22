#Date: 2025-06-20
#Write a simple Python script that prints "Hello, World!" to the console.
print("Hello, World!")


#Swap two variables without using third variable
a = 5
b = 10
temp = a
a = b
b = temp    
print("a:", a, "b:", b)


#Check if a number is even or odd
num = 4
if num % 2 == 0:
    print(num, "is even")
else:
    print(num, "is odd")
    
        
#Find the largest of three numbers
a = 5
b = 10
c = 3
if a > b and a > c:
    print(a, "is the largest")
elif b > a and b > c:
    print(b, "is the largest")
else:
    print(c, "is the largest")

    
#Calculate the factorial of a number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
num = 5
print("Factorial of", num, "is", factorial(num))


#Check if a string is a palindrome
def is_palindrome(s):
    return s == s[::-1] 
s = "radar"
if is_palindrome(s):
    print(s, "is a palindrome")
else:
    print(s, "is not a palindrome")

    
#Reverse a string
def reverse_string(s):
    return s[::-1]
s = "hello"
print("Reverse of", s, "is", reverse_string(s))


#Find the sum of digits of a number
def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))
num = 12345
print("Sum of digits of", num, "is", sum_of_digits(num))


#Check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
num = 29
if is_prime(num):
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")

    
#Find the Fibonacci sequence up to n terms
def fibonacci(n):   
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence
n = 10
print("Fibonacci sequence up to", n, "terms is", fibonacci(n))      