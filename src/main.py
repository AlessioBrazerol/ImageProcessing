from PIL import Image

originalImagePath = "C:/Users/aless/Desktop/original.png"
originalImage = Image.open(originalImagePath)

imagePath = "C:/Users/aless/Desktop/image.png"
image = Image.new("RGB",originalImage.size,"white")

image.save(imagePath)
