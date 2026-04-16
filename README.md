# 🔐 Diffie-Hellman Key Exchange Lab

## 📌 Exploring Insecure vs Secure Diffie-Hellman (D-H)

---

## 1. 🎯 Objective

The objective of this lab is to:

- Implement the basic (**insecure**) Diffie-Hellman key exchange  
- Demonstrate its vulnerability to **Man-in-the-Middle (MitM)** attacks  
- Implement a secure version using **Elliptic Curve Diffie-Hellman (ECDH)**  
- Compare outputs and evaluate their security properties  

---

## 2. ⚙️ Environment Setup

The lab was conducted on a **Kali Linux virtual machine**.

### Steps:
- Installed Python environment  
- Created a virtual environment for isolation  
- Installed required cryptographic library (**PyCryptodome**)  

### Commands Used:

```bash
python3 -m venv dh_env
source dh_env/bin/activate
pip install pycryptodome
📸 Environment Setup Output

3. 🔓 Insecure Diffie-Hellman Implementation

The basic Diffie-Hellman algorithm was implemented using small prime numbers and modular exponentiation.

Key Steps:
Public parameters 
𝑝
p and 
𝑔
g are shared
Each party generates a private key
Public keys are exchanged
Shared secret is computed
📸 Insecure DH Output

🔍 Observation:
Both parties compute the same shared secret
Keys are small and lack authentication, making them insecure
4. ⚔️ Man-in-the-Middle (MitM) Attack Simulation

A MitM attack was simulated by introducing an attacker (Eve) who intercepts and replaces public keys.

📸 MitM Attack Output

🔍 Observation:
Alice and Bob no longer share the same secret
Eve establishes separate keys with both parties
Communication can be intercepted and modified
5. 🔐 Secure Diffie-Hellman (ECDH) Implementation

A secure implementation was developed using:

Elliptic Curve Cryptography (ECC)
Ephemeral keys (forward secrecy)
Key Derivation Function (HKDF)
📸 Secure ECDH Output

🔍 Observation:
Both parties derive identical secure keys
Keys are long, random, and cryptographically strong
Each execution produces a different key (forward secrecy)
6. 📊 Comparison of Outputs
Aspect	Insecure DH (insecure_dh.py)	Secure ECDH (secure_ecdh.py)
Public Parameters	Small integers (p = 23, g = 5)	Curve implicit (P-256)
Public Keys	Simple integers	PEM-encoded keys
Private Keys	Printed	Not exposed
Shared Secret	Small integer	Processed into bytes
Final Key	Weak (same as shared secret)	256-bit cryptographic key
Key Size	Very small	Strong (256-bit)
Randomness	Low	High
Output Format	Plain numbers	Hexadecimal
Consistency	Matching values	Matching values
Reproducibility	Possible	Practically impossible
Exposure Risk	High	Very low
Forward Secrecy	❌ No	✅ Yes
Security Level	Educational only	Production-grade
7. 🧠 Conclusion

This lab demonstrates that while the basic Diffie-Hellman algorithm correctly establishes a shared secret, it is inherently insecure due to its vulnerability to Man-in-the-Middle attacks.

The secure ECDH implementation improves security by:

Using strong elliptic curve cryptography
Applying key derivation techniques
Ensuring forward secrecy through ephemeral keys

👉 Therefore, secure key exchange must include authentication and modern cryptographic primitives to be viable in real-world systems.