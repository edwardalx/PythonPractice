myList1 = ["Bill", "Asamoah", "Agya", "Koo", "Mensah","Kantanka", "Obuasi","Accra"]
myList2 = list(myList1)
myList3 = myList1[:]
myList1.append(4)
print(myList1)
print(myList2)
print(myList3)

#loop with for loop

for item in myList2:
    print(item.title())


# 4.10 

first_three = myList1[:3]
print(f"The first three items in the list are: " )
for item in first_three: print(item)

middle_three = myList1[2:5]
print(f"The first three items from the middle are: " )
for item in middle_three: print(item)

last_three = myList1[5:]
print(f"\n The last three items are: " )
for item in last_three: print(item)
myList2.sort()
print(f"My alphabetical order is {myList2}")
myList2.reverse()
print(f"My reverse alphabetical order is {myList2}")

friend_list = myList1[:]
myList1.append("original")
friend_list.append("mypizza")

print("My favorite piz-zas are:")
for item in myList1:
    print(item)

print("\n My friend’s favorite pizzas are:")
friend_list.pop(-2)
print(friend_list)
for item in friend_list:
    print(f"You are welcome {item}, Have a nice day!!!!!")
    print(item.upper(), "\n")