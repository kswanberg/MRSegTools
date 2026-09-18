# THIS SCRIPT TURNS THE SEGMENTATION GRAY (WILL NOT FLIP)
# THIS REMAP SCRIPT ASSUMES THAT EVERYTHING WAS SEGMENTED PROPERLY ACROSS MIDLINE
# THIS WILL TURN ALL COLOURS TO GRAY (EXCEPT LABELS 2, 10, 17)
# USE THIS IN ORDER TO VERIFY IF COLOURS EXPORTED PROPERLY
# made by Dean Dizon 2026
import os
import numpy as np
from PIL import Image

# Folder with your current coloured PNGs
input_dir = os.path.expanduser("~/REPLACE_WITH_YOUR_INPUT_FOLDER")

# New folder where fixed PNGs will be saved
output_dir = os.path.expanduser("~/REPLACE_WITH_YOUR_OUTPUT_FOLDER")
os.makedirs(output_dir, exist_ok=True)

# Fill this in:
# (wrong_R, wrong_G, wrong_B): (correct_R, correct_G, correct_B)
COLOR_REMAP = {
	# (incorrect/old): (proper/new)    # number: name
    (194, 199, 255): (1, 1, 1),      # 1: L Hippocampus (Light Blue)
    (255, 149, 120): (21, 21, 21),      # 21: R Hippocampus (Tan)
    (0, 0, 255): (0, 0, 255),      # 2: L/R External Capsule (Blue)
    (128, 0, 128): (3, 3, 3),      # 3: L Caudate Putamen (Grape Purple)
    (101, 255, 255): (23, 23, 23),      # 23: R Caudate Putamen (Cyan)
    (252, 111, 207): (4, 4, 4),      # 4: L Anterior Commissure (Pink)
    (255, 255, 10): (24, 24, 24),      # 24: R Anterior Commissure (Yellow)
    (146, 156, 54): (5, 5, 5),      # 5: L Globus Pallidus (Yellow-Olive)
    (95, 172, 162): (25, 25, 25),      # 25: R Globus Pallidus (Philly Eagle Green)
    (255, 126, 0): (6, 6, 6),      # 6: L Internal Capsule (Orange)
    (191, 52, 128): (26, 26, 26),      # 26: R Internal Capsule (Purple)
    (9, 0, 130): (7, 7, 7),      # 7: L Thalamus (Navy Blue)
    (160, 86, 255): (27, 27, 27),      # 27: R Thalamus (Bright Purple)
    (153, 102, 51): (8, 8, 8),      # 8: L Cerebellum (Brown)
    (218, 121, 253): (28, 28, 28),      # 28: R Cerebellum (Pink)
    (222, 205, 4): (9, 9, 9),      # 9: L Superior Colliculi (Yellow)
    (255, 52, 0): (29, 29, 29),      # 29: R Superior Colliculi (Orange)
    (254, 204, 102): (254, 204, 102),      # 10 L/R Ventricles (Beige)
    (252, 174, 230): (11, 11, 11),      # 11: L Hypothalamus (Pink)
    (104, 244, 203): (31, 31, 31),      # 31: R Hypothalamus (Light Blue)
    (214, 0, 87): (12, 12, 12),      # 12: L Inferior Colliculi (Hot Pink)
    (199, 11, 203): (32, 32, 32),      # 32: R Inferior Colliculi (Magenta)
    (136, 129, 128): (13, 13, 13),      # 13: L Central Gray (Gray)
    (10, 3, 10): (33, 33, 33),      # 33: R Central Gray (Black)
    (15, 49, 1): (14, 14, 14),      # 14: L Neocortex (Dark Green)
    (54, 255, 153): (34, 34, 34),      # 34: R Neocortex (Light Green)
    (65, 34, 8): (15, 15, 15),      # 15: L Amygdala (Brown)
    (253, 236, 169): (35, 35, 35),      # 35: R Amygdala (Beige)
    (33, 255, 6): (16, 16, 16),      # 16: L Olfactory Bulb (Neon Green)
    (128, 0, 255): (36, 36, 36),      # 36: R Olfactory Bulb (Purple)
    (88, 160, 3): (88, 160, 3),      # 17: L/R Brainstem (Green)
    (216, 142, 71): (18, 18, 18),      # 18: L Midbrain (Brown)
    (0, 115, 255): (38, 38, 38),      # 38: R Midbrain (Blue)
    (0, 129, 20): (19, 19, 19),      # 19: L Septal Region (Green)
    (251, 2, 7): (39, 39, 39),      # 39: R Septal Region (Red-Orange)
    (255, 19, 94): (20, 20, 20),      # 20: L Fimbria (Hot Pink)
    (255, 0, 255): (40, 40, 40),      # 40: R Fimbria (Pink) 
   
}

for filename in sorted(os.listdir(input_dir)):
    if not filename.lower().endswith(".png"):
        continue

    img_path = os.path.join(input_dir, filename)
    img = Image.open(img_path).convert("RGB")
    arr = np.array(img)

    for wrong_color, correct_color in COLOR_REMAP.items():
        mask = np.all(arr == wrong_color, axis=-1)
        arr[mask] = correct_color

    output_path = os.path.join(output_dir, filename)
    Image.fromarray(arr, mode="RGB").save(output_path)

print("Done. Fixed PNGs saved to:")
print(output_dir)
