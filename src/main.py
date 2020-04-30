from PIL import Image

'''
Dilate binary image using a structuring element
originalImage (+) structuringElement = {(x,y) el. N^2 | ^B(x,y) intersect A != emptyset  }
with A = all black pixels
'''
def dilateBinaryImage():
    for y in range(0, size[1]):
        for x in range(0, size[0]):
            pixelColor = originalImage.getpixel((x, y))[0]
            # print("({},{}) {}".format(x, y, pixelColor))

            # Go through all potions in the structuring element relative to x y
            for p in structuringElement:
                u = x + p[0]
                v = y + p[1]

                # Check if u and v are inside the image size
                if 0 <= u < size[0] and 0 <= v < size[0]:

                    # if the pixel is black at u,v change the center to black and get out of the loop
                    if originalImage.getpixel((u, v))[0] == 0:
                        imageMap[x, y] = (0, 0, 0, 255)

                        break;





originalImagePath = "C:/Users/aless/Desktop/original.png"
originalImage = Image.open(originalImagePath)

imagePath = "C:/Users/aless/Desktop/image.png"
image = Image.new("RGB",originalImage.size,"white")
imageMap = image.load()

size = originalImage.size

structuringElement = {(0, 0), (-1, 0), (1, 0), (0, 1), (0, -1)}

dilateBinaryImage()

image.show()
