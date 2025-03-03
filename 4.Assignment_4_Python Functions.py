
# EXERCISE 1

def calculate(a, b=10, c=None):
    if c is None:
        print(a + b)
    else:
        print(a * b * c)

calculate(10)

calculate(10,20)

calculate(10,20,30)

# EXERCISE 2

def filter_long_strings(strings):
    return [s for s in strings if len(s) >= 5]

words = ['Apple', 'Orange', 'Banana', 'Strawberry', 'Blueberry', 'kiwi']
result = filter_long_strings(words)
print(result)

# EXERCISE 3

expression = "3 * 5 + 2"
result = eval(expression)
print("Result:", result)

# EXERCISE 4

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = [20, 3, 5, 9, 13, 17, 120, 203, 300]
prime_numbers = list(filter(is_prime, numbers))

print("Prime numbers:", prime_numbers)

# EXERCISE 5

strings = ["cherry", "plum", "avocado", "dragon fruit"]

uppercase_strings = list(map(str.upper, strings))

print("Uppercase Strings:", uppercase_strings)


