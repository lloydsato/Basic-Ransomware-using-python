import os
from cryptography.fernet import Fernet

# listing files

files = []

for file in os.listdir():
    if file == "main.py" or file == "thekey.key" or file == "Decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)


print(files)

# Assigning decryption key to a variable
with open("thekey.key", "rb") as key:
    secretkey = key.read()

# Secret phrase to activate decryption script (optional)
secret_phrase = "Chicken_biryani"
user_phrase = input("Enter the secret phrase")

if user_phrase == secret_phrase:

# decrypting the files (Decryption script)
    for file in files:
        with open(file, "rb") as thefile:
            contents = thefile.read()
        contents_decrypted = Fernet(secretkey).decrypt(contents)
        with open(file, "wb") as thefile:
            thefile.write(contents_decrypted)
else:
    print("oops wrong one, TRY AGAIN")

