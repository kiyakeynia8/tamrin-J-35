import cv2
import numpy as np

def Decryptor(image):
    image = cv2.imread("tamrin/5/image/encrypted.bmp")
    secret = np.load("tamrin/5/image/secret.npy")

    decrypted = cv2.bitwise_xor(image, secret)
    return decrypted