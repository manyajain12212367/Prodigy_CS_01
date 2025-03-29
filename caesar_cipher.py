import random

def caesar_cipher(text, shift):
    result = ""

    for char in text:
        # Checking if the character is an uppercase letter
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Checking if the character is a lowercase letter
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char

    return result

def encode(text):
    shift = random.randint(1, 25)  # Generating a random shift key
    encoded_text = caesar_cipher(text, shift)
    # Appending the key at the end of the encoded text
    return f"{encoded_text} | Key:{shift}"

def decode(encoded_text, shift):
    return caesar_cipher(encoded_text, -shift)


if __name__ == "__main__":
    # Asking the user for their choice
    choice = input("Do you want to encode or decode a text? (e/d): ").strip().lower()

    if choice == 'e':
        # Getting the text from the user to encode
        user_text = input("Enter the text you want to encode: ")
        # Encoding the text
        encoded_text = encode(user_text)
        print("Encoded Text:", encoded_text)
    elif choice == 'd':
        # Getting encoded text from the user to decode
        user_encoded_text = input("Enter the encoded text (without key): ")
        # Asking for the key
        key = int(input("Enter the key for decoding: "))
        # Decoding the text
        decoded_text = decode(user_encoded_text, key)
        print("Decoded Text:", decoded_text)
    else:
        print("Invalid choice. Please enter 'e' for encode or 'd' for decode.")