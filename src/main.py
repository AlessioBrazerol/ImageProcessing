from PIL import Image
from math import cos,sin
from src.binaryimageprocessing import dilate_binary_image, erode_binary_image
from src.convolution import  convolution

outputPath = "C:/Users/aless/Desktop/image.png"
binaryImagePath = "C:/Users/aless/Desktop/original.png"
binaryImage = Image.open(binaryImagePath)

structuringElement = {(0, 0), (-1, 0), (1, 0), (0, 1), (0, -1)}
structuringElement2 = {(-2, 0), (2, 0), (0, 2), (0, -2), (0, 0)}
structuringElement3 = {(0, 5)}

image1 = dilate_binary_image(binaryImage, structuringElement)
image2 = erode_binary_image(image1, structuringElement)

# image1.show()
# image2.show()
# image.save(outputPath);

lennaImagePath = "C:/Users/aless/Desktop/image2.jpg"
lennaImage = Image.open(lennaImagePath)

spatiaLowpassMatrix = [[1, 1, 1],
                       [1, 1, 1],
                       [1, 1, 1]]

spatiaLowpass = (spatiaLowpassMatrix, (1, 1), True)

spatialHighpassMatrix = [[0, -1, 0],
                         [-1, 4, -1],
                         [0, -1, 0]]

spatialHighpass = (spatialHighpassMatrix, (1, 1), False)

sharpenMatrix = [[0, -1, 0],
                 [-1, 5, -1],
                 [0, -1, 0]]

sharpen = (sharpenMatrix, (1, 1), False)

gaussianBlur3x3Matrix = [[1, 2, 1],
                         [2, 4, 2],
                         [1, 2, 1]]

gaussianBlur3x3 = (gaussianBlur3x3Matrix, (1, 1), True)

gaussianBlur5x5Matrix = [[1, 4, 6, 4, 1],
                         [4, 16, 24, 16, 4],
                         [6, 24, 36, 24, 6],
                         [4, 16, 24, 16, 4],
                         [1, 4, 6, 4, 1]]

gaussianBlur5x5 = (gaussianBlur5x5Matrix, (1, 1), True)

lenaCopy = convolution(lennaImage, spatiaLowpass)
lenaCopy.show("spatiaLowpass")

lenaCopy = convolution(lennaImage, spatialHighpass)
lenaCopy.show("spatialHighpass")

lenaCopy = convolution(lennaImage, sharpen)
lenaCopy.show("sharpen")

lenaCopy = convolution(lennaImage, gaussianBlur3x3)
lenaCopy.show("gaussianBlur3x3")

lenaCopy = convolution(lennaImage, gaussianBlur5x5)
lenaCopy.show("gaussianBlur5x5")

