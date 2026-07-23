##################################################
## Count voxels in a nifti label mask
##################################################
## BSD 2-clause license 
##################################################
## Author: Kelley Swanberg  
## Copyright: Copyright 2026
## Version: v2026
## Maintainer: Kelley Swanberg
## Email: kelley.swanberg@med.lu.se
## Status: Development
##################################################

import numpy as np
import matplotlib.pyplot as plt
import os
import datetime 
import csv
import nibabel as nib 
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Select the file in which to count the voxels 
Tk().withdraw(); 
nifti_to_calculate = askopenfilename(); 
print(nifti_to_calculate); 
img = nib.load(nifti_to_calculate); 

# Find number of unique labels in image 
unique_labels = np.unique(img.get_fdata()); 

# Loop through unique labels and count number of voxels for each
voxel_counts = np.zeros((len(unique_labels), 2));

# For each label count the number of associated voxels 
for ii, label in enumerate(unique_labels):
    voxel_count = np.sum(img.get_fdata() == label);
    voxel_counts[ii, 0] = label;
    voxel_counts[ii, 1] = voxel_count;

# Print the label counts as a CSV for that unique file
csvfilename = os.path.splitext(nifti_to_calculate)[0]
csvfilename  = csvfilename .replace('.', '')
timeidentifier = str(datetime.datetime.now()).replace(' ', '_'); 
timeidentifier = timeidentifier.replace(':', ''); 
timeidentifier = timeidentifier.replace('.', ''); 

with open(csvfilename + timeidentifier + '_voxel_counts.csv', 'w', newline='') as f:
    writer = csv.writer(f);
    writer.writerow(['Label', 'Voxel Count']);
    writer.writerows(voxel_counts);
