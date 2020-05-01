from PIL import Image


def convolution(input_image, structuring_element):
    # Create the output image and load it
    output_image = Image.new("RGB", input_image.size, "white")
    image_map = output_image.load()



    return output_image
