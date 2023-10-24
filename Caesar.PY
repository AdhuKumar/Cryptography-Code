def caesar_cipher(plaintext, shift, mode):

  ciphertext = ""

  for letter in plaintext:
    if mode == "encrypt":
      ciphertext += chr((ord(letter) + shift - 65) % 26 + 65)
    elif mode == "decrypt":
      ciphertext += chr((ord(letter) - shift - 65) % 26 + 65)

  return ciphertext

print("Caesar Cipher Implementation: - \n")

plaintext = input("Enter the data: ")
shift = int(input("Enter the key: "))

encrypted_message = caesar_cipher(plaintext, shift, "encrypt")
decrypted_message = caesar_cipher(encrypted_message, shift, "decrypt")

print("\nOriginal Message  : " + plaintext)
print("Key Used          : " + str(shift))  
print("Encrypted Message : " + encrypted_message)
print("Decrypted Message : " + decrypted_message)
