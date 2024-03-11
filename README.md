## GIF Frame Extractor

**Description**

This Python script is designed to extract individual frames from GIF files and save them as separate PNG images. It's ideal for scenarios where you want to analyze, modify, or use specific frames of an animated GIF.

**Features**

-   Extracts all frames from GIF files.
-   Saves frames as high-quality PNG images.
-   Automatically creates organized output folders (one folder per GIF).

**Prerequisites**

-   Python 3 ([https://www.python.org/](https://www.python.org/))
-   Pillow (PIL) library: Install using `pip install Pillow`

**Usage**

1. **Place your GIF files in a folder named "gifs" within the same directory as the script.**
2. **Run the script from the command line:**
    ```bash
    python extract_frames.py
    ```

**Explanation**

The script works as follows:

1. **Imports Necessary Libraries:** `PIL` (Pillow) is used for image manipulation, and `os` is used for file and directory operations.

2. **`extract_gif_frames` Function:**

    - Opens the input GIF.
    - Gets the base file name of the GIF.
    - Creates an output directory named after the GIF (if it doesn't exist).
    - Iterates through each frame of the GIF:
        - Seeks to the current frame.
        - Converts the frame to RGBA format (for transparency support).
        - Saves the frame as a PNG file with an auto-incrementing index.

3. **Main Execution (`if __name__ == "__main__":`)**
    - Finds all files in the "gifs" folder.
    - For each GIF file, calls the `extract_gif_frames` function to process it, using the GIF's filename (without extension) as the output directory name.

**Example**

If you have a GIF named "animation.gif" in the "gifs" folder, running the script will:

-   Create a folder named "animation".
-   Extract frames and save them as "animation_0.png", "animation_1.png", etc., inside the "animation" folder.
