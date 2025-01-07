# i=0
# while i<5:
#     print(i*"a")
#     i=i+1

# for i in range(1, 6):
#     print(i*"a")

# password = input("Enter Password: ")
# correct_pw = "Ablution"
# while  password != correct_pw:
#         print("Wrong Password")
#         password = input("Enter Password: ")
# print("successful")

#  password = input("Enter Password: ")
# # correct_pw = "Ablution"
# # while  password != correct_pw:
# #         print("Wrong Password")
# #         password = input("Enter Password: ")
# # print("successful")

correct_pw="Ablution"
i=0
while i < 4: #maximum itrations
    password = input("Enter Password: ")
    i=i+1 
    if password == correct_pw:
        print("successful")
        break
    else:
        remaining_attempts = 3 - i
        if remaining_attempts > 0:
         print("Wrong Password, you have", remaining_attempts, "remaining attempts left" )
        
    if i == 3:
        print("your account is blocked")
    
# number = 0
# while number < 6:
#     number=number+1
#     #print(number)
#     diff = 3 - number
    
#     if diff > 0: 
#          print(diff)
# correct_password = "Ablution"
# i=0
# while i < 4:
#     i=1+i
#     password = input("Enter Password")
#     if password == correct_password:
#         print("Successful")
#     else: print("Wrong Password")

