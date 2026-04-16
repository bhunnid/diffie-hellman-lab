import random

p = 23
g = 5

# Alice
a = random.randint(1, p-1)
A = pow(g, a, p)

# Bob
b = random.randint(1, p-1)
B = pow(g, b, p)

# Shared secret
alice_secret = pow(B, a, p)
bob_secret = pow(A, b, p)

print("=== INSECURE DH ===")
print("p =", p, "g =", g)

print("\nAlice -> Private:", a, "Public:", A)
print("Bob   -> Private:", b, "Public:", B)

print("\nShared Secrets:")
print("Alice:", alice_secret)
print("Bob:  ", bob_secret)