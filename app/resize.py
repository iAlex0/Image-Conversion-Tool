import os
from PIL import Image

def resize_images():
    # Check if 'input' directory exists
    if not os.path.exists('../input'):
        print("\033[91m" + "Error: 'input' directory does not exist.")
        return

    # Get all image files in 'input' directory
    files_to_resize = [f for f in os.listdir("../input") if os.path.isfile(os.path.join("../input", f))]
    
    if not files_to_resize:
        print("\033[93m" + "No image files found in 'input' directory.")
        return
    
    # Get resize dimensions from user input
    while True:
        try:
            resize_input = input("\nEnter resize dimensions (in the form 'width x height' (e.g. 300x300)): ")
            resize_dimensions = tuple(map(int, resize_input.split('x')))
            break
        except ValueError:
            print("\033[91m" + "Error: Invalid resize dimensions. Must be in the form 'width x height'.")
            continue

    # Create the directory for the resized images
    if not os.path.exists("../output"):
        os.makedirs("../output")
    
    # Loop through each image file and resize it
    for filename in files_to_resize:
        try:
            i = Image.open(os.path.join("../input", filename))
            fn, fext = os.path.splitext(filename)
            resized_image = i.resize(resize_dimensions)
            resized_filename = f"{fn}_resized_{resize_input}{fext}"
            counter = 1
            while os.path.exists(os.path.join("../output", resized_filename)):
                resized_filename = f"{fn}_resized_{resize_input}({counter}){fext}"
                counter += 1
            resized_image.save(os.path.join("../output", resized_filename))
            print("\033[92m" + f"Successfully resized {filename} to {resized_filename}")
        except Exception as e:
            print("\033[91m" + f"Error resizing {filename}: {str(e)}")


if __name__ == "__main__":
    resize_images()
