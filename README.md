Overview

This project is a beginner-friendly Image Encryption Tool that uses pixel manipulation techniques to hide image content.
It supports:

 Swapping pixel positions

 Applying a simple mathematical operation (XOR) on pixel values

These operations distort the image and make it unreadable without the correct key.
A valid key is required to reverse the operations and restore the original image.

This tool is mainly created for learning basic encryption concepts, image processing, and Python programming.


How It Works:

The program performs two encryption steps:

1️⃣ Pixel Swapping

The image is converted into a NumPy array.

All pixels are flattened into a single list.

The list is shuffled using a random seed based on the key.

This destroys the original structure of the image.

2️⃣ XOR Operation

Each pixel value is XORed with (key % 256)

XOR is reversible → the same operation is used during decryption.

Decryption

XOR is applied again.

The original pixel positions are restored using the same key.
# SCT_CS_2
