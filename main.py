print("Diffie Hellman Key Exchange Demo")

# Public values
p = int(input("Enter Prime Number: "))
g = int(input("Enter Generator: "))

# Private keys of Alice and Bob
alice_private = int(input("Enter Alice Private Key: "))
bob_private = int(input("Enter Bob Private Key: "))

# Generate public keys
alice_public = (g ** alice_private) % p
bob_public = (g ** bob_private) % p

print("\nAlice Public Key:", alice_public)
print("Bob Public Key:", bob_public)

# Generate shared secret key
alice_secret = (bob_public ** alice_private) % p
bob_secret = (alice_public ** bob_private) % p

print("\nAlice Secret Key:", alice_secret)
print("Bob Secret Key:", bob_secret)

# Eavesdropper view
print("\n--- Eavesdropper View ---")
print("Prime Number:", p)
print("Generator:", g)
print("Alice Public Key:", alice_public)
print("Bob Public Key:", bob_public)

# Check result
if alice_secret == bob_secret:
    print("\nSecret Key Matched Successfully")
    print("Eavesdropper cannot calculate the final secret key")
else:
    print("\nKey Exchange Failed")