import random

import time
import psutil

# Utility to simulate command flashes and processing time
def simulate_processing(text, duration=2):
    print(text)
    time.sleep(duration)
    print("Processing...")
    time.sleep(duration)
    print("Done.")

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Function to display system stats
def display_system_stats():
    cpu_usage = psutil.cpu_percent(interval=1)
    virtual_memory = psutil.virtual_memory().percent
    print(f"CPU Usage: {cpu_usage}%")
    print(f"Memory Usage: {virtual_memory}%")
    gpu_power = "Estimating..."
    print(f"GPU Power: {gpu_power}")
    time.sleep(1)

# RSA Key Generation
def generate_keypair(p, q):
    simulate_processing("Initializing RSA Key Generation...")
    n = p * q
    phi = (p - 1) * (q - 1)
    
    simulate_processing(f"Calculating n (p * q): {n}")
    simulate_processing(f"Calculating φ(n) (phi): {phi}")

    e = random.randrange(1, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(1, phi)
    simulate_processing(f"Chosen public exponent 'e': {e}")

    d = pow(e, -1, phi)
    simulate_processing(f"Calculated private exponent 'd': {d}")
    
    public_key = (e, n)
    private_key = (d, n)
    
    print(f"Public Key: {public_key}")
    print(f"Private Key: {private_key}")
    
    display_system_stats()
    return public_key, private_key

# Encryption
def encrypt(public_key, plaintext):
    simulate_processing("Encrypting Message...")
    e, n = public_key
    cipher = [(ord(char) ** e) % n for char in plaintext]
    simulate_processing(f"Original Message: {plaintext}")
    simulate_processing(f"Encrypted Message (ciphertext): {cipher}")
    display_system_stats()
    return cipher

# Decryption
def decrypt(private_key, ciphertext):
    simulate_processing("Decrypting Message...")
    d, n = private_key
    plain = [chr((char ** d) % n) for char in ciphertext]
    decrypted_message = ''.join(plain)
    simulate_processing(f"Decrypted Message: {decrypted_message}")
    display_system_stats()
    return decrypted_message

def brute_force_attack(public_key, ciphertext):
    print("\n*** WARNING: RSA - Brute Force Attack Engaged ***")
    proceed = input("Do you want to proceed? (y/n): ").strip().lower()

    if proceed != 'y':
        print("Attack aborted.")
        return

    password = input("Enter password to authorize attack: ").strip()
    if password != "Ishaan3949":
        print("Authorization failed. Attack aborted.")
        return

    print("\n--- Performing Brute-force Attack ---")
    time.sleep(1)  # Simulate delay before the attack begins
    e, n = public_key
    attack_started = time.time()

    for possible_d in range(2, n):
        possible_plain = []
        is_valid = True

        for char in ciphertext:
            decoded_char = (char ** possible_d) % n
            if 32 <= decoded_char <= 126:  # Check for valid ASCII characters
                possible_plain.append(chr(decoded_char))
            else:
                is_valid = False  # Mark the key as invalid if a non-ASCII character is found
                break

        if is_valid:  # If all characters are valid, print the decrypted message
            possible_message = ''.join(possible_plain)
            print(f"Trying private key 'd': {possible_d} -> Possible Message: {possible_message}")
            
            # Simple check for common words in the message
            if " " in possible_message or any(word in possible_message.lower() for word in ["hola", "friends"]):
                print("\n--- Brute-force Attack Successful ---")
                print(f"Discovered private key: {possible_d}")
                print(f"Decrypted Message: {possible_message}")
                break

    attack_ended = time.time()
    attack_duration = attack_ended - attack_started
    simulate_processing(f"Attack Duration: {attack_duration:.2f} seconds")
    display_system_stats()


def main():
    print("=== RSA Encryption and Attack Simulation ===")
    
    message = input("Enter the message you want to encrypt: ")

    p = 78
    q = 41
    
    public_key, private_key = generate_keypair(p, q)
    encrypted_msg = encrypt(public_key, message)
    decrypted_msg = decrypt(private_key, encrypted_msg)
    brute_force_attack(public_key, encrypted_msg)

if __name__ == "__main__":
    main()
