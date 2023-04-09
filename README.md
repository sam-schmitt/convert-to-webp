# Code to Convert Images to WebP

This code is a Python script that converts images from a source folder to the WebP image format and saves them in a destination folder. The code uses the Python Imaging Library (PIL) module to process the images.

## How to Use

To use this code, follow these steps:

1. Install the PIL module by running `pip install Pillow` in your command prompt or terminal.
2. Create a folder named `input` in the same directory as the script.
3. Add the images you want to convert to the `input` folder.
4. Run the script using `python script_name.py`.
5. The converted images will be saved in a folder named `output`.

Note: The script only supports `.png`, `.jpg`, and `.jpeg` file extensions. Other file types will not be processed.

## Code Explanation

The `convert_to_webp()` function takes two parameters: `src_folder` and `dest_folder`. The function first checks if the `dest_folder` exists and creates it if it does not.

The function then loops through all files in the `src_folder`. It checks the file extension and only processes files with `.png`, `.jpg`, or `.jpeg` extensions. The function uses the PIL module to open the image and save it in the WebP format in the `dest_folder`.

The `if __name__ == '__main__':` block checks if the `src_folder` exists. If it does not, the script exits with an error message. If the folder exists, the `convert_to_webp()` function is called, and a success message is printed.

Happy converting!
