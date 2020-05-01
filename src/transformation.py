from PIL import Image
import numpy as np


def affine_transform(input_image, affine_matrix):
    output_image = Image.new("RGB", input_image.size, "white")
    image_map = output_image.load()

    # Look at all pixel in the original Image
    for y in range(1, input_image.size[1]+1):
        for x in range(1, input_image.size[0]+1):

            # Calculate the transformed position
            pos_new = np.dot([[x, y, 1]], affine_matrix)
            # Normalize new positions
            pos_new = (int(pos_new[0][0]) % (input_image.size[0]), int(pos_new[0][1]) % (input_image.size[1]))

            # Check if new pos in image, this should always be true
            if 0 <= pos_new[0] < (input_image.size[0]) and 0 <= pos_new[1] < (input_image.size[1]):
                # Set the color to the color from the new position
                image_map[x-1, y-1] = input_image.getpixel((pos_new[0], pos_new[1]))

    return output_image


def transform(input_image, affine_matrix):
    output_image = Image.new("RGB", input_image.size, "white")
    image_map = output_image.load()

    # Look at all pixel in the original Image
    for y in range(1, input_image.size[1] + 1):
        for x in range(1, input_image.size[0] + 1):

            # Calculate the transformed position
            pos_new = [[x+affine_matrix[0][0], y+affine_matrix[0][1]]]

            # Normalize new positions
            pos_new = (int(pos_new[0][0]) % (input_image.size[0]), int(pos_new[0][1]) % (input_image.size[1]))

            # Check if new pos in image, this should always be true
            if 0 <= pos_new[0] < (input_image.size[0]) and 0 <= pos_new[1] < (input_image.size[1]):
                # Set the color to the color from the new position
                image_map[x - 1, y - 1] = input_image.getpixel((pos_new[0], pos_new[1]))

    return output_image
