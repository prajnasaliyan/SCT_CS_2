from PIL import Image
import numpy as np

# -----------------------------
# SIMPLE IMAGE ENCRYPTION TOOL
# -----------------------------

def encrypt_image(input_path, output_path, key):
    # Load image
    img = Image.open(input_path)
    arr = np.array(img)

    # Flatten pixels for easy operations
    flat = arr.reshape(-1, 3)   # Only RGB

    # --- 1) Simple Pixel Swapping ---
    np.random.seed(key)    # use key for reproducible swapping
    np.random.shuffle(flat)

    # --- 2) Simple Math Operation (XOR with key) ---
    flat = flat ^ (key % 256)

    # Reshape back to original
    encrypted = flat.reshape(arr.shape)

    # Save output
    Image.fromarray(encrypted).save(output_path)
    print(f"Image encrypted and saved as {output_path}")


def decrypt_image(input_path, output_path, key):
    # Load encrypted image
    img = Image.open(input_path)
    arr = np.array(img)

    # Flatten
    flat = arr.reshape(-1, 3)

    # --- Reverse XOR ---
    flat = flat ^ (key % 256)

    # --- Reverse pixel swapping ---
    # We generate the same order again and reverse it
    np.random.seed(key)
    order = np.arange(len(flat))
    np.random.shuffle(order)

    # Create empty array to place pixels back
    original = np.zeros_like(flat)
    original[order] = flat

    # Reshape back to original
    decrypted = original.reshape(arr.shape)

    Image.fromarray(decrypted).save(output_path)
    print(f"Image decrypted and saved as {output_path}")


# -----------------------------
# Run example
# -----------------------------
if __name__ == "__main__":
    print("Simple Image Encryption Tool")

    choice = input("Encrypt or Decrypt (e/d): ")

    if choice.lower() == "e":
        encrypt_image("/home/kali/Downloads/cat.png", "encrypted.png", key=123)
    else:
        decrypt_image("encrypted.png", "decrypted.png", key=123)
