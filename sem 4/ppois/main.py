from MainMenu import MainMenu
from webapp.app import app

def main():
    user_input = input("Enter '1' for Main Menu or '2' to run the app: ")

    if user_input == '1':
        MainMenu.main_menu()
    elif user_input == '2':
        app.run()
    else:
        print("Invalid input. Please enter '1' or '2'.")

if __name__ == "__main__":
    main()
