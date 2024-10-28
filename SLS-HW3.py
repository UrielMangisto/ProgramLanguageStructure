import time
import sys
import math


# מגדיל את גבול הרקורסיה
sys.setrecursionlimit(1500)

# שאלה 1.1 - יצירת tuple של המספרים 1-1000 באמצעות רקורסיה רגילה
def create_tuple_regular(n):
    if n == 1:
        return (1,)
    return create_tuple_regular(n - 1) + (n,)

# שאלה 1.1 - יצירת tuple של המספרים 1-1000 באמצעות רקורסיה זנבית
def create_tuple_tail(n):
    def helper(current, acc):
        if current > n:
            return acc
        return helper(current + 1, acc + (current,))
    return helper(1, ())

# שאלה 1.2 - סכום איברי מערך באמצעות רקורסיה רגילה
def sum_array_regular(arr):
    if not arr:
        return 0
    return arr[0] + sum_array_regular(arr[1:])


# שאלה 1.2 - סכום איברי מערך באמצעות רקורסיה זנבית
def sum_array_tail(arr, acc=0):
    if not arr:
        return acc
    return sum_array_tail(arr[1:], acc + arr[0])


# שאלה 1.3 - חישוב LCM (מכפיל משותף מינימלי)
# Regular recursion
def gcd_recursive(a, b):
    if b == 0:
        return a
    return gcd_recursive(b, a % b)


def lcm_recursive(a, b):
    return (a * b) // gcd_recursive(a, b)

# Tail recursion
def gcd_tail_recursive(a, b):
    def gcd_helper(a, b):
        if b == 0:
            return a
        return gcd_helper(b, a % b)
    return gcd_helper(abs(a), abs(b))


def lcm_tail_recursive(a, b):
    return abs(a * b) // gcd_tail_recursive(a, b)


# שאלה 1.4 - בדיקת פלינדרום
def is_palindrome(num):
    num_str = str(num)
    if len(num_str) <= 1:
        return True
    return num_str[0] == num_str[-1] and is_palindrome(int(num_str[1:-1]))


# Tail recursion
def is_palindrome_tail(num):
    def isPalindrome_helper(s, start, end):
        # Base case: we've checked all digits or crossed over
        if start >= end:
            return True

        # If the digits don't match, it's not a palindrome
        if s[start] != s[end]:
            return False

        # Recursive case: check the next pair of digits
        return isPalindrome_helper(s, start + 1, end - 1)

    # Convert the number to a string and start the recursive helper
    return isPalindrome_helper(str(num), 0, len(str(num)) - 1)


# שאלה 1.5 - מיון וזיפ של רשימות
# Regular recursion
def sortedzip(lists):
    # Base case: if the list is empty, return an empty list
    if not lists:
        return []

    # Sort each sublist
    sorted_lists = [sorted(sublist) for sublist in lists]

    # Get the first elements of each sorted sublist
    first_elements = [sublist[0] if sublist else None for sublist in sorted_lists]

    # Recursive call with the rest of the elements
    rest = sortedzip([sublist[1:] for sublist in sorted_lists if sublist])

    # Combine the first elements with the rest
    return [tuple(first_elements)] + rest


# Tail recursion
def sortedzip_tail(lists):
    def helper(sorted_lists, acc):
        # If all sublists are empty, return the accumulated result
        if all(not sublist for sublist in sorted_lists):
            return acc

        # Get the first elements of each non-empty sublist
        first_elements = [sublist[0] if sublist else None for sublist in sorted_lists]

        # Create new sorted_lists without the first elements
        new_sorted_lists = [sublist[1:] if sublist else [] for sublist in sorted_lists]

        # Recursive call with updated lists and accumulated result
        return helper(new_sorted_lists, acc + [tuple(first_elements)])

    # Sort each sublist first
    sorted_lists = [sorted(sublist) for sublist in lists]

    # Start the recursion with empty accumulator
    return helper(sorted_lists, [])

# שאלה 2.1 - יצירת מערך 0-10000 ללא lazy evaluation
def create_array_eager():
    start_time = time.time()
    array = list(range(10001))
    end_time = time.time()

    execution_time = end_time - start_time
    memory_size = sys.getsizeof(array)

    print(f"Eager execution time: {execution_time:.6f} seconds")
    print(f"Eager memory size: {memory_size} bytes")
    return array


