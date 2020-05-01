from PIL import Image

'''
Dilate binary image using a structuring element
originalImage (+) structuringElement = {(x,y) el. N^2 | ^B(x,y) intersect A != emptyset  }
with A = all black pixels
'''


def dilate_binary_image(input_image, structuring_element):
    # Create the output image and load it
    output_image = Image.new("RGB", input_image.size, "white")
    image_map = output_image.load()
    
    # Look at all pixel in the original Image
    for y in range(0, input_image.size[1]):
        for x in range(0, input_image.size[0]):

            # Go through all potions in the structuring element relative to x y
            for p in structuring_element:
                u = x + p[0]
                v = y + p[1]

                # Check if u and v are inside the image size
                if 0 <= u < input_image.size[0] and 0 <= v < input_image.size[1]:

                    # if the pixel is black at u,v change the center to black and get out of the loop
                    if input_image.getpixel((u, v))[0] == 0:
                        image_map[x, y] = (0, 0, 0, 255)
                        break
    return output_image


'''
Erode binary image using a structuring element
originalImage (-) structuringElement = {(x,y} el N^2 | ^B(x,y) subset A
with A = all black pixel
'''


def erode_binary_image(input_image, structuring_element):
    # Create the output image and load it
    output_image = Image.new("RGB", input_image.size, "white")
    image_map = output_image.load()
    
    # Look at all pixel in the original Image
    for y in range(0, input_image.size[1]):
        for x in range(0, input_image.size[0]):

            # Go through all potions in the structuring element relative to x y
            overlaps_completely = True
            for p in structuring_element:
                u = x + p[0]
                v = y + p[1]

                # Check if u and v are inside the image size
                if 0 <= u < input_image.size[0] and 0 <= v < input_image.size[1]:

                    # If the pixel is white at u,v, break and set overlaps_completely to False
                    if input_image.getpixel((u, v))[0] == 255:
                        overlaps_completely = False
                        break

            # If the structuring element is overlapping completely set center to black
            if overlaps_completely:
                image_map[x, y] = (0, 0, 0, 255)
    return output_image
