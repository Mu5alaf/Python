x, y, z = 20, 90, 20  

if x >= 100 and y >= 100 and z >= 100: 
    print(-1)
else:
    if x < 100 and (x > y or y >= 100) and (x > z or z >= 100):
        print(x)
    elif y < 100 and (y > x or x >= 100) and (y > z or z >= 100):
        print(y)
    else:
        print(z)

"""
happy case
22,90,100
20,20,20
1000, 90, 99
------------

unhappy case
-1 case
500,900,551
""" 


"""
student name : Muhammad Khalaf Muhamamd
email : muhammadkhalaf195@gmail.com
"""