# שאלה 2.1 - יצירת מערך 0-10000 עם lazy evaluation
def create_array_lazy():
    start_time = time.time()
    lazy_array = range(10001)
    end_time = time.time()

    execution_time = end_time - start_time
    memory_size = sys.getsizeof(lazy_array)

    print(f"Lazy execution time: {execution_time:.6f} seconds")
    print(f"Lazy memory size: {memory_size} bytes")
    return lazy_array


# שאלה 2.1 - יצירת 5000 האיברים הראשונים
def create_first_5000(array):
    start_time = time.time()
    first_5000 = list(array[:5000])
    end_time = time.time()

    execution_time = end_time - start_time
    memory_size = sys.getsizeof(first_5000)

    print(f"First 5000 execution time: {execution_time:.6f} seconds")
    print(f"First 5000 memory size: {memory_size} bytes")
    return first_5000


# שאלה 2.2 - גנרטור למספרים ראשוניים
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def prime_generator():
    n = 2
    while True:
        if is_prime(n):
            yield n
        n += 1


# שאלה 2.3 - חישוב טור טיילור עבור e^x
def taylor_series_e_x(x):
    n = 0
    factorial = 1
    while True:
        term = (x ** n) / factorial
        yield term
        n += 1
        factorial *= n


def calculate_e_x(x, num_terms):
    generator = taylor_series_e_x(x)
    sum_result = 0
    for _ in range(num_terms):
        sum_result += next(generator)
        yield sum_result


if __name__ == "__main__":
    # דוגמאות שימוש

    print("שאלה 1.1 - יצירת tuple של המספרים 1-1000:")
    regular_tuple = create_tuple_regular(1000)
    tail_tuple = create_tuple_tail(1000)

    print(f"אורך ה-tuple הרגיל: {len(regular_tuple)}")
    print(f"10 האיברים הראשונים של ה-tuple הרגיל: {regular_tuple[:10]}")
    print(f"10 האיברים האחרונים של ה-tuple הרגיל: {regular_tuple[-10:]}")

    print(f"\nאורך ה-tuple הזנבי: {len(tail_tuple)}")
    print(f"10 האיברים הראשונים של ה-tuple הזנבי: {tail_tuple[:10]}")
    print(f"10 האיברים האחרונים של ה-tuple הזנבי: {tail_tuple[-10:]}")

    print("\nשאלה 1.2 - סכום איברי מערך:")
    test_array = tail_tuple
    print(f"סכום: {sum_array_regular(test_array)}")
    print(f"סכום (זנבי): {sum_array_tail(test_array)}")

    print("\nשאלה 1.3 - חישוב LCM:")
    print(lcm_recursive(4, 6))  # Output: 12
    print(lcm_tail_recursive(4, 6))  # Output: 12

    print("\nשאלה 1.4 - בדיקת פלינדרום:")
    print(is_palindrome(123454321))  # Output: True
    print(is_palindrome(12345))  # Output: False
    print(is_palindrome_tail(123454321))  # Output: True
    print(is_palindrome_tail(12345))  # Output: False

    print("\nשאלה 1.5 - מיון וזיפ של רשימות:")
    input_lists = [[3, 1, 2], [5, 6, 4], ['a', 'b', 'c']]
    print(list(sortedzip(input_lists)))
    print(list(sortedzip_tail(input_lists)))
    # Expected output for both: [(1, 4, 'a'), (2, 5, 'b'), (3, 6, 'c')]

    print("\nשאלה 2.1 - יצירת מערכים:")
    eager_array = create_array_eager()
    lazy_array = create_array_lazy()
    first_5000_eager = create_first_5000(eager_array)
    first_5000_lazy = create_first_5000(lazy_array)

    print(f"\nסוג המערך הרגיל: {type(eager_array)}")
    print(f"סוג המערך העצלן: {type(lazy_array)}")
    print(f"סוג 5000 הראשונים מהרגיל: {type(first_5000_eager)}")
    print(f"סוג 5000 הראשונים מהעצלן: {type(first_5000_lazy)}")

    print("\nשאלה 2.2 - גנרטור למספרים ראשוניים:")
    primes = prime_generator()
    print("10 המספרים הראשוניים הראשונים:")
    for _ in range(10):
        print(next(primes), end=" ")

    print("\n\nשאלה 2.3 - חישוב טור טיילור עבור e^2:")
    x = 2
    for i, approximation in enumerate(calculate_e_x(x, 7), 1):
        print(f"קירוב {i}: {approximation}")
    print(f"הערך האמיתי של e^2: {math.exp(2)}")