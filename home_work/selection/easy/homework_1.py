num_1 = 2
num_2 = 0

if num_1 % 2 != 0 and num_2 % 2 != 0 :
    print(num_1 * num_2)
elif num_1 % 2 == 0 and num_2 % 2 == 0 :
    if num_1 and num_2 != 0:
        print(num_1 / num_2)
    else:
        print("Zero Division Error")
elif num_1 % 2 != 0 and num_2 % 2 == 0:
    print(num_1 + num_2)
elif num_1 % 2 == 0 and num_2 % 2 != 0:
    print(num_1 - num_2)
else:
    print("OK")

"""
test numbers:
1 8
8 5
5 5
8 8
"""
"""
student name : Muhammad Khalaf Muhamamd
email : muhammadkhalaf195@gmail.com
"""
<<<<<<< HEAD

=======
>>>>>>> refs/remotes/origin/main
