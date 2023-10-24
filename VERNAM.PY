import random

def generate_key(length):
  key = ""

  for i in range(length):
    key += chr(random.randint(65, 90))

  return key

def encrypt(plaintext, key):
  ciphertext = ""

  for i in range(len(plaintext)):
    ciphertext += chr(ord(plaintext[i]) ^ ord(key[i]))

  return ciphertext

def decrypt(ciphertext, key):
  plaintext = ""

  for i in range(len(ciphertext)):
    plaintext += chr(ord(ciphertext[i]) ^ ord(key[i]))

  return plaintext

print("Vernam Cipher Implementation: - \n")

plaintext = input("Enter the data: ")
key = generate_key(len(plaintext))

encrypted_message = encrypt(plaintext, key)
decrypted_message = decrypt(encrypted_message, key)

print("\nOriginal Message  : " + plaintext)
print("Key Used          : " + key)
print("Encrypted Message : " + encrypted_message)
print("Decrypted Message : " + decrypted_message)
