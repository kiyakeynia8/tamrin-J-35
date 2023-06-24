from PIL import Image, ImageDraw, ImageFont, ImageOps
import matplotlib.pyplot as plt

# with Image.open("input/rgb.jpg").convert("RGBA") as base:
#     txt = Image.new("RGBA", base.size, (255, 255, 255, 0))
#     fnt = ImageFont.truetype("input/FreeMono.otf", 40)
#     d = ImageDraw.Draw(txt)

#     d.text((10, 150), "Hello", font=fnt, fill=(255, 255, 255, 128))
#     d.text((70, 190), "World", font=fnt, fill=(255, 255, 255, 255))

#     out = Image.alpha_composite(base, txt)
#     out.show()



# image = Image.open("input/rgb.jpg")

# r, g, b = image.split()
# r_hist = r.histogram()
# g_hist = g.histogram()
# b_hist = b.histogram()
# plt.plot(r_hist, color='red')
# plt.plot(g_hist, color='green')
# plt.plot(b_hist, color='blue')
# plt.show()



# image_e = ImageOps.equalize(Image.open("input/rgb.jpg"))
# image_e = ImageOps.equalize(Image.open("input/image_microsoft.png"))
# image_e = ImageOps.equalize(Image.open("input/rubik.png"))
# r, g, b = image_e.split()
# r_hist = r.histogram()
# g_hist = g.histogram()
# b_hist = b.histogram()
# plt.plot(r_hist, color='red')
# plt.plot(g_hist, color='green')
# plt.plot(b_hist, color='blue')
# plt.show()



# image_gray = ImageOps.grayscale(Image.open("input/rgb.jpg"))
# plt.imshow(image_gray, cmap='gray')
# plt.show()



# image_gray = ImageOps.grayscale(Image.open("input/rgb.jpg"))
# plt.plot(image_gray.histogram())
# plt.show()



image_gray = ImageOps.grayscale(Image.open("input/rgb.jpg"))
image_gray_e = ImageOps.equalize(image_gray, mask=None)
plt.plot(image_gray_e.histogram())
plt.show()