usernames = ['zdzisiek', 'warcek', 'ziemowit', 'burgund', 'admin']

for username in usernames:
    if username == 'admin':
        print(f"Hello {username}, would you like to see a status report?")
    else:
        print(f"Hello {username}, thank you for logging again!")