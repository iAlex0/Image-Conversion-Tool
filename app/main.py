import resize
import removecolor
import blur
import rotate
import convert

def main():
    while True:
        try:
            choice = int(input("Enter the number for the action you want to perform:\n\n1. Resize image\n2. Remove color from image\n3. Blur image\n4. Rotate image\n5. Convert image format\n\n- "))
            if choice not in range(1, 6):
                raise ValueError
            break
        except ValueError:
            print("\033[91m" + "Error: Invalid choice. Enter a number between 1 and 5.")
            continue

    if choice == 1:
        resize.resize_images()
    elif choice == 2:
        removecolor.convert_to_bw()
    elif choice == 3:
        blur.blur_image()
    elif choice == 4:
        rotate.rotate_images()
    elif choice == 5:
        convert.convert_images()

if __name__ == "__main__":
    main()
