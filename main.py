from libs import welcome_message, exit_program
from games import cuypy
from tools import warung
    
def menu():
    user_options = int(input(f'\n\nSilahkan pilih menu Programnya:\n1. CUYPY Games\n2. Warung Mini\n3. Keluar Program\n\nSilahkan pilih:  '))
    
    if user_options == 1:
        cuypy.start()
    elif user_options == 2:
        warung.start()
    elif user_options == 3:
        exit_program()
    else:
        print('Maaf, menu tidak tersedia')
    
    
def main():
    welcome_message()
    menu()
    exit_program()

if __name__ == "__main__":
    main()



