x, y, z = 0,45.2,45.1

if x < y:
    if x < z:
        small = x
        if y < z:
            middle = y
            big = z
        else:
            middle = z
            big = y
    else:
        small = z
        middle = x
        big = y
else:
    if y < z:
        small = y
        if x < z:
            middll = x
            big = z
        else:
            midell = z
            big = x
    else:
        small = z
        midell = y
        big = y
    
print(small,middle,big)

"""
test numbers:
0,45.2,45.1
1 , 5 , 10
"""

"""
student name : Muhammad Khalaf Muhamamd
email : muhammadkhalaf195@gmail.com
"""