# RSA Parameters
p = 5
q = 11
e = 3
message = 7

# Calculate n and φ(n)
n = p * q
phi_n = (p - 1) * (q - 1)

print(f"Given values:")
print(f"p = {p}, q = {q}")
print(f"n = p × q = {p} × {q} = {n}")
print(f"φ(n) = (p-1)(q-1) = {p-1} × {q-1} = {phi_n}")
print(f"e = {e}")
print()

# Find private key d using Extended Euclidean Algorithm
def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def mod_inverse(e, phi_n):
    gcd, x, y = extended_gcd(e, phi_n)
    if gcd != 1:
        return None  # No inverse exists
    return (x % phi_n + phi_n) % phi_n

d = mod_inverse(e, phi_n)
print(f"Private key calculation:")
print(f"Find d such that {e}d ≡ 1 mod {phi_n}")
print(f"d = {d}")
print(f"Verification: {e} × {d} mod {phi_n} = {(e * d) % phi_n}")
print()

# Display keys
print(f"Keys:")
print(f"Public key = ({e}, {n})")
print(f"Private key = ({d}, {n})")
print()

# Encryption: C = M^e mod n
ciphertext = pow(message, e, n)
print(f"Encryption:")
print(f"Message M = {message}")
print(f"C = {message}^{e} mod {n}")
print(f"C = {message**e} mod {n}")
print(f"C = {ciphertext}")
print()

# Decryption: M = C^d mod n
decrypted = pow(ciphertext, d, n)
print(f"Decryption:")
print(f"Ciphertext C = {ciphertext}")
print(f"M = {ciphertext}^{d} mod {n}")
print(f"M = {decrypted}")
print()

# Verification
print(f"Verification:")
print(f"Original message: {message}")
print(f"Decrypted message: {decrypted}")
print(f"Match: {message == decrypted}")

# Additional test case
print(f"\n" + "="*50)
print(f"Testing decryption of C = 13:")
test_decrypt = pow(13, d, n)
print(f"13^{d} mod {n} = {test_decrypt}")