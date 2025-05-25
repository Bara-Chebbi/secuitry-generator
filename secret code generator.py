# Ask the user to enter a word for encryption
word = input("Enter a word to encrypt: ")

# Ask the user to enter a shift number (how many letters to shift)
shift = int(input("Enter shift number (e.g., 1, 2, 3): "))

# Initialize an empty string to store the encrypted word
encrypted = ""

# Loop through each letter in the original word
for char in word:
    # Check if the character is an uppercase letter
    if char.isupper():
        # Shift the letter forward by converting it to ASCII, shifting, and converting back
        encrypted += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
    # Check if the character is a lowercase letter
    elif char.islower():
        # Shift the letter forward for lowercase similarly
        encrypted += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
    else:
        # If it's not a letter, keep it the same (like space or punctuation)
        encrypted += char

# Show the encrypted word to the user
print("Encrypted word:", encrypted)

# Initialize an empty string to store the decrypted word
decrypted = ""

# Loop through each letter in the encrypted word
for char in encrypted:
    # Check if the character is an uppercase letter
    if char.isupper():
        # Shift the letter backward by converting it to ASCII, shifting, and converting back
        decrypted += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
    # Check if the character is a lowercase letter
    elif char.islower():
        # Shift the letter backward for lowercase similarly
        decrypted += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
    else:
        # If it's not a letter, keep it the same
        decrypted += char

# Show the decrypted word to verify it matches the original
print("Decrypted word:", decrypted)
