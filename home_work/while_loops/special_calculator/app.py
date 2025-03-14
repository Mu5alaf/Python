while True:
    print("Menu:")
    print("Enter 1 to sum Numbers from 1 to N")
    print("Enter 2 to sum evaluate simple 2 Numbers experssion (e.g. 2 + 3)")
    print("Enter 3 to end the program")

    operator_number = int(input("Enter choice From 1 to 3: "))

    #valdiat the operator
    if operator_number > 3:
        print(" Invaild Input ... Try agin \n")
    # first operator
    if operator_number == 1:
        num = int(input("Enter a Number: "))
        sum_counter = 1
        value = 0
        while sum_counter < num:
            value += sum_counter 
            sum_counter += 1
        print("Sum From 1 to",num,"is", value,"\n")

    #Second operator
    if operator_number == 2:
        first_num, operator,second_num = map(str,input("Enter a Simple experssion: ").split())
        first_value = float(first_num)
        second_value = float(second_num)
        if first_value and second_value != 0:
            if operator == '**':
                print (first_value ** second_value,"\n")
            if operator == '//':
                print (first_value // second_value,"\n")
            if operator == '/':
                print (first_value / second_value,"\n")
            if operator == '*':
                print (first_value * second_value,"\n")
            if operator == '+':
                print (first_value + second_value,"\n")
            if operator == '-':
                print (first_value - second_value,"\n")
        else:
            print("Sorry: No wat to compute this Experssion \n")
    #third operator
    if operator_number == 3:
        print("Bye...")
        break
    continue

