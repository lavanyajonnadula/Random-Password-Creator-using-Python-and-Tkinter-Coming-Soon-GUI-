This is a Python-based **secure password generator** that allows users to customize their password structure using numbers, symbols, uppercase, and lowercase characters. It also supports blocklisting unwanted names using a `.docx` file.


🔒 Security Benefits (add this to your README)
This password generator prioritizes security and uniqueness. It ensures that:

Password length is always greater than 8 characters, reducing the risk of brute-force attacks.

It avoids character repetition for stronger entropy.

It cross-checks against a list of blocked names from a DOCX file, helping to prevent use of predictable or commonly hacked passwords (like names).

Since the generation process is fully randomized, it guarantees no two users will receive the same password, making it highly secure.

These layers of validation make this project a strong tool for generating secure and unpredictable passwords, especially useful for systems where user privacy and account safety are top priorities.

