# ask user for input 
import pyjokes

def helper_Agent():
    print('Hello there, how can i help You For Math enter 1 for random Jok perss 2')
    commend = input()
    try:
        if commend == '1':
            print('Wellcom to Callculator Agent enter Your Firts number\n')
            num_a = int(input())
            print('Please Choise the type of operation that you want to do\n')
            operation= input('+ , - , * , / \n')
            num_b = int(input('So now enter Your second Number\n'))
            #operations
            sub = num_a - num_b
            add = num_a + num_b
            div = num_a / num_b
            muill = num_a * num_b
            try:
                if operation == '+':
                    result = add
                elif operation == '-':
                    result = sub
                elif operation == '*':
                    result = muill
                elif operation == '/':
                    if num_b == 0:
                        raise ZeroDivisionError
                    result = num_a / num_b
                else:
                    print('Oop failed')
                print(f"we got {result}")
            except:
                raise ValueError
        
        elif commend == '2':
            print(pyjokes.get_joke())
        else:
            print(f'Only options are 1 or 2, I don\'t understand "{commend}"')
    except:
        return ('error')
    
helper_Agent()
