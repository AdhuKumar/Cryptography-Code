from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# Function to pad the data to be a multiple of block_size
def pad_data(data, block_size):
    pad_length = block_size - (len(data) % block_size)
    padding = bytes([pad_length] * pad_length)
    return data + padding

# Function to unpad the data after decryption
def unpad_data(data):
    pad_length = data[-1]
    return data[:-pad_length]

def aes_encrypt(plain_text, key):
    cipher = AES.new(key, AES.MODE_ECB)
    cipher_text = cipher.encrypt(pad_data(plain_text, AES.block_size))
    return cipher_text

def aes_decrypt(cipher_text, key):
    cipher = AES.new(key, AES.MODE_ECB)
    plain_text = unpad_data(cipher.decrypt(cipher_text))
    return plain_text

if __name__ == '__main__':
    key = get_random_bytes(16)  # 16 bytes (128 bits) key
    plaintext = input("Enter the data: ").encode('utf-8')

    encrypted = aes_encrypt(plaintext, key)
    decrypted = aes_decrypt(encrypted, key)

    print(f"Original: {plaintext.decode('utf-8')}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted.decode('utf-8')}")
