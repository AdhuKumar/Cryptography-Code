def encrypt(message, key):
    encrypted_message = ""
    for i in range(len(message)):
        if message[i].isalpha():
            if message[i].islower():
                encrypted_message += key[ord(message[i]) - ord('a')]
            else:
                encrypted_message += key[ord(message[i]) - ord('A')].upper()
        else:
            encrypted_message += message[i]
    return encrypted_message

def decrypt(encrypted_message, key):
    decrypted_message = ""
    for i in range(len(encrypted_message)):
        if encrypted_message[i].isalpha():
            if encrypted_message[i].islower():
                decrypted_message += chr(key.index(encrypted_message[i]) + ord('a'))
            else:
                decrypted_message += chr(key.index(encrypted_message[i].lower()) + ord('A'))
        else:
            decrypted_message += encrypted_message[i]
    return decrypted_message

print("Monoalphabetic Cipher Implementation: - \n")
message = input("Enter the data \n")
key = "zyxwvutsrqponmlkjihgfedcba"

encrypted_message = encrypt(message, key)
decrypted_message = decrypt(encrypted_message, key)

print("\nOriginal Message is : " + message)
print("Encrypted Message is: " + encrypted_message)
print("Decrypted Message is: " + decrypted_message)
