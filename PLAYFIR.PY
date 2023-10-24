def playfair_cipher(plaintext, key, mode):
    alphabet = 'abcdefghiklmnopqrstuvwxyz'

    key = key.replace(' ', '').replace('j', '').lower()

    key_square = ''
    for letter in key + alphabet:
        if letter not in key_square:
            key_square += letter

    plaintext = plaintext.replace(' ', '').replace('j', 'i').lower()
    if len(plaintext) % 2 == 1:
        plaintext += 'x'
    digraphs = [plaintext[i:i+2] for i in range(0, len(plaintext), 2)]

    result = ''
    for digraph in digraphs:
        if mode == 'encrypt':
            result += encrypt_digraph(digraph, key_square)
        elif mode == 'decrypt':
            result += decrypt_digraph(digraph, key_square)

    return result

def encrypt_digraph(digraph, key_square):
    if digraph[0] not in key_square:
        digraph = 'x' + digraph[1]
    if digraph[1] not in key_square:
        digraph = digraph[0] + 'x'

    row_a, col_a = key_square.index(digraph[0]) // 5, key_square.index(digraph[0]) % 5
    row_b, col_b = key_square.index(digraph[1]) // 5, key_square.index(digraph[1]) % 5

    if row_a == row_b:
        return key_square[row_a * 5 + (col_a + 1) % 5] + key_square[row_b * 5 + (col_b + 1) % 5]

    elif col_a == col_b:
        return key_square[(row_a + 1) % 5 * 5 + col_a] + key_square[(row_b + 1) % 5 * 5 + col_b]

    else:
        return key_square[row_a * 5 + col_b] + key_square[row_b * 5 + col_a]

def decrypt_digraph(digraph, key_square):
    if digraph[0] not in key_square:
        digraph = 'x' + digraph[1]
    if digraph[1] not in key_square:
        digraph = digraph[0] + 'x'

    row_a, col_a = key_square.index(digraph[0]) // 5, key_square.index(digraph[0]) % 5
    row_b, col_b = key_square.index(digraph[1]) // 5, key_square.index(digraph[1]) % 5

    if row_a == row_b:
        return key_square[row_a * 5 + (col_a - 1) % 5] + key_square[row_b * 5 + (col_b - 1) % 5]

    elif col_a == col_b:
        return key_square[(row_a - 1) % 5 * 5 + col_a] + key_square[(row_b - 1) % 5 * 5 + col_b]

    else:
        return key_square[row_a * 5 + col_b] + key_square[row_b * 5 + col_a]

print("Playfair Cipher Implementation: - \n")
plaintext = input("Enter the data \n")
key = input("Enter the key \n")

encrypted_message = playfair_cipher(plaintext, key, 'encrypt')
decrypted_message = playfair_cipher(encrypted_message, key, 'decrypt')

print("\nOriginal message :", plaintext)
print("Key used         :", key)
print("Encrypted message:", encrypted_message)
print("Decrypted message:", decrypted_message)
