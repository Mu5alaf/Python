"""Sol 1"""

x = 10
a, b ,c ,d ,e = 300, 1, 5, 100, 200

more_than_x, less_than_x = 0 , 0

if a <= 10:
    less_than_x += 1
if a > x:
    more_than_x += 1
if b <= x:
    less_than_x +=1
if b > x:
    more_than_x +=1
if c <= x:
    less_than_x +=1
if c > x:
    more_than_x +=1
if d <= x:
    less_than_x +=1
if d > x:
    more_than_x +=1
if e <= x:
    less_than_x +=1
if e > x:
    more_than_x +=1

print(less_than_x, more_than_x)


"""Sol 2"""
x = 10
a, b ,c ,d ,e = 300, 1, 5, 100, 200

more_than_x, less_than_x = 0 , 0

if a > x: more_than_x += 1
else: less_than_x += 1

if b > x: more_than_x += 1
else: less_than_x += 1

if c > x: more_than_x += 1
else: less_than_x += 1

if d > x: more_than_x += 1
else: less_than_x += 1

if e > x: more_than_x += 1
else: less_than_x += 1
    
print(less_than_x, more_than_x)


"""
student name : Muhammad Khalaf Muhamamd
email : muhammadkhalaf195@gmail.com
"""