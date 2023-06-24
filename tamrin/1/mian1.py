import cv2

image = cv2.imread("input/image_microsoft.png")
image_a = cv2.cvtColor(image,cv2.COLOR_BGR2BGRA)

for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        if image[i,j,0] == 85 and image[i,j,1] == 85 and image[i,j,2] == 85:
            image_a[i,j,3] = 0

cv2.imwrite("output/1_output.png", image_a)