from PIL import Image




outputPath = "C:/Users/aless/Desktop/image.png"
binaryImagePath = "C:/Users/aless/Desktop/original.png"
binaryImage = Image.open(binaryImagePath)

structuringElement = {(0, 0), (-1, 0), (1, 0), (0, 1), (0, -1)}
structuringElement2 = {(-2, 0), (2, 0), (0, 2), (0, -2), (0, 0)}
structuringElement3 = {(0, 5)}

image1 = dilate_binary_image(binaryImage, structuringElement)
image2 = erode_binary_image(image1, structuringElement)

image1.show()
image2.show()
# image.save(outputPath);
