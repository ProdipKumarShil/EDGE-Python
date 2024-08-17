import re

def main_menu():
    print("MAIN MENU")
    print("1. String Operation")
    print("2. Number Operation")
    print("3. EXIT")

def fnEmailValidation(email):
    if re.match(f"[^@]+@[^@]+\.[^@]+", email):
        return True
    return False

def createPyramid(n):
    for i in range(0, n):
        print("#" * i)
    for i in range(n, 0, -1):
        print('#' * i)

def write_lines_to_file(filename):
    lines =[]
    print("Enter multiple line of text (type 'DONE' on a new line to finish):")
    while True:
        line = input()
        if line.strip().upper()=="DONE":
            break
        lines.append(line)
    with open(filename, "w") as file:
        for line in lines:
            file.write(line + "\n")
        print(f"File [{filename}] has been saved successfully!")



def main():
    while (True):
        main_menu()
        choice = input('\nEnter choice(1, 2 or 3): ')
        if choice == '1':
            while True:
                rchoice = input('Choice(1-> EmailValidation,2->Exit): ')
                print()
                if rchoice == '1':
                    email = input("\nEnter an email address: ")
                    if (fnEmailValidation(email)) is True:
                        print(f"\nProvided email address [{email}] is valid")
                    else:
                        print(f"\nProvided email address [{email}] not valid")

                elif rchoice == '2':
                    n = int(input("How many number?"))
                    createPyramid(n)

                elif rchoice == '3':
                    filename = "output2.txt"
                    write_lines_to_file(filename)
                else:
                    print('\n Invalid input !!!')
                    break

        elif choice == '2':
            print('\nThank you for choosing number operation.')

        elif choice == '3':
            print('\nThanks for using Switch Statements')
            break
        else:
            print('\nInvalid input!!!')


main()