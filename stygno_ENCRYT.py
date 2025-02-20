import cv2
import os

# Load image
image_path = r"Screenshot.png"  # Use correct path
img = cv2.imread(image_path)

# Check if image is loaded properly
if img is None:
    print(f"Error: Image '{image_path}' not found. Check the file path.")
    exit()

msg = input("Enter secret message: ")
password = int(input("Enter a passcode: "))

d = {}  # Character to number mapping

for i in range(255):
    d[chr(i)] = i+1

height, width, _ = img.shape
total_pixels = height * width

# Check if message fits in image
if len(msg) > total_pixels:
    print("Error: Message is too long for this image.")
    exit()

m, n, z =0, 0, 0

# Encoding Message into Image
for i in range(len(msg)):
    img[n, m, z] = d[msg[i]]+password%17
    
    m += password%23+1
    if m >= width:  # Move to next row if needed
        m = 0
        n += 1

    z = (z + 1) % 3  # Change color channel

# Save Encrypted Image
cv2.imwrite("encryptedImage.png", img)
print("Message encrypted successfully! Saved as 'encryptedImage.png'.")

print("Passcode saved in 'password.txt'. Keep it safe!")