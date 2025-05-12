from PIL import Image
import sys

def make_gif_loop_infinite(input_path, output_path):
    with Image.open(input_path) as img:
        frames = []
        try:
            while True:
                frames.append(img.copy())
                img.seek(len(frames))  # Go to next frame
        except EOFError:
            pass  # End of frames

        frames[0].save(
            output_path,
            save_all=True,
            append_images=frames[1:],
            loop=0,
            duration=img.info.get('duration', 100),
            disposal=2
        )
        print(f"Saved infinite-looping GIF to: {output_path}")

# Usage example
if __name__ == "__main__":
    make_gif_loop_infinite("Variants/DG4D/1/step_22.5.gif", "Variants/DG4D/1/step_22.5.gif")
