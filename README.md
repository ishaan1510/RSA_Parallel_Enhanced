
# RSA Encryption and Decryption Project

This project implements RSA encryption and decryption using large prime numbers, optimized modular arithmetic, and parallelization. It includes functions for key generation, encryption, and decryption, all executed with efficient computational methods.

## Project Structure

- **RSA Key Generation**: Generates public and private keys using large primes `p` and `q`.
- **Miller-Rabin Primality Test**: Used to ensure the primality of generated numbers.
- **Modular Exponentiation**: Computes large power mod operations efficiently.
- **Encryption and Decryption**: Encrypts and decrypts integer messages using the generated RSA keys.

## Prerequisites

- **GMP Library**: GNU MP (GMP) library is required for handling large numbers.
- **OpenMP**: To leverage parallelization for efficient computation.
- **G++ Compiler**: Ensure you have the GMP development libraries linked to your compiler.

## Compilation

Use the following commands to compile the project:

```bash
g++ -o rsa_encryption rsa.cpp -lgmp -lgmpxx -fopenmp
```

## Usage

Run the compiled program with the following arguments:

```bash
./rsa_encryption <keysize> <iterations> <threads>
```

Example:

```bash
./rsa_encryption 2048 25 4
```

### Input

- `keysize`: Bit length for the key.
- `iterations`: Number of iterations for the Miller-Rabin primality test.
- `threads`: Number of threads for parallel execution.

### Workflow

1. **Generate RSA Keys**: Runs the Miller-Rabin test to produce two large prime numbers, `p` and `q`, which generate the RSA modulus `n`, public exponent `e`, and private exponent `d`.
2. **Encryption**: Encrypts an integer message input by the user.
3. **Decryption**: Decrypts the ciphertext back to the original integer.

### Sample Output

The output will include the generated keys, encrypted message, and decrypted message:

```plaintext
Generating RSA keys with large primes...
Key generation completed.
Prime Factors (p, q):
p: <prime_p_value>
q: <prime_q_value>

Public Key (n, e):
n: <modulus_n_value>, e: 65537

Private Key (d):
d: <private_d_value>

Enter a message (as an integer) to encrypt: 1234
Encrypted Message: <cipher_value>
Decrypted Message: 1234
```

## Notes

- Ensure you use integer values for message encryption.
- A prime check with Miller-Rabin helps to provide high confidence in prime generation.
- The code handles modular inversion, a critical operation in RSA decryption.

## License

This project is open-source and available under the MIT License.

---

**Happy Encrypting!**
