from PIL import Image, ImageSequence
import glob
import os
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def process_gif(input_path, output_path):
    try:
        with Image.open(input_path) as im:
            frames = [frame.copy() for frame in ImageSequence.Iterator(im)]
            im.save(
                output_path,
                save_all=True,
                append_images=frames[1:],
                loop=0
            )
        logger.info(f"Successfully processed: {input_path}")
    except Exception as e:
        logger.error(f"Error processing {input_path}: {str(e)}")

def find_dg4d_dirs(root_dir):
    dg4d_dirs = []
    for root, dirs, files in os.walk(root_dir):
        if "DG4D" in dirs:
            dg4d_path = os.path.join(root, "DG4D")
            dg4d_dirs.append(dg4d_path)
    return dg4d_dirs

# # Main execution
# root_dir = "COMP"
# dg4d_dirs = find_dg4d_dirs(root_dir)

# if not dg4d_dirs:
#     logger.warning(f"No DG4D directories found under {root_dir}")
# else:
#     logger.info(f"Found {len(dg4d_dirs)} DG4D directories")
#     for dg4d_dir in dg4d_dirs:
#         logger.info(f"Processing directory: {dg4d_dir}")
#         gif_pattern = os.path.join(dg4d_dir, "**", "*.gif")
#         gif_files = glob.glob(gif_pattern, recursive=True)
        
#         if not gif_files:
#             logger.info(f"No GIF files found in {dg4d_dir}")
#         else:
#             logger.info(f"Found {len(gif_files)} GIF files in {dg4d_dir}")
#             for gif_file in gif_files:
#                 process_gif(gif_file, gif_file)

gifs_to_process = ["COMP/Variants/Brian_Running/castle/DG4D/step_22.5.gif", "COMP/Variants/Brian_Running/castle/DG4D/step_247.5.gif"]

for g in gifs_to_process:
    process_gif(g, g)