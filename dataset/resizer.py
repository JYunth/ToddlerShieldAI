import cv2
import os

input_folder = '/home/jyunth/repos/ToddlerShieldAI/dataset/own_test'  # Replace with the path to your input folder
output_folder = '/home/jyunth/repos/ToddlerShieldAI/dataset/own_test_resized'  # Replace with the path to your output folder

output_size = (64, 64)

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Iterate through the images in the input folder
for image_name in os.listdir(input_folder):
    image_path = os.path.join(input_folder, image_name)

    # Read the image using OpenCV
    image = cv2.imread(image_path)

    # Resize the image
    resized_image = cv2.resize(image, output_size)

    # Save the resized image to the output folder
    output_path = os.path.join(output_folder, image_name)
    cv2.imwrite(output_path, resized_image)