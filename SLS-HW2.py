from functools import reduce
import time
from datetime import datetime, timedelta
import math

#1

y = lambda x: x/2 + 2

#1.1

lst = list(map(y, range(10001)))
print(lst)

#1.2


def sum_of_lst(l):
    return sum(l)


print(sum_of_lst(lst))

#1.3


def calc_imperative(x):
    total = 0
    for i in x:
        total += i
    return total


start_time_reduce = time.time()  # התחלת מדידת הזמן
result = sum_of_lst(lst)
end_time_reduce = time.time()  # סיום מדידת הזמן

execution_time_reduce = end_time_reduce - start_time_reduce

start_time_imperative = time.time()  # התחלת מדידת הזמן
calc_by_for_loop = calc_imperative(lst)
end_time_imperative = time.time()  # סיום מדידת הזמן

execution_time_imperative = end_time_imperative - start_time_imperative
print(execution_time_reduce)
print(end_time_imperative)


def cal_and_sum():
    return sum(y(i) for i in range(10001))


print(cal_and_sum())


#2

l = [i for i in range(1, 1000)]

even_lst = [x for x in l if x % 2 == 0]  # מספרים זוגיים
odd_lst = [x for x in l if x % 2 != 0]    # מספרים אי-זוגיים

#2.1
# פונקציית למבדה עבור רשימת המספרים הזוגיים
even_lambda = lambda x, y: x * y

# פונקציית למבדה עבור רשימת המספרים האי-זוגיים
odd_lambda = lambda x, y: x/2 + 2 + y

#2.2
# הרצת הפונקציה המתאימה על כל אחת מהרשימות
even_result = int(reduce(even_lambda, even_lst))
odd_result = int(reduce(odd_lambda, odd_lst))

print("תוצאת הפעולה על המספרים הזוגיים:", even_result)
print("תוצאת הפעולה על המספרים האי-זוגיים:", odd_result)

#2.3
# סכימת התוצאות
total_sum = even_result + odd_result
print("הסכום הכולל של שתי התוצאות:", total_sum)


#3
def get_dates(start_date_str, num_dates, day_skip):
    # המרה של התאריך מ-String ל- datetime
    start_date = datetime.strptime(start_date_str, '%d-%m-%Y')

    # שימוש ב-map והגדרת פונקציה על כדי להוסיף ימים לכל תאריך
    date_list = list(map(lambda i: (start_date + timedelta(days=i * day_skip)).strftime('%d-%m-%Y'), range(num_dates)))

    return date_list


# דוגמה לשימוש בפונקציה
print(get_dates('01-01-2024', 5, 7))  # מחזיר 5 תאריכים, כל אחד במרווח של 7 ימים


# 4
# א. פונקציה המקבלת מעריך חזקה ומחזירה פונקציה לחישוב החזקה
def power_function(exponent):
    return lambda base: base ** exponent


# דוגמה לשימוש
power_of_2 = power_function(2)
print(power_of_2(3))  # מדפיס 9
print(power_of_2(5))  # מדפיס 25


# ב. פונקציה המחזירה אובייקט map של פונקציות חזקה
def power_functions(n):
    return map(lambda x: (lambda base: base ** x), range(n))


# דוגמה לשימוש
power_funcs = power_functions(5)
for i, func in enumerate(power_funcs):
    print(f"x^{i}: {func(2)}")  # מדפיס תוצאות עבור x = 2


# פונקציה להחזרת קירוב טיילור עבור e^x
def taylor_approximation(x, n):
    # יצירת חזקות של x ופקטוריאלים עד הדרגה המבוקשת
    powers = [x ** i for i in range(n)]
    factorials = [math.factorial(i) for i in range(n)]

    # חישוב הסכום של כל איבר בקירוב טיילור
    terms = [(powers[i] / factorials[i]) for i in range(n)]
    return sum(terms)


# דוגמה לשימוש
print(taylor_approximation(1, 10))  # קירוב של e^1


# 5 מנהל משימות (closure)
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


# דוגמה לשימוש
tasks_manager = task_manager()
tasks_manager['add_task']("Write email")
tasks_manager['add_task']("Shopping", "in progress")
tasks_manager['add_task']("Homework")

print(tasks_manager['get_tasks']())
tasks_manager['complete_task']("Write email")
print(tasks_manager['get_tasks']())