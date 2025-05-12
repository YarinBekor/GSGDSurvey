from PIL import Image, ImageSequence

input_path = "Variants/DG4D/1/step_22.5.gif"
output_path = "Variants/DG4D/1/step_22.5.gif"

with Image.open(input_path) as im:
    frames = [frame.copy() for frame in ImageSequence.Iterator(im)]
    im.save(
        output_path,
        save_all=True,
        append_images=frames[1:],
        loop=0
    )