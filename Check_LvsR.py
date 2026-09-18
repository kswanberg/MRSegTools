# THIS SCRIPT TURNS ALL LABELS DESIGNATED FOR THE L HEMISPHERE TO BLACK (0,0,0)
# THIS SCRIPT TURNS ALL LABELS DESIGNATED FOR THE R HEMISPHERE TO GRAY (125,125,125)
# THIS WILL AFFECT ALL COLOURS (EXCEPT LABELS 2, 10, 17)
# made by Dean Dizon 2026

import os
import numpy as np
from PIL import Image

# Folder with your current coloured PNGs
input_dir = os.path.expanduser("~/REPLACE_WITH_YOUR_INPUT_FOLDER")

# New folder where fixed PNGs will be saved
output_dir = os.path.expanduser("~/REPLACE_WITH_YOUR_INPUT_FOLDER")
os.makedirs(output_dir, exist_ok=True)

# Fill this in:
# (wrong_R, wrong_G, wrong_B): (correct_R, correct_G, correct_B)
COLOR_REMAP = {
	# (incorrect/old): (proper/new)    # number: name
    (194, 199, 255): (0, 0, 0),      # 1: L Hippocampus (Light Blue)
    (255, 149, 120): (125, 125, 125),      # 21: R Hippocampus (Tan)
    (0, 0, 255): (0, 0, 255),      # 2: L/R External Capsule (Blue)
    (128, 0, 128): (0, 0, 0),      # 3: L Caudate Putamen (Grape Purple)
    (102, 255, 255): (125, 125, 125),      # 23: R Caudate Putamen (Cyan)
    (252, 111, 207): (0, 0, 0),      # 4: L Anterior Commissure (Pink)
    (255, 255, 10): (125, 125, 125),      # 24: R Anterior Commissure (Yellow)
    (146, 156, 54): (0, 0, 0),      # 5: L Globus Pallidus (Yellow-Olive)
    (95, 172, 162): (125, 125, 125),      # 25: R Globus Pallidus (Philly Eagle Green)
    (255, 126, 0): (0, 0, 0),      # 6: L Internal Capsule (Orange)
    (191, 52, 128): (125, 125, 125),      # 26: R Internal Capsule (Purple)
    (9, 0, 130): (0, 0, 0),      # 7: L Thalamus (Navy Blue)
    (160, 86, 255): (125, 125, 125),      # 27: R Thalamus (Bright Purple)
    (153, 102, 51): (0, 0, 0),      # 8: L Cerebellum (Brown)
    (218, 121, 253): (125, 125, 125),      # 28: R Cerebellum (Pink)
    (222, 205, 4): (0, 0, 0),      # 9: L Superior Colliculi (Yellow)
    (255, 52, 0): (125, 125, 125),      # 29: R Superior Colliculi (Orange)
    (254, 204, 102): (254, 204, 102),      # 10 L/R Ventricles (Beige)
    (252, 174, 230): (0, 0, 0),      # 11: L Hypothalamus (Light Blue)
    (104, 244, 203): (125, 125, 125),      # 31: R Hypothalamus (Pink)
    (214, 0, 87): (0, 0, 0),      # 12: L Inferior Colliculi (Hot Pink)
    (199, 11, 203): (125, 125, 125),      # 32: R Inferior Colliculi (Magenta)
    (136, 129, 128): (0, 0, 0),      # 13: L Central Gray (Gray)
    (10, 3, 10): (125, 125, 125),      # 33: R Central Gray (Black)
    (15, 49, 1): (0, 0, 0),      # 14: L Neocortex (Dark Green)
    (54, 255, 153): (125, 125, 125),      # 34: R Neocortex (Light Green)
    (65, 34, 8): (0, 0, 0),      # 15: L Amygdala (Brown)
    (253, 236, 169): (125, 125, 125),      # 35: R Amygdala (Beige)
    (33, 255, 6): (0, 0, 0),      # 16: L Olfactory Bulb (Neon Green)
    (128, 0, 255): (125, 125, 125),      # 36: R Olfactory Bulb (Purple)
    (88, 160, 3): (88, 160, 3),      # 17: L/R Brainstem (Green)
    (216, 142, 71): (0, 0, 0),      # 18: L Midbrain (Brown)
    (0, 115, 255): (125, 125, 125),      # 38: R Midbrain (Blue)
    (0, 129, 20): (0, 0, 0),      # 19: L Septal Region (Green)
    (251, 2, 7): (125, 125, 125),      # 39: R Septal Region (Red-Orange)
    (255, 19, 94): (0, 0, 0),      # 20: L Fimbria (Hot-Pink)
    (255, 0, 255): (125, 125, 125),      # 40: R Fimbria (Pink) 
   
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
