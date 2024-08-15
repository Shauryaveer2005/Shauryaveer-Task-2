import secrets
import string

def generate_secure_password(length=12, include_uppercase=True, include_digits=True, include_symbols=True):
    if length < 4:
        raise ValueError("Password length should be at least 4 characters")
    
    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if include_uppercase else ''
    digits = string.digits if include_digits else ''
    symbols = string.punctuation if include_symbols else ''
    
    # Combine all characters
    all_characters = lowercase + uppercase + digits + symbols
    
    if not all_characters:
        raise ValueError("At least one character set must be included")
    
    # Ensure the password has at least one character from each selected set
    password = [
        secrets.choice(lowercase),
        secrets.choice(uppercase) if include_uppercase else '',
        secrets.choice(digits) if include_digits else '',
        secrets.choice(symbols) if include_symbols else ''
    ]
    
    # Fill the rest of the password length with random choices from all characters
    password += [secrets.choice(all_characters) for _ in range(length - len(password))]
    
    # Shuffle the password list to ensure random distribution
    secrets.SystemRandom().shuffle(password)
    
    return ''.join(password)

# Example usage
password = generate_secure_password(length=16, include_uppercase=True, include_digits=True, include_symbols=True)
print("Generated secure password:", password)
