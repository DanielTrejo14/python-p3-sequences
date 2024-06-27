#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0:
        print([])
        return
    elif length == 1:
        print([0])
        return

    fibonacci = [0, 1]  # Initialize the Fibonacci sequence with the first two numbers
    for i in range(2, length):
        fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])  # Calculate the next Fibonacci number
    print(fibonacci) 