# Simple Calculator

while True: 
    user_input = input('Enter the first number: ')
    user_input2 = input('Enter the second number: ')
    user_operation = input('Enter the operation you would want to calculate: (exit) ')
    if user_operation == 'exit':  
        print('Exiting the calculator.')
        break
    elif user_operation == '+' or user_operation == 'add':
        print('Result: ', int(user_input) + int(user_input2))
    elif user_operation == '-' or user_operation == 'sub':
        print('Result: ', int(user_input) - int(user_input2))
    elif user_operation == '*' or user_operation == 'mul':
        print('Result: ', int(user_input) * int(user_input2))
    elif user_operation == '/' or user_operation == 'div':
        if int(user_input2) == 0:
            print('Error: Division by zero is not allowed.')
        else:
            print('Result: ', int(user_input) / int(user_input2))
    else:
        print('Invalid operation. Please try again.')
    
