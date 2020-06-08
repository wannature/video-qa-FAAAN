from PIL import Image

img1 = Image.open("./3/1.png")
img1 = img1.convert('RGBA')
img1=img1.resize((320, 240))
img1.save("./3/1.png")

img2 = Image.open("./3/2.png")
img2 = img2.convert('RGBA')
img2=img2.resize((320, 240))
img2.save("./3/2.png")

img3 = Image.open("./3/3.png")
img3 = img3.convert('RGBA')
img3=img3.resize((320, 240))
img3.save("./3/3.png")

img4 = Image.open("./3/4.png")
img4 = img4.convert('RGBA')
img4=img4.resize((320, 240))
img4.save("./3/4.png")

