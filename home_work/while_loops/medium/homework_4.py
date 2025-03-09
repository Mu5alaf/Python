cases_number = int(input("Test Case number: "))
counter = 0
while counter < cases_number:
    N = int(input("Test Case Input range: "))
    min_value = int(input(":"))
    n_counter = 1
    while n_counter < N:
        num = int(input(":"))
        if num > min_value:
            num = min_value
        n_counter += 1
    print("Min Value is : ", num)
    counter += 1

"""
student name : Muhammad Khalaf Muhamamd
email : muhammadkhalaf195@gmail.com
"""