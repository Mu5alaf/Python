N = int(input(""))
counter = 1
while counter < N:
    space = N - counter
    print(' ' * space, end="")
    stars = 2 * counter -1
    print('*' * stars)
    counter += 1 
    
counter = N - 1
while counter >= 1:
    space = N - counter
    print(' ' * space, end="")
    stars = 2 * counter -1
    print('*' * stars)
    counter -= 1 


"""
student name : Muhammad Khalaf Muhamamd
email : muhammadkhalaf195@gmail.com
"""