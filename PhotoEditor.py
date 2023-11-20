
#! ! ! -IMPORTANT NOTE- ! ! ! 
#The image window will appear in the top left corner of your
#desktop, likely BEHIND your currently opened windows.

import cv2
import numpy as np
import platform

def main():
    menu_options_choice = 0
    image_name = input("Please choose a jpeg from your images to edit, and move it into the same folder as this Python file. What is the exact name of your image file? (Recommended - Nyan_cat.jpeg): ")
    try:
        image = cv2.imread(image_name)
        height, width, depth = image.shape
    except:
        print()
        print("Error: File not recognized. Please ensure the file was placed in the same folder as this program and was inputted correctly. Do not include parentheses when inputting the file name.")
    print()
    while menu_options_choice != 4:
        menu_options_choice = int(input("Please choose from the following editing options:\n1. Invert Colors\n2. Find and Replace a Color\n3. Resize Image (please perform this last)\n4. Quit Program\n(Enter a number): "))
        if menu_options_choice == 1:
            invert_colors(image, height, width, depth)
        elif menu_options_choice == 2:
            find_and_replace(image, height, width)
        elif menu_options_choice == 3:
            resize_image(image, height, width)
    print()
    print("Thank you for using Python Photo Editor. Have a nice day.")



def invert_colors(image, height, width, depth):
    for i in range(height):
        for j in range(width):
            for c in range(depth):
                image[i,j,c] = 255 - image[i,j,c]

    cv2.imshow("window", image)
    cv2.waitKey(1)

    move_window_to_top_left()

    return image


def find_and_replace(image, height, width):
    print()
    print("Open this link and select a color that closely resembles the one you'd like to replace in the image ---> https://htmlcolorcodes.com/color-picker/ ")
    red_user_input_remove = int(input("What is the RGB value for RED?: "))
    green_user_input_remove = int(input("What is the RGB value for GREEN?: "))
    blue_user_input_remove = int(input("What is the RGB value for BLUE?: "))
    print()
    print("Color recorded.")
    print()
    print("Once again, navigate to the website. Choose a new color to replace the color you removed.")
    red_user_input_paint = int(input("What is the new RGB value for RED?: "))
    green_user_input_paint = int(input("What is the new RGB value for GREEN?: "))
    blue_user_input_paint = int(input("What is the new RGB value for BLUE?: "))
    print()
    print("Color recorded.\n\nEditing...(This may take some time)")
    print()
    color_to_replace = [blue_user_input_remove, green_user_input_remove, red_user_input_remove]
    replacement_color = [blue_user_input_paint, green_user_input_paint, red_user_input_paint]

    for i in range(height):
        for j in range(width):
            pixel = image[i, j]
            if np.allclose(pixel, color_to_replace, atol=60):
                image[i, j] = replacement_color

    cv2.imshow("window", image)
    cv2.waitKey(1)

    move_window_to_top_left()

    return image


def resize_image(image, height, width):
    current_height_and_width = print(f"The current dimensions of your image:\n Height: {height} pixels\n Width: {width} pixels\n")
    print(current_height_and_width)
    user_height = int(input("What is the new height you'd like to set for your image? (in pixels): "))
    user_width = int(input("What is the new width you'd like to set for your image? (in pixels): "))
    image = cv2.resize(image, (user_height, user_width))

    cv2.namedWindow("window", cv2.WINDOW_NORMAL)  # Create window with resize capability
    cv2.imshow("window", image)
    cv2.waitKey(1)

    move_window_to_top_left()

    return image

def move_window_to_top_left():
    current_platform = platform.system()
    if current_platform == "Windows":
        cv2.moveWindow("window", 0, 0)  # Move window to top left corner on Windows
    elif current_platform == "Linux":
        cv2.moveWindow("window", 0, 0)  # Move window to top left corner on Linux
    elif current_platform == "Darwin":
        cv2.moveWindow("window", 0, 22) # Move window to top left corner on Mac
    
main()
