from PIL import Image

'''
Dilate binary image using a structuring element
originalImage (+) structuringElement = {(x,y) el. N^2 | ^B(x,y) intersect A != emptyset  }
with A = all black pixels
'''


def dilate_binary_image(input_image, output_map, structuring_element):
    for y in range(0, input_image.size[1]):
        for x in range(0, input_image.size[0]):
            # print("({},{}) {}".format(x, y, pixelColor))

            # Go through all potions in the structuring element relative to x y
            for p in structuring_element:
                u = x + p[0]
                v = y + p[1]

                # Check if u and v are inside the image size
                if 0 <= u < input_image.size[0] and 0 <= v < input_image.size[1]:

                    # if the pixel is black at u,v change the center to black and get out of the loop
                    if input_image.getpixel((u, v))[0] == 0:
                        output_map[x, y] = (0, 0, 0, 255)
                        break


binaryImagePath = "C:/Users/aless/Desktop/original.png"
binaryImage = Image.open(binaryImagePath)

imagePath = "C:/Users/aless/Desktop/image.png"
image = Image.new("RGB", binaryImage.size, "white")
imageMap = image.load()

structuringElement = {(0, 0), (-1, 0), (1, 0), (0, 1), (0, -1)}
structuringElement2 = {(-2, 0), (2, 0), (0, 2), (0, -2)}
structuringElement3 = {(0, 5)}

dilate_binary_image(binaryImage, imageMap, structuringElement)

image.show()
