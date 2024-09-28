import random
import string

charmander = " " + string.punctuation + string.digits + string.ascii_letters
charmander = list(charmander)
alicia_keys = charmander.copy()

random.shuffle(alicia_keys)

print(f"charmander: {charmander}")
print(f"alicia_keys: {alicia_keys}")

#ENCRYPT
plain_text = input("Enter a message to encrypt: ")
cipher_text  = ""

for letter in plain_text: 
    index = charmander.index(letter)
    cipher_text += alicia_keys[index]

print(f"original message: {plain_text}")
print(f"encrypted message: {cipher_text}")

#DECRYPT
cipher_text = input("Enter a message to decrypt: ")
plain_text = ""

for letter in cipher_text:
    index = alicia_keys.index(letter)
    plain_text += charmander[index]

print(f"encrypted message: {cipher_text}")
print(f"original message: {plain_text}")