start, end = map(int,input('Enter The start and The end number: ').split())
if start >= end:
    counter = start
    while counter >= end:
        print(counter)
        counter -= 1
else:
    counter = start
    while counter <= end:
        print(counter)
        counter += 1
"""
test case
1 5
5 5
-1 20
0 -100
"""

"""
student name : Muhammad Khalaf Muhamamd
email : muhammadkhalaf195@gmail.com
"""