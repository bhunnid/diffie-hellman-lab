from Crypto.PublicKey import ECC
from Crypto.Hash import SHA256
from Crypto.Protocol.KDF import HKDF

# Generate ephemeral keys
alice = ECC.generate(curve='P-256')
bob = ECC.generate(curve='P-256')

alice_pub = alice.public_key()
bob_pub = bob.public_key()

# Shared secret (ECDH)
alice_point = alice.d * bob_pub.pointQ
bob_point = bob.d * alice_pub.pointQ

alice_secret = int(alice_point.x).to_bytes(32, 'big')
bob_secret = int(bob_point.x).to_bytes(32, 'big')

# Derive strong symmetric key
alice_key = HKDF(alice_secret, 32, b'context', SHA256)
bob_key = HKDF(bob_secret, 32, b'context', SHA256)

print("=== SECURE ECDH ===")

print("\nAlice Key:", alice_key.hex())
print("Bob Key:  ", bob_key.hex())

print("\nKeys match:", alice_key == bob_key)