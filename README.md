RSA Encryption and Decryption Project
This project implements RSA encryption and decryption using C++ with GMP and OpenMP for efficient handling of large numbers and parallel processing. It allows generating large prime numbers, creating public and private keys, and encrypting and decrypting messages provided by the user.

Features
Modular Exponentiation: Calculates powers modulo a large number efficiently.
Miller-Rabin Primality Test: Verifies if large numbers are prime.
Prime Generation: Generates large prime numbers with specified bit lengths.
Extended Euclidean Algorithm: Calculates modular inverses for key generation.
OpenMP: Utilizes parallel processing to optimize prime checking.
GMP Library: Handles large integer operations required for RSA encryption.
Requirements
C++ compiler
GMP Library
OpenMP
gmpxx.h for C++ interface to GMP
Setup
Clone the repository:
