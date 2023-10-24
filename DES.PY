from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes

def des_encrypt(plain_text, key):
    des = DES.new(key, DES.MODE_ECB)
    cipher_text = des.encrypt(plain_text)
    return cipher_text

def des_decrypt(cipher_text, key):
    des = DES.new(key, DES.MODE_ECB)
    plain_text = des.decrypt(cipher_text)
    return plain_text

if __name__ == '__main__':
    key = get_random_bytes(8)  # 8 bytes (64 bits) key
    plaintext = b'adhu kumar'

    # Padding the plaintext to a multiple of 8 bytes if needed
    if len(plaintext) % 8 != 0:
        plaintext += b' ' * (8 - len(plaintext) % 8)

    encrypted = des_encrypt(plaintext, key)
    decrypted = des_decrypt(encrypted, key)

    print(f"Original: {plaintext}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")
