from PIL import Image
import os

def extract_gif_frames(gif_path, output_dir=None):
    gif = Image.open(gif_path)
    base_filename = os.path.splitext(os.path.basename(gif_path))[0]

    if output_dir is None:
        output_dir = base_filename
    os.makedirs(output_dir, exist_ok=True)  

    try:
        i = 0
        while True:
            gif.seek(i)
            frame = gif.convert('RGBA')
            frame.save(os.path.join(output_dir, f'{base_filename}_{i}.png'), format='PNG')
            i += 1
    except EOFError:
        pass

if __name__ == "__main__":
    for file in os.listdir("gifs"):
        extract_gif_frames(f"gifs/{file}", file[:-4])
