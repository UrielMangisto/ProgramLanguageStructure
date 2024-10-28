from functools import reduce
import time
from datetime import datetime, timedelta

# 1. Lambda for calculating values

# 1.1 Define lambda function
y = lambda x: x / 2 + 2

# 1.2 Function to calculate the sum of a list
def sum_of_lst(l):
    return sum(l)

# 1.3 Imperative sum calculation
def calc_imperative(x):
    total = 0
    for i in x:
        total += i
    return total

# 1.4 Calculate and sum using comprehension
def cal_and_sum():
    return sum(y(i) for i in range(10001))


# 2. Filtering and reducing lists

# 2.1 Define lambda functions for even and odd lists
even_lambda = lambda x, y: x * y
odd_lambda = lambda x, y: x / 2 + 2 + y

# 3. Date Generator
def get_dates(start_date_str, num_dates, day_skip):
    start_date = datetime.strptime(start_date_str, '%d-%m-%Y')
    date_list = list(map(lambda i: (start_date + timedelta(days=i * day_skip)).strftime('%d-%m-%Y'), range(num_dates)))
    return date_list


# 4. Power Functions

# 4.1 Function returning a power function with a specific exponent
def power_function(exponent):
    return lambda base: base ** exponent

# 4.2 Function returning map of power functions for a range
def power_functions(n):
    return map(lambda x: (lambda base: base ** x), range(n))

# 4.3 Taylor Series approximation of e^x
def taylor_approximation(x, n):
    powers = power_functions(n)
    factorials = map(lambda i: (lambda: 1 if i == 0 else reduce(lambda a, b: a * b, range(1, i + 1))), range(n))
    terms = map(lambda power, factorial: (lambda: (x ** power()) / factorial()), powers, factorials)
    return sum(map(lambda term: term(), terms))


# 5. Task Manager (Closure)
def task_manager():
    tasks = {}

    def add_task(task, status='incomplete'):
        tasks[task] = status

    def get_tasks():
        return tasks

    def complete_task(task):
        if task in tasks:
            tasks[task] = 'complete'

    return {
        'add_task': add_task,
        'get_tasks': get_tasks,
        'complete_task': complete_task
    }


# Main function to run all parts
if __name__ == "__main__":
    # 1. Lambda calculations
    lst = list(map(y, range(10001)))
    print("List after lambda calculation:", lst)

    print("Sum using sum_of_lst:", sum_of_lst(lst))
    start_time_reduce = time.time()
    result = sum_of_lst(lst)
    end_time_reduce = time.time()
    print("Execution time for sum_of_lst:", end_time_reduce - start_time_reduce)

    start_time_imperative = time.time()
    calc_by_for_loop = calc_imperative(lst)
    end_time_imperative = time.time()
    print("Execution time for calc_imperative:", end_time_imperative - start_time_imperative)

    print("Calculation and sum using comprehension:", cal_and_sum())

    # 2. Filter and reduce lists
    l = list(range(1, 1001))
    even_lst = list(filter(lambda x: x % 2 == 0, l))
    odd_lst = list(filter(lambda x: x % 2 != 0, l))

    even_result = reduce(even_lambda, even_lst)
    odd_result = reduce(odd_lambda, odd_lst)

    print("Result for even numbers:", even_result)
    print("Result for odd numbers:", odd_result)
    print("Total sum of both results:", even_result + odd_result)

    # 3. Date generation
    print("Generated dates:", get_dates('01-01-2024', 5, 7))

    # 4. Power and Taylor functions
    power_of_2 = power_function(2)
    print("Power of 2 applied to 3:", power_of_2(3))
    print("Power of 2 applied to 5:", power_of_2(5))

    power_funcs = power_functions(5)
    for i, func in enumerate(power_funcs):
        print(f"x^{i} for x = 2:", func(2))

    print("Taylor approximation of e^1 with 10 terms:", taylor_approximation(1, 10))

    # 5. Task Manager
    tasks_manager = task_manager()
    tasks_manager['add_task']("Write email")
    tasks_manager['add_task']("Shopping", "in progress")
    tasks_manager['add_task']("Homework")

    print("Task list:", tasks_manager['get_tasks']())
    tasks_manager['complete_task']("Write email")
    print("Updated task list:", tasks_manager['get_tasks']())
