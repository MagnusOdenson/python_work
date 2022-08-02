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