from PIL import Image
import skimage.io
import math
def blend_two_images():

	width=240
	height=280
	img1 = Image.open("1.jpg")
	img1 = img1.convert('RGBA')
	img1=img1.resize((320, 240))
	max=10
	min=10

	img2 = Image.open("2.jpg")
	img2 = img2.convert('RGBA')
	img2=img2.resize((320, 240))
	for i in range (0,320):
		for j in range (0,240):
			if img1.getpixel((i, j))[1]>max:
				max=img1.getpixel((i, j))[1]
			if img1.getpixel((i, j))[1]<min:
				min=img1.getpixel((i, j))[1]
			img2.putpixel((i, j), (img2.getpixel((i, j))[0], img2.getpixel((i, j))[1], img2.getpixel((i, j))[2],
								  int(math.pow(img1.getpixel((i, j))[1], 1.25))))

	print max
	print min





	import matplotlib.pyplot as plt
	plt.imshow(img2)
	plt.show()
	img2.save("test.png")


	return

if __name__ == '__main__':
	blend_two_images()