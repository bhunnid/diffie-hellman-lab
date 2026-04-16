import random

p = 23
g = 5

# Alice
a = random.randint(1, p-1)
A = pow(g, a, p)

# Bob
b = random.randint(1, p-1)
B = pow(g, b, p)

# Eve (attacker)
e1 = random.randint(1, p-1)
e2 = random.randint(1, p-1)

E1 = pow(g, e1, p)
E2 = pow(g, e2, p)

# Attack:
# Alice thinks she receives B, but actually gets E1
alice_secret = pow(E1, a, p)

# Bob thinks he receives A, but actually gets E2
bob_secret = pow(E2, b, p)

# Eve computes both secrets
eve_with_alice = pow(A, e1, p)
eve_with_bob   = pow(B, e2, p)

print("=== MITM ATTACK ===")

print("\nAlice's computed secret:", alice_secret)
print("Bob's computed secret:  ", bob_secret)

print("\nEve's secrets:")
print("Eve <-> Alice:", eve_with_alice)
print("Eve <-> Bob:  ", eve_with_bob)