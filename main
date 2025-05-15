from secure_password_manager import add_password, get_password, generate_key, validate_input
from getpass import getpass
from cryptography.fernet import Fernet
import os

if not os.path.exists('data'):
    os.makedirs('data')

if not os.path.exists('data/passwords.json'):
    with open('data/passwords.json', 'w') as f:
        f.write('{}')
def main():
    from getpass import getpass
    master_password = input("Ievadi meistara paroli")
    key = generate_key(master_password)
    fernet = Fernet(key)

    while True:
        print("\n1. Pievienot paroli\n2. Skatīt paroli\n3. Iziet")
        choice = input("Izvēlies: ")

        if choice == "1":
            site = input("Vietne: ")
            if not validate_input(site):
                print("Nederīga vietne.")
                continue
            username = input("Lietotājvārds: ")
            password = input("Parole: ")
            add_password(site, username, password, fernet)
            print("Parole saglabāta.")
        elif choice == "2":
            site = input("Vietne: ")
            result = get_password(site, fernet)
            if result:
                print(f"Lietotājvārds: {result['username']}, Parole: {result['password']}")
            else:
                print("Nav atrasts vai nepareiza meistara parole.")
        elif choice == "3":
            break
        else:
            print("Nederīga izvēle.")

if __name__ == "__main__":
    main()
