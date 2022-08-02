guest_list = ['Ada Lovelace', 'Akira Toriyama', 'Ben Affleck']
message = "you are cordially invited to a dinner."

print(f"{guest_list[0]}, {message}")
print(f"{guest_list[1]}, {message}")
print(f"{guest_list[2]}, {message}")

popped_guest = guest_list.pop(0)
message1 = "can't make it due to illness."

print(f"{popped_guest}, {message1}")
guest_list.append('Henry Cavill')

print(f"{guest_list[0]}, {message}")
print(f"{guest_list[1]}, {message}")
print(f"{guest_list[2]}, {message}")