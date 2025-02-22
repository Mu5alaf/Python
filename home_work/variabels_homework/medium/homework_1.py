"""
i traced the lines of the code like
we have num1 = 1 and num2 = 2

num3 = num1 + num2
num1 = num2
num2 = num3
so when we add num1 , num2  and assign this value to num3 will = 3
so now  
num3 = 3 , num1 = 2 , num2 = num3

and so on till we got 34 at after 6 times
"""

num1 = 1
num2 = 2

num3 = num1 + num2
num1 = num2
num2 = num3

num3 = num1 + num2
num1 = num2
num2 = num3

num3 = num1 + num2
num1 = num2
num2 = num3

num3 = num1 + num2
num1 = num2
num2 = num3

num3 = num1 + num2
num1 = num2
num2 = num3

num3 = num1 + num2
num1 = num2
num2 = num3

print(num2)



"""
student name : Muhammad Khalaf Muhamamd
email : muhammadkhalaf195@gmail.com
"""