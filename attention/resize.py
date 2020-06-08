from PIL import Image
import matplotlib.pyplot as plt
img2 = Image.open("1-5.png")
img2 = img2.convert('RGBA')
img2=img2.resize((320, 240))
for i in range (0,320):
	for j in range (0,240):
		img2.putpixel((i, j), (img2.getpixel((i, j))[0]-20, img2.getpixel((i, j))[1]-20, img2.getpixel((i, j))[2]-20,img2.getpixel((i, j))[3]+10))
plt.imshow(img2)
plt.show()
img2.save("1-5.png")