# Caesar Cipher Encoder & Decoder 🔐  

This Python program implements a **Caesar Cipher** encryption and decryption system. It allows users to encode text with a randomly generated shift key and later decode it using the provided key.  

## Features ✨  
✔ **Encode Mode:** Encrypts text using a randomly generated shift value (1-25) and appends the key for reference.  
✔ **Decode Mode:** Decrypts text using the provided shift key.  
✔ **Supports Upper & Lowercase Letters:** Keeps non-alphabetic characters unchanged.  
✔ **User-Friendly Interface:** Simple text-based input and output for easy interaction.  

## How It Works ⚙️  
1. Run the script and choose between encoding (`e`) or decoding (`d`).  
2. If encoding, enter your text; the program encrypts it and displays the encoded message with the key.  
3. If decoding, provide the encoded text and the key to retrieve the original message.  

## Example Usage 🛠  
### Encoding:  
```
Do you want to encode or decode a text? (e/d): e
Enter the text you want to encode: HelloWorld
Encoded Text: KhoorZruog | Key:3
```
### Decoding:  
```
Do you want to encode or decode a text? (e/d): d
Enter the encoded text (without key): KhoorZruog
Enter the key for decoding: 3
Decoded Text: HelloWorld
```

## Technologies Used 🖥️  
- Python  
- Random Library for Key Generation  

## Future Improvements 🚀  
- Support for automatic key retrieval from the encoded message.  
- Option to encrypt/decrypt entire files.  
- GUI implementation for better usability.  

Feel free to contribute or suggest improvements! 😊  
