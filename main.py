def options():
    while True:
        print('Main Menu')
        print('1. String Operation')
        print('2. Number Operation')
        print('3. Exit \n \n')

        useInput = input('Enter your options:(1, 2 or 3)  ')
        if(useInput == '1'):
            print('You choose "String Operaion" \n')
        elif(useInput == '2'):
            print('You choose "Number Operaion" \n')
        elif(useInput == '3'):
            print('Exit from program \n')
            break
        else:
            print('Invalid Options \n')

options()