#!/usr/bin/env python3
# coding: utf-8

# Code to rebuild the cut-out patches from the original files
# to be able to interpret their position in the original images.

# Path to the patches
# Format: 
# <IMAGE NAME>_<INDEX LABELME SELECTION>_<TISSUE TYPE>_l_<X POS IN IMAGE>_w_<Y POS IN IMAGE>.jpg 
# example: 992_22_ca_202203081937_2_Normal_l_12280_w_6255.jpg
# where <IMAGE NAME> = 992_22_ca_202203081937, <INDEX LABELME SELECTION> = 2 (second box in labelme json), 
# <TISSUE TYPE> = Normal, <X POS IN IMAGE> = 12280 (starting X or vertical pixel of path in original full size file),
# <Y POS IN IMAGE> = 6255 (starting Y or horizontal pixel of path in original full size file)
#

import os
import re
import numpy as np
from PIL import Image

# Path to patch files of an image extracted from a labelme json file on the original tiff data
path = "./992_22_ca_202203081937_labelme/"
#path = "./GWIN2000713_982_rebuild/GWIN2000713_982_labelme/"

# Patch size (sizexsize patches)
patch_size = 300

def extract_l_w_values_from_directory(path):
    """
    Extract L and W values from all files in a specified directory.
    
    Parameters:
    path (str): Path to the directory containing files
    
    Returns:
    tuple: Two numpy arrays containing L and W values
    """
    # Regular expression to match L and W values in the filename
    pattern = r'l_(\d+)_w_(\d+)'
    
    # Lists to store extracted values
    l_values = []
    w_values = []
    
    # Get all files in the directory
    try:
        # List all files in the directory
        filenames = os.listdir(path)
        
        # Iterate through filenames and extract values
        for filename in filenames:
            # Full path to the file
            full_path = os.path.join(path, filename)
            
            # Only process if it's a file (not a subdirectory)
            if os.path.isfile(full_path):
                match = re.search(pattern, filename)
                if match:
                    l_values.append(int(match.group(1)))
                    w_values.append(int(match.group(2)))
        
        return np.array(l_values), np.array(w_values), filenames
    
    except FileNotFoundError:
        print(f"Directory not found: {path}")
        return np.array([]), np.array([])
    except PermissionError:
        print(f"Permission denied when accessing directory: {path}")
        return np.array([]), np.array([])

array_l, array_w, filenames = extract_l_w_values_from_directory(path)

merged_array = np.stack([array_l, array_w]).T

#print("L values:", array_l)
#print("W values:", array_w)
print("Total files processed:", len(array_l))

# Create empty array to fit patches
x_min = array_l.min()
y_min = array_w.min()
x_max = array_l.max() + patch_size # x end size
y_max = array_w.max() + patch_size # y end size

# Note: does not have to be exactly by patch_size as points are selected by hand
# and can even overlap!
blank = np.zeros((x_max-x_min, y_max-y_min, 3))

# Read each patch (file) and fit in in the blank array
# TODO - check that the file name corresponds with l and w values

for ind, x_y_tuple in enumerate(merged_array):
    #print(x_y_tuple, ind)
    file_path = os.path.join(path, filenames[ind])
    image = np.asarray(Image.open(file_path))
    #print(image.shape, x_y_tuple[0], x_y_tuple[1])
    # Positions relative to the blank array
    blank[x_y_tuple[0]-x_min:x_y_tuple[0]-x_min+patch_size, x_y_tuple[1]-y_min:x_y_tuple[1]-y_min+patch_size, :] = image

# Convert to int to show
rebuild_ima = blank.astype(int)

# The original can be read
#image992 = np.asarray(Image.open("../992_22_ca_202203081937_pred_grid_web.jpg"))
# To rescale
#im992 = image992.astype(np.uint8)
# original_height, original_width, channels = im992.shape
#new_height = original_height * 4
#new_width = original_width * 4
# Opencv uses traditional x and y dimensions (not like python arrays!)
#new_dimensions = (new_width, new_height)
#nim992 = cv2.resize(im992, new_dimensions, interpolation=cv2.INTER_AREA)