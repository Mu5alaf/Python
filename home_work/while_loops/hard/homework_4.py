test_case = int(input("Number of Test Cases: "))
test_case_counter = 0

while test_case_counter < test_case:
    n_length = int(input("Number of N: "))
    n_number_counter = 0
    total_sum = 0
    
    while n_number_counter < n_length:
        n_number = int(input(": "))
        product = 1
        m_counter = 0
        exponent = n_number_counter + 1
        while m_counter < exponent:
            product *= n_number
            m_counter += 1
        
        total_sum += product
        n_number_counter += 1
        
    print("Total Sum:", total_sum)
    test_case_counter += 1

"""
student name : Muhammad Khalaf Muhamamd
email : muhammadkhalaf195@gmail.com
"""
