target_num = int(input("enter tagrget number: "))
counter = 0

start_1, end_1 = int(input("First start: ")), int(input("First end: "))
start_2, end_2 = int(input("Second start: ")), int(input("Second end: "))
start_3, end_3 = int(input("Third start: ")), int(input("Third end: "))

if start_1 <= target_num <= end_1: counter += 1
if start_2 <= target_num <= end_2: counter += 1
if start_3 <= target_num <= end_3: counter += 1

print(counter)


"""
student name : Muhammad Khalaf Muhamamd
email : muhammadkhalaf195@gmail.com
"""