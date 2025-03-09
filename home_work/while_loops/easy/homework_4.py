n = int(input(""))
counter = 1
odd_sum = 0
even_sum = 0
odd_count = 0
even_count = 0
while counter <= n:
    num = int(input(": "))
    if counter %2 == 0:
        odd_sum += num
        odd_count +=1
    else:
        even_sum += num
        even_count += 1
    
    counter += 1

odd_avarage = float(odd_sum / odd_count)
even_avarage = float(even_sum /even_count)

print(even_avarage,odd_avarage)

"""
student name : Muhammad Khalaf Muhamamd
email : muhammadkhalaf195@gmail.com
"""