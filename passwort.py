from getpass import getpass
username = input("Benutzername: ")
password = getpass("Passwort: ")
print(f"Benutzername: {username}, Passwort: {'*' * len(password)}")
