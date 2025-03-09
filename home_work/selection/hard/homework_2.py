start_1, end_1 = map(int,input("Enter First list: ").split())
start_2, end_2 = map(int,input("Enter First list: ").split())

if(end_1 < start_2 or end_2 < start_1):
    print(-1)
else:
    if start_1 > start_2:
        intersect_start = start_1
    else:
        intersect_start = start_2
        
    if end_1 < end_2:
        intersect_end = end_1
    else:
        intersect_end = end_2
    
    listed = intersect_start,intersect_end
    print(list(listed))

"""
Test 
0 3 & 2 4
-1 34 & 0 4
"""

"""
student name : Muhammad Khalaf Muhamamd
email : muhammadkhalaf195@gmail.com
"""