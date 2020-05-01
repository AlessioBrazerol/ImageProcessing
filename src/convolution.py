from PIL import Image
from progress.bar import Bar


def convolution(input_image, structuring_element):
    # Create Progress Bar
    bar = Bar('Creating Image', max=input_image.size[0]*input_image.size[1])

    # Create the output image and load it
    output_image = Image.new("RGB", input_image.size, "white")
    image_map = output_image.load()

    # Get the structuring matrix and center of structuring element and normalize
    structuring_matrix = structuring_element[0]
    se_center = structuring_element[1]
    normalize = structuring_element[2]

    # Look at all pixel in the original Image
    for y in range(0, input_image.size[1]):
        for x in range(0, input_image.size[0]):

            color_new = (0, 0, 0)
            # Normalize amount, can change because of edge pixel
            n = 0

            # Go through all positions in the structuring_matrix
            for row_idx, row in enumerate(structuring_matrix):
                for column_idx in range(0, len(row)):
                    # print("({},{}) = {}".format(column_idx - se_center[0], row_idx - se_center[1], row[column_idx]))

                    # Calculate coordinates of pixels to check for structuring element
                    pixel_x = x + column_idx - se_center[0]
                    pixel_y = y + row_idx - se_center[1]

                    # Check if pixel_x and pixel_y are inside the image
                    if 0 <= pixel_x < input_image.size[0] and 0 <= pixel_y < input_image.size[1]:
                        # Create new color out of neighbour colors
                        factor = row[column_idx]

                        pixel_color = input_image.getpixel((pixel_x, pixel_y))
                        n += factor

                        # Check if gray-scale image
                        if isinstance(pixel_color, int):
                            color_temp = color_new[0] + factor * pixel_color
                            color_new = (color_temp, color_temp, color_temp)

                        else:
                            color_r = color_new[0] + factor * pixel_color[0]
                            color_g = color_new[1] + factor * pixel_color[1]
                            color_b = color_new[2] + factor * pixel_color[2]
                            color_new = (color_r, color_g, color_b)

            if normalize:
                color_new = (color_new[0] // n, color_new[1] // n, color_new[2] // n)

            color_new = (int(color_new[0]), int(color_new[1]), int(color_new[2]))

            image_map[x, y] = color_new
            bar.next()
    bar.finish()
    return output_image
