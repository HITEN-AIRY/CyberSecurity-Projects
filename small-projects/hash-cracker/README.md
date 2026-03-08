# Python Hash Cracker

A dictionary-based hash cracking tool implemented in Python.
This project demonstrates how hashed passwords can be tested against a wordlist using common cryptographic hash algorithms.

## Overview

Many systems store passwords as **hash values** instead of plaintext.
A hash function converts an input string into a fixed-length output that cannot easily be reversed.

Attackers often attempt to recover the original password using a **dictionary attack**, where candidate words are hashed and compared against a target hash.

This tool replicates that process for educational purposes.

## Supported Algorithms

The script supports the following hashing algorithms:

* MD5
* SHA1
* SHA256
* SHA512
* SHA3_256
* SHA3_512

All hashing functions are implemented using Python’s `hashlib` module.

## Libraries Used

* hashlib
* pyfiglet
* sys

## Project Structure

```
hash-cracker
│
├── hash_cracker.py
├── wordlist.txt
├── example_hashes.txt
└── README.md
```

## How It Works

1. The user selects the hashing algorithm.
2. The program loads a wordlist containing potential passwords.
3. Each word is hashed using the selected algorithm.
4. The generated hash is compared with the target hash.
5. If a match is found, the plaintext password is displayed.

## Installation

Install the required dependency:

```
pip install pyfiglet
```

## Usage

Run the script:

```
python hash_cracker.py
```

Example input:

```
Hash type: MD5
Wordlist location: wordlist.txt
Enter hash: 5f4dcc3b5aa765d61d8327deb882cf99
```

Output:

```
Hash Cracked! The word is: password
```

## Example Hash

The following hash corresponds to the password `password`.

```
MD5
5f4dcc3b5aa765d61d8327deb882cf99
```

## Disclaimer

This project is intended for educational purposes to demonstrate password cracking techniques and the importance of strong password security.

Do not use this tool on systems or data without proper authorization.

## Author

Hiten Singh Airy
GitHub: https://github.com/HITEN-AIRY

