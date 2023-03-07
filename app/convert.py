import os
from PIL import Image

def convert_images():
    # Check if 'input' directory exists
    if not os.path.exists('../input'):
        print("\033[91m" + "Error: 'input' directory does not exist.")
        return

    # Get all image files in 'input' directory
    files_to_convert = [f for f in os.listdir("../input") if os.path.isfile(os.path.join("../input", f))]
    
    if not files_to_convert:
        print("\033[93m" + "No image files found in 'input' directory.")
        return
    
    # Print conversion options
    print("\nConversion Options:\n1. webp\n2. png\n3. jpeg\n4. bmp")

    while True:
        # Get conversion option from user input
        conversion_choice = input("\nEnter conversion choice (1-4): ")

        # Set output format based on user choice
        if conversion_choice == "1":
            output_format = "webp"
            break
        elif conversion_choice == "2":
            output_format = "png"
            break
        elif conversion_choice == "3":
            output_format = "jpeg"
            break
        elif conversion_choice == "4":
            output_format = "bmp"
            break
        else:
            print("\033[91m" + "Error: Invalid conversion choice. Must be a number from 1 to 4.")
            continue

    # Create the directory for the converted images
    if not os.path.exists("../output"):
        os.makedirs("../output")
    
    # Loop through each image file and convert it
    for filename in files_to_convert:
        try:
            i = Image.open(os.path.join("../input", filename))
            fn, fext = os.path.splitext(filename)
            converted_filename = f"{fn}_converted.{output_format}"
            counter = 1
            while os.path.exists(os.path.join("../output", converted_filename)):
                converted_filename = f"{fn}_converted({counter}).{output_format}"
                counter += 1
            i.save(os.path.join("../output", converted_filename), format=output_format)
            print("\033[92m" + f"Successfully converted {filename} to {converted_filename}")
        except Exception as e:
            print("\033[91m" + f"Error converting {filename}: {str(e)}")


if __name__ == "__main__":
    convert_images()
