# Prodigy_infotech-Task_02
Pixel manipulation 
# Image Encryption Tool - README

This is a simple Python-based image encryption and decryption tool that manipulates the pixel values of an image using a basic encryption algorithm. The tool allows users to encrypt and decrypt images by modifying the pixel values with a user-provided key. This README provides an overview of the tool, its functionality, and instructions on how to use it.

---

## Table of Contents
1. [Introduction]
2. [Features]
3. [Requirements]
4. [Usage]
5. [How It Works]
6. [Limitations]
7. [Contributing]

---

## Introduction

This tool is designed to demonstrate basic image manipulation and encryption techniques using Python. It uses the `Pillow` library (PIL) to handle image processing and allows users to encrypt and decrypt images by modifying the pixel values with a simple key-based algorithm.

The encryption process involves adding a key to each pixel value, while the decryption process subtracts the key to restore the original image. This is a basic form of encryption and is not intended for secure or sensitive data.

---

## Features

- **Image Encryption:** Encrypts an image by modifying its pixel values using a user-provided key.
- **Image Decryption:** Decrypts an encrypted image using the same key to restore the original image.
- **User-Friendly Interface:** Provides a simple command-line interface for users to interact with the tool.
- **Error Handling:** Includes basic error handling to manage issues during image processing.

## Requirements

To run this tool, you need the following:

- **Python 3.x**: The script is written in Python and requires Python 3.x to run.
- **Pillow Library**: The script uses the `Pillow` library for image processing. You can install it using pip:
  ```
  pip install pillow
  ```

---

2. **Install Dependencies**:
   Ensure you have the `Pillow` library installed:
   pip install pillow
   
4. **Run the Script**:
   You can run the script directly using Python:
   python Pixel_manipulation.py

## Usage

### Running the Tool
1. **Start the Tool**:
   Run the script using Python:
   ```bash
   python Pixel_manipulation.py
   ```

2. **Main Menu**:
   The tool will display a menu with the following options:
   ```
   Image Encryption Tool
   1. Encrypt an image
   2. Decrypt an image
   3. Quit
   ```

### Encrypting an Image
1. Choose option `1` from the menu.
2. Enter the path to the image you want to encrypt.
3. Enter the path where you want to save the encrypted image.
4. Enter an encryption key (an integer).
5. The tool will encrypt the image and save it to the specified path.

### Decrypting an Image
1. Choose option `2` from the menu.
2. Enter the path to the encrypted image.
3. Enter the path where you want to save the decrypted image.
4. Enter the decryption key (the same key used for encryption).
5. The tool will decrypt the image and save it to the specified path.

### Exiting the Tool
- Choose option `3` to quit the tool.

---

## How It Works

### Encryption Process
1. The tool opens the image using the `Pillow` library.
2. It iterates over each pixel in the image.
3. For each pixel, it adds the encryption key to the RGB values (or RGBA if the image has an alpha channel).
4. The pixel values are wrapped around using modulo 256 to ensure they stay within the valid range (0-255).
5. The modified image is saved as the encrypted image.

### Decryption Process
1. The tool opens the encrypted image.
2. It iterates over each pixel in the image.
3. For each pixel, it subtracts the decryption key from the RGB values.
4. The pixel values are wrapped around using modulo 256 to ensure they stay within the valid range (0-255).
5. The modified image is saved as the decrypted image.

---

## Limitations

- **Basic Encryption:** This tool uses a very simple encryption algorithm that is not secure for sensitive data. It is intended for educational purposes only.
- **Key Management:** The user must remember the exact key used for encryption to successfully decrypt the image.
- **Image Formats:** The tool works with common image formats supported by the `Pillow` library (e.g., PNG, JPEG).

## Contributing

Contributions are welcome! If you would like to improve this tool, feel free to open an issue or submit a pull request. Here are some ideas for improvements:
- Add support for more advanced encryption algorithms.
- Improve the user interface (e.g., GUI).
- Add error handling for invalid image formats or keys

---

## Acknowledgments

- **Pillow Library**: This tool relies on the `Pillow` library for image processing. You can learn more about it [here](https://python-pillow.org/).
- **Python**: The script is written in Python, a versatile and powerful programming language.

---

Enjoy using the Image Encryption Tool! If you have any questions or feedback, feel free to reach out.
