guest_list = ['Ada Lovelace', 'Akira Toriyama', 'Ben Affleck']
message = "you are cordially invited to a dinner."

message1 = "We managed to find a bigger venue.\nThus more people have been invited:"

print(message1)

guest_list.insert(0, 'Henry Cavill')
guest_list.append('Gal Gadot')
guest_list.insert(3, 'John Cena')

print(f"{guest_list[0]}, {message}")
print(f"{guest_list[1]}, {message}")
print(f"{guest_list[2]}, {message}")
print(f"{guest_list[3]}, {message}")
print(f"{guest_list[4]}, {message}")
print(f"{guest_list[5]}, {message}")

message2 = "Unfortunately the new venue is being fumigated,\nthus only 2 people can be invited."

print(message2)

popped_guest1 = guest_list.pop(0)
message3 = "Utmost apologies but I have to rescind the invitation."

print(f"{popped_guest1}, {message3}")

popped_guest2 = guest_list.pop(3)

print(f"{popped_guest2}", {message3})

popped_guest3 = guest_list.pop(2)

print(f"{popped_guest3}, {message3}")

popped_guest4 = guest_list.pop(1)

print(f"{popped_guest4}, {message3}")



print(f"{guest_list[0]}, {message}")
print(f"{guest_list[1]}, {message}")