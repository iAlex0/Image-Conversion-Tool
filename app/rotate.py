import os
from PIL import Image

def rotate_images():
    # Check if 'input' directory exists
    if not os.path.exists('../input'):
        print("\033[91m" + "Error: 'input' directory does not exist.")
        return

    # Get all image files in 'input' directory
    files_to_rotate = [f for f in os.listdir("../input") if os.path.isfile(os.path.join("../input", f))]
    
    if not files_to_rotate:
        print("\033[93m" + "No image files found in 'input' directory.")
        return
    
    # Print rotation options
    print("\nRotation Options:\n1. 90 degrees clockwise\n2. 90 degrees counterclockwise\n3. 180 degrees\n4. Custom angle")

    while True:
        # Get rotation option from user input
        rotation_choice = input("\nEnter rotation choice (1-4): ")

        # Set rotation angle based on user choice
        if rotation_choice == "1":
            angle = 90
            break
        elif rotation_choice == "2":
            angle = -90
            break
        elif rotation_choice == "3":
            angle = 180
            break
        elif rotation_choice == "4":
            angle = input("Enter custom rotation angle (in degrees): ")
            try:
                angle = int(angle)
                break
            except ValueError:
                print("\033[91m" + "Error: Invalid angle input. Must be an integer.")
                continue
        else:
            print("\033[91m" + "Error: Invalid rotation choice. Must be a number from 1 to 4.")
            continue

    # Create the directory for the rotated images
    if not os.path.exists("../output"):
        os.makedirs("../output")
    
    # Loop through each image file and rotate it
    for filename in files_to_rotate:
        try:
            i = Image.open(os.path.join("../input", filename))
            fn, fext = os.path.splitext(filename)
            rotated_filename = f"{fn}_rotated{angle}{fext}"
            counter = 1
            while os.path.exists(os.path.join("../output", rotated_filename)):
                rotated_filename = f"{fn}_rotated{angle}({counter}){fext}"
                counter += 1
            rotated_image = i.rotate(angle, expand=True)
            rotated_image.save(os.path.join("../output", rotated_filename))
            print("\033[92m" + f"Successfully rotated {filename} and saved as {rotated_filename}")
        except Exception as e:
            print("\033[91m" + f"Error rotating {filename}: {str(e)}")


if __name__ == "__main__":
    rotate_images()
