import hashlib

# RSA key components
e = 3
d = 27
n = 55

# Serialize keys as strings
public_key_str = f"{e},{n}"
private_key_str = f"{d},{n}"

# Hash function
def sha256_hash(data):
    return hashlib.sha256(data.encode()).hexdigest()

# Compute hashes
public_key_hash = sha256_hash(public_key_str)
private_key_hash = sha256_hash(private_key_str)

# Display on console
print("Public Key Hash (SHA-256):", public_key_hash)
print("Private Key Hash (SHA-256):", private_key_hash)

# Save to file
with open("rsa_hashes.txt", "w") as f:
    f.write("RSA Key Hashes (SHA-256)\n")
    f.write("=========================\n")
    f.write(f"Public Key (e={e}, n={n}): {public_key_hash}\n")
    f.write(f"Private Key (d={d}, n={n}): {private_key_hash}\n")

print("Hashes saved to rsa_hashes.txt")
