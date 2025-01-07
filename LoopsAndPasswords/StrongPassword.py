import string
while True:
    password = input("Please enter your password or type in 'Exit' to exit: ")
    if password.lower() == "exit":
        break
    password_has_uppercase = any(letter.isupper() for letter in password)
    password_has_lowercase = any(letter.islower() for letter in password)
    password_has_digit = any(letter.isdigit() for letter in password)
    password_has_specialChar = any(letter in string.punctuation for letter in password)
    password_has_length = len(password)
    if not  6 <= password_has_length <= 12 :
        print("Your password should be betwwen 6 and 12 characters")
    if   password_has_lowercase is False :
        print("Your password should have atlease one lowercase letter")
    if   password_has_uppercase is False :
        print("Your password should have atlease one uppercase letter")
    if  not password_has_digit:
        print("Your password should has atleast one number")
    if  not password_has_specialChar:
        print("Your password should have at least one speacial character")      
    if  6 <= password_has_length <= 12 and password_has_specialChar and password_has_digit and password_has_lowercase and password_has_uppercase :
        print("Your are logged in successfully")
        break

        

            

