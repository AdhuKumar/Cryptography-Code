def columnar_cipher_encrypt(message, keyword):
  ciphertext = []
  for i in range(len(keyword)):
    ciphertext.append([])
  rows = []
  for i in range(0, len(message), len(keyword)):
    row = message[i:i + len(keyword)]
    rows.append(row)
  for i in range(len(keyword)):
    for row in rows:
      if i < len(row):
        ciphertext[i].append(row[i])
  ciphertext_string = ""
  for column in ciphertext:
    ciphertext_string += "".join(column)

  return ciphertext_string

def columnar_cipher_decrypt(ciphertext, keyword):
  plaintext = []
  for i in range(len(keyword)):
    plaintext.append([])
  rows = []
  for i in range(0, len(ciphertext), len(keyword)):
    row = ciphertext[i:i + len(keyword)]
    rows.append(row)
  for i in range(len(keyword)):
    for row in rows:
      if i < len(row):
        plaintext[i].append(row[i])
  plaintext_string = ""
  for column in plaintext:
    plaintext_string += "".join(column)
  return plaintext_string

print("Columnar Cipher Implementation: - \n")
message = input("Enter the data: ")
keyword = input("Enter the key: ")
encrypted_message = columnar_cipher_encrypt(message, keyword)
decrypted_message = columnar_cipher_decrypt(encrypted_message, keyword)

print("\nOriginal Message  : " + message)
print("Key Used          : " + keyword)
print("Encrypted Message : " + encrypted_message)
print("Decrypted Message : " + decrypted_message)
