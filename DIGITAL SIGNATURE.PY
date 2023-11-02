def euclid(m, n):
    if n == 0:
        return m
    else:
        r = m % n
        return euclid(n, r)

def exteuclid(a, b):
    r1 = a
    r2 = b
    s1 = 1
    s2 = 0
    t1 = 0
    t2 = 1
    while r2 > 0:
        q = r1 // r2
        r = r1 - q * r2
        r1 = r2
        r2 = r
        s = s1 - q * s2
        s1 = s2
        s2 = s
        t = t1 - q * t2
        t1 = t2
        t2 = t
    if t1 < 0:
        t1 = t1 % a
    return (r1, t1)

# Enter two large prime numbers p and q
p = 823
q = 953
n = p * q
Pn = (p - 1) * (q - 1)

# Generate encryption key in the range 1 < e < Pn
key = []
for i in range(2, Pn):
    gcd = euclid(Pn, i)
    if gcd == 1:
        key.append(i)

e = 313  # You can choose an encryption key from the 'key' list
r, d = exteuclid(Pn, e)
if r == 1:
    d = d % Pn  # Ensure the private key is within the range [0, Pn)
    print("Decryption key is:", d)
else:
    print("Multiplicative inverse for the given encryption key does not exist. Choose a different encryption key")

# Enter the message to be sent
M = 19070

# Signature is created by Adhu
S = (M**d) % n
M1 = (S**e) % n

# If M = M1, only then we accept the message sent by Adhu.
if M == M1:
    print("As M = M1, accept the message sent by Adhu")
else:
    print("As M is not equal to M1, do not accept the message sent by Adhu")
