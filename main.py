import pyfiglet #module for the ASCII banner
import os #module to execute commands
import getpass #module for password input
import bcrypt #module for password encryption
import regex #module for regular expressions
import sys # module for iformation about constants, functions and methods of the Python interpreter
import hashlib #module for hashing
from cryptography.fernet import Fernet #module for password encryption

options = ["Strength Meter", "Password Encryption", "Hashing", "Tips", "Exit"]

ascii_banner = pyfiglet.figlet_format("KeyWord") #defining ASCII banner for main
SM_banner = pyfiglet.figlet_format("Strength Meter") #defining ASCII banner for strength meter
PE_banner = pyfiglet.figlet_format("Password Encryption") #defining ASCII banner for Password Encryption
HS_banner = pyfiglet.figlet_format("Hashing") #defining ASCII banner for Hashing
TP_banner = pyfiglet.figlet_format("Tips") #defining ASCII banner for Tips

print(ascii_banner) #view banner

for i in range(5): #loop for user's choices
    print("[" + str(i) + "] " + options[i])
    i+=1

print()

while True:
    choice = int(input("Choice: ")) #user input
    if (choice == 0):
        os.system('cls')
        print(SM_banner)
        print("This is KeyWord's strength meter. A good strong password is a must. \nSome people unfortunately choose weak passwords that can easily be cracked ny a hacker. \nSo it is better to test the strength of your password to see if it is strong enough.")
        print()
        passwordSM = getpass.getpass("Password: ")
        score = 0 #score set to 0 to later on determine the strength
        if regex.search('[a-z]',passwordSM): #check for lowercase letters
            score += 1
        else:
            score -= 0
        if regex.search('[A-Z]',passwordSM): #check for uppercase letters
            score += 1
        else:
            score -= 0
        if len(passwordSM) > 10: #check if password has a minimum length of 10 letters
            score += 1
        else:
            score -= 0
        if regex.search('[0-9]',passwordSM): #check for numbers
            score += 1
        else:
            score -= 0
        if regex.search('[|^&+\-%*/=!>;,.()`´§]', passwordSM): #check for special characters
            score += 1
        else:
            score -= 0
        print('Your password: ' + passwordSM)
        if score == 1 or score == 2: #password is weak when score is 1/5 or 2/5
            print('Your password is weak.')
        if score == 3: #password is medium when score is 3/5 
            print('Your password is medium, try to make it more secure.')
        if score == 4 or score == 5: #password is weak when score is 4/5 or 5/5
            print('Your password is strong.')
        while True:
            ans = str(input("New attempt? (y/n): "))
            if ans == 'y' or ans == 'Y': #if user answers y or Y. User can try again
                os.system('cls')
                print(SM_banner)
                print("This is KeyWord's strength meter. A good strong password is a must. \nSome people unfortunately choose weak passwords that can easily be cracked ny a hacker. \nSo it is better to test the strength of your password to see if it is strong enough.")
                print()
                passwordSM = getpass.getpass("Password: ")
                score = 0 #score set to 0 to later on determine the strength
                if regex.search('[a-z]',passwordSM): #check for lowercase letters
                    score += 1
                else:
                    score -= 0
                if regex.search('[A-Z]',passwordSM): #check for uppercase letters
                    score += 1
                else:
                    score -= 0
                if len(passwordSM) > 10: #check if password has a minimum length of 10 letters
                    score += 1
                else:
                    score -= 0
                if regex.search('[0-9]',passwordSM): #check for numbers
                    score += 1
                else:
                    score -= 0
                if regex.search('[|^&+\-%*/=!>;,.()`´§]', passwordSM): #check for special characters
                    score += 1
                else:
                    score -= 0
                print('Your password: ' + passwordSM)
                if score == 1 or score == 2: #password is weak when score is 1/5 or 2/5
                    print('Your password is weak.')
                if score == 3: #password is medium when score is 3/5 
                    print('Your password is medium, try to make it more secure.')
                if score == 4 or score == 5: #password is weak when score is 4/5 or 5/5
                    print('Your password is strong.')
            elif ans == 'n' or ans == 'N': #if user answers n or N. It will go back to the menu by restarting the script
                os.system('cls')
                sys.stdout.flush()
                os.execl(sys.executable, 'python', __file__, *sys.argv[1:])
                break
            else:
                print("invalid choice")
        break
    elif (choice == 1):
        os.system('cls')
        print(PE_banner)
        print("Encryption is a 2-way process in which, on one hand, the data is converted from plaintext into a “ciphertext” using an encryption key and on the other, it is converted back into plaintext by using a decryption key.")
        print()
        passwordPE = getpass.getpass("Password: ")
        key = Fernet.generate_key()
        fernet = Fernet(key)
        encpasswordPE = fernet.encrypt(passwordPE.encode())
        print("encrypted string: ", encpasswordPE)
        decpasswordPE = fernet.decrypt(encpasswordPE).decode()
        print("decrypted string: ", decpasswordPE)
        while True:
            ans = str(input("New attempt? (y/n): "))
            if ans == 'y' or ans == 'Y':
                os.system('cls')
                print(PE_banner)
                print("Encryption is a 2-way process in which, on one hand, the data is converted from plaintext into a “ciphertext” using an encryption key and on the other, it is converted back into plaintext by using a decryption key.")
                print()
                passwordPE = getpass.getpass("Password: ")
                key = Fernet.generate_key()
                fernet = Fernet(key)
                encpasswordPE = fernet.encrypt(passwordPE.encode())
                print("encrypted string: ", encpasswordPE)
                decpasswordPE = fernet.decrypt(encpasswordPE).decode()
                print("decrypted string: ", decpasswordPE)
            elif ans == 'n' or ans == 'N':
                os.system('cls')
                sys.stdout.flush()
                os.execl(sys.executable, 'python', __file__, *sys.argv[1:])
                break
            else:
                print("invalid choice.")
        break
    elif (choice == 2):
        os.system('cls')
        print(HS_banner)
        print("When a password has been “hashed” it means it has been turned into a scrambled representation of itself by the MD5 hashfunction.")
        print()
        passwordHS = getpass.getpass("Password: ")
        hashedPW = hashlib.md5(passwordHS.encode()) # encoding the password using encode() then sending to md5()
        print("Your password in plain text: " + passwordHS)
        print("Hashed password: " + hashedPW.hexdigest()) #show the hashed password
        #give the user another chance if needed
        while True: 
            ans = str(input("New attempt? (y/n): "))
            if ans == 'y' or ans == 'Y': #if user answers y or Y. User can try again
                os.system('cls')
                print(HS_banner)
                print("When a password has been “hashed” it means it has been turned into a scrambled representation of itself by the MD5 hashfunction.")
                print()
                passwordHS = getpass.getpass("Password: ")
                hashedPW = hashlib.md5(passwordHS.encode()) # encoding the password using encode() then sending to md5()
                print("Your password in plain text: " + passwordHS)
                print("Hashed password: " + hashedPW.hexdigest()) #show the hashed password
            elif ans == 'n' or ans == 'N': #if user answer n or N. It will go back to menu by restarting the script
                os.system('cls')
                sys.stdout.flush()
                os.execl(sys.executable, 'python', __file__, *sys.argv[1:])
                break
        break
    elif (choice == 3):
        os.system('cls')
        print(TP_banner)
        print("Here are a few tips you can benefit from to create a strong password.")
        print("")
        with open('tips.txt', encoding='utf8') as file: #reading the txt file containing the tips regarding passsword security
            for line in file:
                print(line.rstrip())
        print()
        while True:
            ans = str(input("Do you want to exit? (y/n): "))
            if ans == 'n' or ans == 'N': #if user answers y or Y. User can try again
                os.system('cls')
                print(TP_banner)
                print("Here are a few tips you can benefit from to create a strong password.")
                print("")
                with open('tips.txt', encoding='utf8') as file: #reading the txt file containing the tips regarding passsword security
                    for line in file:
                        print(line.rstrip())
                print()
            elif ans == 'y' or ans == 'Y': #if user answer n or N. It will go back to menu by restarting the script
                os.system('cls')
                sys.stdout.flush()
                os.execl(sys.executable, 'python', __file__, *sys.argv[1:])
                break
        break
    elif (choice ==4):
        exit() #close the program
        break
    else:
        print("invalid choice please try again.") #notice the user after wrong input