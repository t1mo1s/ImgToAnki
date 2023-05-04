def showMenu():
    print(f"\n\n\nWelcome to the AnkiConnect program!")
    print("Please choose one of the following options:")
    print("1. Check if .txt File is arranged correctly")
    print("2. add .txt File to AnkiConnect")
    print("0. Exit the program")
    userChoice = input("Enter your choice: ")
    return int(userChoice)