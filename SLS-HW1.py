# 1. Pentagon Number Functions

# Function to calculate the nth pentagonal number
def get_penta_num(n):
    return n * (3 * n - 1) // 2

# Function to calculate a list of pentagonal numbers in a range
def penta_num_range(n1, n2):
    return list(map(get_penta_num, range(n1, n2)))


# 2. Sum of Digits Function

# Function to sum digits of a number
def sum_digit(n):
    return sum(map(int, str(n)))


# 3. Gematria Calculation

# Dictionary of gematria values
gematria_dict = {
    'א': 1, 'ב': 2, 'ג': 3, 'ד': 4, 'ה': 5, 'ו': 6, 'ז': 7, 'ח': 8, 'ט': 9, 'י': 10,
    'כ': 20, 'ל': 30, 'מ': 40, 'נ': 50, 'ס': 60, 'ע': 70, 'פ': 80, 'צ': 90, 'ק': 100,
    'ר': 200, 'ש': 300, 'ת': 400
}

# Function to calculate gematria value of a Hebrew word
def gematria(s):
    return sum(map(lambda c: gematria_dict.get(c, 0), s))


# 4. Prime Number Functions

# Function to check if a number is prime
def is_prime(n):
    return n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))

# Function to find twin prime of a prime number if exists
def twin_prime(n):
    if is_prime(n):
        if is_prime(n - 2):
            return n - 2
        if is_prime(n + 2):
            return n + 2
    return None

# Function to create a dictionary of primes and their twin primes
def dict_prime(n):
    return {i: twin_prime(i) for i in range(2, n + 1) if is_prime(i)}


# 5. Add Three Dictionaries

# Lambda function to merge three dictionaries by key with unique values in tuples
add3dicts = lambda d1, d2, d3: {k: tuple(set(d[k] for d in (d1, d2, d3) if k in d)) for k in set(d1) | set(d2) | set(d3)}


# 6. Apply Functions to List of Numbers

# Individual functions for testing
def square(x):
    return x ** 2

def double(x):
    return x * 2

def inverse(x):
    return 1 / x

# Function to apply a list of functions to a list of numbers
def apply_functions(funcs, numbers):
    results = {}
    for f in funcs:
        results[f.__name__] = list(map(f, numbers))
    return results


# Main section to run and display each function's output
if __name__ == "__main__":
    # 1. Pentagon Number Functions
    print("Pentagonal number of 2:", get_penta_num(2))
    print("Pentagonal numbers from 1 to 3:", penta_num_range(1, 3))

    # 2. Sum of Digits Function
    print("Sum of digits in 115:", sum_digit(115))

    # 3. Gematria Calculation
    print("Gematria of 'בדיקה':", gematria("בדיקה"))

    # 4. Prime Number Functions
    print("Is 5 prime?", is_prime(5))
    print("Twin prime of 5:", twin_prime(5))
    print("Dictionary of primes with twin primes up to 13:", dict_prime(13))

    # 5. Add Three Dictionaries
    d1 = {'a': 1, 'b': 2, 'c': 3}
    d2 = {'b': 2, 'c': 30, 'd': 40}
    d3 = {'c': 300, 'd': 4, 'e': 500}
    print("Merged dictionary:", add3dicts(d1, d2, d3))

    # 6. Apply Functions to List of Numbers
    functions_list = [square, double, inverse]
    numbers = [1, 2, 3, 4, 5]
    print("Applied functions result:", apply_functions(functions_list, numbers))
