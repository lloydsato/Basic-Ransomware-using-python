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

# decrypting the files
for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    contents_decrypted = Fernet(secretkey).decrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_decrypted)

