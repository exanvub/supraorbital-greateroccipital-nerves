# Imports
import pandas as pd
import numpy as np
from helper_functions import *
from mayavi import mlab
import os
import csv

# Getting the absolute path of the directory of our script
script_dir = os.path.dirname(os.path.abspath(__file__))

# List of file names to process
file_names = [
	        #'41 Supraorb', 
            #'41 occip',

	        #'70 Supraorb',
            #'70 occip',

	        #'74 Supraorb',
            #'74 occip',


            #'80 Supraorb',
            #'80 occip'

	        #'103 Supraorb',
            #'103 occip',

	        #'122 Supraorb',
            #'122 occip'

			#'158 Supraorb',
			#'158 occip',
			
            #'197 Supraorb',
            #'197 occip',
	    
			'183 Supraorb_mean',
			'183 occip_mean'

			#'183 Supraorb',
			#'183 occip_ORIG(2)'

			# '157 Supraorb',
			# '157 occip'
	    ]
#
# Select the mesh to be used
#src = mlab.pipeline.open("3D-models/model-41/Segmentation_41.stl")
#src = mlab.pipeline.open("3D-models/model-70/Segmentation_70.stl")
#src = mlab.pipeline.open("3D-models/model-74/Segmentation_74.stl")
#src = mlab.pipeline.open("3D-models/model-80/Segmentation_80.stl")
#src = mlab.pipeline.open("3D-models/model-103/Segmentation_103.stl")
#src = mlab.pipeline.open("3D-models/model-122/Segmentation_122.stl")
#src = mlab.pipeline.open("3D-models/model-158/Segmentation_158.stl")
#src = mlab.pipeline.open("3D-models/model-197/Segmentation_197.stl")
src = mlab.pipeline.open("3D-models/model-183/Segmentation_183.stl")
# src = mlab.pipeline.open("3D-models/model-157/Segmentation_157.stl")

# Loading mesh data from .STL file

mesh = mlab.pipeline.surface(src)

# Defining the color mapping dictionary
color_mapping = {
    1: (0.0, 0.0, 0.0),  # Black for reference
    2: (0.0, 1.0, 1.0),  # Cyan for occipital
    3: (1.0, 1.0, 0.0),  # Yellow for medial
    4: (1.0, 0.0, 1.0),  # Magenta for lateral
	5: (0.0, 1.0, 0.0),  # Green for Mediaal
	6: (0.0, 0.0, 1.0),  # Blue for Intermediaal
	7: (1.0, 0.0, 0.0),  # Red for Lateraal
}


for file_name in file_names:
	# Constructing the absolute file path
	rel_path = f"Modified Datasets/new_{file_name}.csv"
	abs_file_path = os.path.join(script_dir, rel_path)

	# Splitting the data of the .csv file into right and left
	lines_right_side = []
	lines_left_side = []

	with open(abs_file_path, 'r') as f:
		reader = csv.DictReader(f)
		for row in reader:
			lines_right_side.append([float(row['x1_r']), float(row['y1_r']), float(row['z1_r']), int(row['color'])])
			lines_left_side.append([float(row['x1_l']), float(row['y1_l']), float(row['z1_l']), int(row['color'])])


	# Grouping points with the same color value in a dictionary
	points_right_side = {}
	for line in lines_right_side:
		color = line[3]
		if color > 0:
			if color not in points_right_side:
				points_right_side[color] = []
			points_right_side[color].append(line[:3])

	points_left_side = {}
	for line in lines_left_side:
		color = line[3]
		if color > 0:
			if color not in points_left_side :
				points_left_side[color] = []
			points_left_side[color].append(line[:3])

	# Drawing lines between points with the same color value
	for color, pts in points_right_side.items():
		pts = np.array(pts)
		if len(pts) > 1:
			line_color = color_mapping.get(color)
			mlab.plot3d(pts[:, 0], pts[:, 1], pts[:, 2], color=line_color, tube_radius=1.5, opacity=0.6)

	for color, pts in points_left_side.items():
		pts = np.array(pts)
		if len(pts) > 1:
			line_color = color_mapping.get(color)
			mlab.plot3d(pts[:, 0], pts[:, 1], pts[:, 2], color=line_color, tube_radius=1.5, opacity=0.6)

## Adding a custom legend using text annotations
#mlab.text(-80, 0, 'Mediaal', z=40, width=0.2, color=(0.0, 1.0, 0.0))  # Green
#mlab.text(-80, 0, 'Intermediaal', z=60, width=0.2, color=(0.0, 0.0, 1.0))  # Blue
#mlab.text(-80, 0, 'Lateraal', z=80, width=0.2, color=(1.0, 0.0, 0.0))  # Red

# Setting the desired orientation when the file is opened
mlab.view(azimuth=0, elevation=90, distance=450)

# Showing the plot
mlab.show()