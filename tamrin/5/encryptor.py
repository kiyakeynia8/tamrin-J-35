import cv2
import numpy as np

def Encryptor(image):
    a,b,c = image.shape

    secret = np.random.randint(0, 256, (a, b, c), np.uint8)
    encrypted = cv2.bitwise_xor(image, secret)

    cv2.imwrite("tamrin/5/image/encrypted.bmp", encrypted)
    np.save("tamrin/5/image/secret.npy", secret)
    return encrypted