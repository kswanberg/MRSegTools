# THIS SCRIPT IS PART 1/2 THAT FLIPS THE COLOURS ACROSS THE MIDLINE
# THIS WILL TURN ALL COLOURS TO GRAY (EXCEPT LABELS 2, 10, 17)
#
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
    (194, 199, 255): (21, 21, 21),      # 1: L Hippocampus (Light Blue)
    (255, 149, 120): (1, 1, 1),      # 21: R Hippocampus (Tan)
    (0, 0, 255): (0, 0, 255),      # 2: L/R External Capsule (Blue)
    (128, 0, 128): (23, 23, 23),      # 3: L Caudate Putamen (Grape Purple)
    (101, 255, 255): (3, 3, 3),      # 23: R Caudate Putamen (Cyan)
    (252, 111, 207): (24, 24, 24),      # 4: L Anterior Commissure (Pink)
    (255, 255, 10): (4, 4, 4),      # 24: R Anterior Commissure (Yellow)
    (146, 156, 54): (25, 25, 25),      # 5: L Globus Pallidus (Yellow-Olive)
    (95, 172, 162): (5, 5, 5),      # 25: R Globus Pallidus (Philly Eagle Green)
    (255, 126, 0): (26, 26, 26),      # 6: L Internal Capsule (Orange)
    (191, 52, 128): (6, 6, 6),      # 26: R Internal Capsule (Purple)
    (9, 0, 130): (27, 27, 27),      # 7: L Thalamus (Navy Blue)
    (160, 86, 255): (7, 7, 7),      # 27: R Thalamus (Bright Purple)
    (153, 102, 51): (28, 28, 28),      # 8: L Cerebellum (Brown)
    (218, 121, 253): (8, 8, 8),      # 28: R Cerebellum (Pink)
    (222, 205, 4): (29, 29, 29),      # 9: L Superior Colliculi (Yellow)
    (255, 52, 0): (9, 9, 9),      # 29: R Superior Colliculi (Orange)
    (254, 204, 102): (254, 204, 102),      # 10 L/R Ventricles (Beige)
    (252, 174, 230): (31, 31, 31),      # 11: L Hypothalamus (Light Blue)
    (104, 244, 203): (11, 11, 11),      # 31: R Hypothalamus (Pink)
    (214, 0, 87): (32, 32, 32),      # 12: L Inferior Colliculi (Hot Pink)
    (199, 11, 203): (12, 12, 12),      # 32: R Inferior Colliculi (Magenta)
    (136, 129, 128): (33, 33, 33),      # 13: L Central Gray (Gray)
    (10, 3, 10): (13, 13, 13),      # 33: R Central Gray (Black)
    (15, 49, 1): (34, 34, 34),      # 14: L Neocortex (Dark Green)
    (54, 255, 153): (14, 14, 14),      # 34: R Neocortex (Light Green)
    (65, 34, 8): (35, 35, 35),      # 15: L Amygdala (Brown)
    (253, 236, 169): (15, 15, 15),      # 35: R Amygdala (Beige)
    (33, 255, 6): (36, 36, 36),      # 16: L Olfactory Bulb (Neon Green)
    (128, 0, 255): (16, 16, 16),      # 36: R Olfactory Bulb (Purple)
    (88, 160, 3): (88, 160, 3),      # 17: L/R Brainstem (Green)
    (216, 142, 71): (38, 38, 38),      # 18: L Midbrain (Brown)
    (0, 115, 255): (18, 18, 18),      # 38: R Midbrain (Blue)
    (0, 129, 20): (39, 39, 39),      # 19: L Septal Region (Green)
    (251, 2, 7): (19, 19, 19),      # 39: R Septal Region (Red-Orange)
    (255, 19, 94): (40, 40, 40),      # 20: L Fimbria (Hot-Pink)
    (255, 0, 255): (20, 20, 20),      # 40: R Fimbria (Pink) 
   
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
