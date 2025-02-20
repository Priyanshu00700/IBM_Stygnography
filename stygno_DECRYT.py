import cv2

# Load encrypted image
image_path = "encryptedImage.png"
img = cv2.imread(image_path)

# Check if image is loaded
if img is None:
    print(f"Error: Image '{image_path}' not found. Run 'encrypt.py' first.")
    exit()


# User input for decryption
pas = int(input("Enter passcode for decryption: "))

c = {}  # Number to character mapping
for i in range(255):
    c[i+1] = chr(i)

height, width, _ = img.shape
# Decode message
message = ""
m, n, z = 0, 0, 0

while True:
    char_code = img[n, m, z]
    
    if char_code == 0:  # Assuming 0 as stopping point
        break
    
    message += c[char_code-pas%17]

    m += pas%23+1
    if m >= width:
        m = 0
        n += 1

    z = (z + 1) % 3  # Change color channel

print("Decrypted message:", message)