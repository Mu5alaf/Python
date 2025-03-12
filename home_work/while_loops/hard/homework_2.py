N = int(input(": "))
R = 0
temp = N

while temp > 0:
    digit = temp % 10
    R = R * 10 + digit
    temp //= 10
print(R,R * 3)


"""
student name : Muhammad Khalaf Muhamamd
email : muhammadkhalaf195@gmail.com
"""