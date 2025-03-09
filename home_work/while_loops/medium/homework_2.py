N = int(input())
counter = 0
num = 0
while counter <= N:
    if (counter % 8 == 0) or (counter % 4 == 0 and counter % 3 == 0):
        print(counter)
    counter += 1


"""
student name : Muhammad Khalaf Muhamamd
email : muhammadkhalaf195@gmail.com
"""