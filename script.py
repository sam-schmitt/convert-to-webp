from PIL import Image
import os
import sys

def convert_to_webp(src_folder, dest_folder):
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    for file in os.listdir(src_folder):
        file_ext = file.lower().split('.')[-1]
        supported_extensions = ['png', 'jpg', 'jpeg']

        if file_ext in supported_extensions:
            image = Image.open(os.path.join(src_folder, file))
            webp_image_name = file.rsplit('.', 1)[0] + '.webp'
            image.save(os.path.join(dest_folder, webp_image_name), 'webp')
        else:
            print(f"Does not handle {file_ext}")

if __name__ == '__main__':

    src_folder = "./input"
    dest_folder = "./output"

    if not os.path.exists(src_folder):
        print(f"Source folder '{src_folder}' does not exist.")
        sys.exit(1)

    convert_to_webp(src_folder, dest_folder)
    print(f"Images from '{src_folder}' have been converted to WebP format and saved in '{dest_folder}'.")
