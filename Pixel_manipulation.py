from PIL import Image

def get_user_input(prompt):
    while True:
        user_input = input(prompt)
        if user_input:
            return user_input
        print("Invalid input. Please try again.")

def encrypt_image(image_path, encrypted_image_path, key):
    try:
        print(f"Encrypting image: {image_path} -> {encrypted_image_path}")
        image = Image.open(image_path)
        pixels = image.load()
        for x in range(image.size[0]):
            for y in range(image.size[1]):
                pixel_value = pixels[x, y]
                encrypted_pixel_value = tuple((val + key) % 256 for val in pixel_value)
                pixels[x, y] = encrypted_pixel_value
        image.save(encrypted_image_path)
        print("Image encrypted successfully!")
    except Exception as e:
        print(f"Error encrypting image: {e}")

def decrypt_image(encrypted_image_path, decrypted_image_path, key):
    try:
        print(f"Decrypting image: {encrypted_image_path} -> {decrypted_image_path}")
        image = Image.open(encrypted_image_path)
        pixels = image.load()
        for x in range(image.size[0]):
            for y in range(image.size[1]):
                pixel_value = pixels[x, y]
                decrypted_pixel_value = tuple((val - key) % 256 for val in pixel_value)
                pixels[x, y] = decrypted_pixel_value
        image.save(decrypted_image_path)
        print("Image decrypted successfully!")
    except Exception as e:
        print(f"Error decrypting image: {e}")

def main():
    while True:
        print("Image Encryption Tool")
        print("1. Encrypt an image")
        print("2. Decrypt an image")
        print("3. Quit")
        choice = get_user_input("Enter your choice: ")
        if choice == '1':
            image_path = get_user_input("Enter the path to the image: ")
            encrypted_image_path = get_user_input("Enter the path to save the encrypted image: ")
            key = int(get_user_input("Enter the encryption key: "))
            encrypt_image(image_path, encrypted_image_path, key)
        elif choice == '2':
            encrypted_image_path = get_user_input("Enter the path to the encrypted image: ")
            decrypted_image_path = get_user_input("Enter the path to save the decrypted image: ")
            key = int(get_user_input("Enter the decryption key: "))
            decrypt_image(encrypted_image_path, decrypted_image_path, key)
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

