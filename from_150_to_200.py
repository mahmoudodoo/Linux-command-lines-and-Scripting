import os
from PIL import Image
import shutil

def copy_images(src_dir, dest_dir, min_width, max_width):
    # Create the destination directory if it doesn't exist
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # Walk through all directories and copy images
    for root, dirs, files in os.walk(src_dir):
        for file in files:
            if file.lower().endswith(".png"):
                image_path = os.path.join(root, file)
                try:
                    with Image.open(image_path) as img:
                        width, _ = img.size
                        if min_width <= width <= max_width:
                            dest_path = os.path.join(dest_dir, file)
                            shutil.copy2(image_path, dest_path)
                            print(f"Copied: {file}")
                except Exception as e:
                    print(f"Error processing {file}: {e}")

if __name__ == "__main__":
    src_directory = os.getcwd()  # Current working directory
    dest_directory = "from_150_to_200"
    min_width = 150
    max_width = 200

    copy_images(src_directory, dest_directory, min_width, max_width)
