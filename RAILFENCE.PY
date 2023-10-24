def rail_fence_encrypt(plain_text, rails):
    fence = [['\n' for _ in range(len(plain_text))] for _ in range(rails)]
    direction = -1
    row, col = 0, 0

    for char in plain_text:
        if row == 0 or row == rails - 1:
            direction = -direction
        fence[row][col] = char
        col += 1
        row += direction

    encrypted_text = ''.join(char for row in fence for char in row if char != '\n')
    return encrypted_text

def rail_fence_decrypt(cipher_text, rails):
    fence = [['\n' for _ in range(len(cipher_text))] for _ in range(rails)]
    direction = -1
    row, col = 0, 0

    for char in cipher_text:
        if row == 0 or row == rails - 1:
            direction = -direction
        fence[row][col] = '*'
        col += 1
        row += direction

    index = 0
    for row in range(rails):
        for col in range(len(cipher_text)):
            if fence[row][col] == '*' and index < len(cipher_text):
                fence[row][col] = cipher_text[index]
                index += 1

    direction = -1
    row, col = 0, 0
    decrypted_text = ''

    for _ in range(len(cipher_text)):
        if row == 0 or row == rails - 1:
            direction = -direction
        decrypted_text += fence[row][col]
        col += 1
        row += direction

    return decrypted_text

print("Railfence Cipher Implementation: - \n")
message = input("Enter the data: \n")
rails = int(input("Enter the number of rails: \n"))

encrypted_text = rail_fence_encrypt(message, rails)
decrypted_text = rail_fence_decrypt(encrypted_text, rails)

print("Original message : ", message)
print("Encrypted message: ", encrypted_text)
print("Decrypted message: ", decrypted_text)
