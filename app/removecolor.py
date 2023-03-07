import os
from PIL import Image

def convert_to_bw():
    # Check if 'input' directory exists
    if not os.path.exists('../input'):
        print("\033[91m" + "Error: 'input' directory does not exist.")
        return

    # Get all image files in 'input' directory
    files_to_convert = [f for f in os.listdir("../input") if os.path.isfile(os.path.join("../input", f))]
    
    if not files_to_convert:
        print("\033[93m" + "No image files found in 'input' directory.")
        return
    
    # Create the directory for the converted images
    if not os.path.exists("../output"):
        os.makedirs("../output")

    # Loop through each image file and convert it to black and white
    for filename in files_to_convert:
        try:
            i = Image.open(os.path.join("../input", filename))
            fn, fext = os.path.splitext(filename)
            converted_filename = f"{fn}_bw{fext}"
            counter = 1
            while os.path.exists(os.path.join("../output", converted_filename)):
                converted_filename = f"{fn}_bw({counter}){fext}"
                counter += 1
            bw_image = i.convert("L")
            bw_image.save(os.path.join("../output", converted_filename))
            print("\033[92m" + f"Successfully converted {filename} to black and white and saved as {converted_filename}")
        except Exception as e:
            print("\033[91m" + f"Error converting {filename}: {str(e)}")



if __name__ == "__main__":
    convert_to_bw()