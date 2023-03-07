from PIL import Image, ImageFilter
import os

def blur_image():
    # Check if 'input' directory exists
    if not os.path.exists('../input'):
        print("\033[91m" + "Error: 'input' directory does not exist.")
        return

    # Get all image files in 'input' directory
    files_to_blur = [f for f in os.listdir("../input") if os.path.isfile(os.path.join("../input", f))]
    
    if not files_to_blur:
        print("\033[93m" + "No image files found in 'input' directory.")
        return
    
    # Loop until user enters a valid blur radius
    while True:
        blur_radius = input("\nEnter blur radius (integer value): ")
        try:
            blur_radius = int(blur_radius)
            break
        except ValueError:
            print("\033[91m" + "Error: Invalid blur radius input. Must be an integer.")

    # Create the directory for the blurred images
    if not os.path.exists("../output"):
        os.makedirs("../output")
    
    # Loop through each image file and blur it
    for filename in files_to_blur:
        try:
            i = Image.open(os.path.join("../input", filename))
            fn, fext = os.path.splitext(filename)
            output_filename = f"{fn}_blurred{fext}"
            suffix = 1
            while os.path.exists(os.path.join("../output", output_filename)):
                output_filename = f"{fn}_blurred({suffix}){fext}"
                suffix += 1
            i.filter(ImageFilter.GaussianBlur(blur_radius)).save(os.path.join("../output", output_filename))
            print("\033[92m" + f"Successfully blurred {filename} and saved as {output_filename}")
        except Exception as e:
            print("\033[91m" + f"Error blurring {filename}: {str(e)}")


if __name__ == "__main__":
    blur_image()

