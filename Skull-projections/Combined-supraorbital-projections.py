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
file_names = ['41 Supraorb python', '70 Supraorb python', '74 Supraorb python',
              '80 Supraorb python', '103 Supraorb python', '122 Supraorb python',
              '197 Supraorb python']

for file_name in file_names:
	# Constructing the relative file path
	rel_path = f"Original Datasets/{file_name}.xlsx"
	# Merging both and this way our script is "location" independent
	abs_file_path = os.path.join(script_dir, rel_path)

	# Reading Excel file
	old_coordinates_df = pd.read_excel(abs_file_path)

	# Temporarily saving the colours as they will be removed later
	temporary_save_for_color_df = old_coordinates_df['color_l']

	del old_coordinates_df['color_l']
	del old_coordinates_df['color_r']
	del old_coordinates_df['label_r']


	# Extracting the reference points for both sides, left and right
	old_reference_points = old_coordinates_df[0:3]

	# Tuning the reference points by adding some offset, in this case to the Nose Point
	x_tune_left_side  = 0; y_tune_left_side  = 0; z_tune_left_side  = 0
	x_tune_right_side = 0; y_tune_right_side = 0; z_tune_right_side = 0
	if   file_name == '41 Supraorb python':
		x_tune_left_side = 0    #
		y_tune_left_side = 5    #
		z_tune_left_side = 5    #
		x_tune_right_side = -10 #
		y_tune_right_side = -10 #
		z_tune_right_side = -14 #

	elif file_name == '70 Supraorb python':
		x_tune_left_side = 5
		y_tune_left_side = 7  # needs further tuning (nerve start is in skull)
		z_tune_left_side = 5
		x_tune_right_side = 14
		y_tune_right_side = 14 # needs further tuning (nerve start is in skull)
		z_tune_right_side = 14

	elif file_name ==  '74 Supraorb python':
		x_tune_left_side = 3
		y_tune_left_side = 3  # needs further tuning (nerve start is in skull)
		z_tune_left_side = 3
		x_tune_right_side = 0 #
		y_tune_right_side = 0 #
		z_tune_right_side = 0 #

	elif file_name == '80 Supraorb python':
		x_tune_left_side = -13
		y_tune_left_side = -13  # needs further tuning (nerve start is in skull)
		z_tune_left_side = -13
		x_tune_right_side = -12
		y_tune_right_side = -12 # needs further tuning (nerve start is in skull)
		z_tune_right_side = -12

	elif file_name == '103 Supraorb python':
		x_tune_left_side = 1#2
		y_tune_left_side = 1#2  # needs further tuning (nerve start is in skull)
		z_tune_left_side = 1#2
		x_tune_right_side = 0
		y_tune_right_side = 0 # needs further tuning (nerve start is in skull)
		z_tune_right_side = 0

	elif file_name == '122 Supraorb python':
		x_tune_left_side = 12
		y_tune_left_side = 12 # needs further tuning (nerve start is in skull, red is floating)
		z_tune_left_side = 12
		x_tune_right_side = 15
		y_tune_right_side = 15 # needs further tuning (nerve start is in skull)
		z_tune_right_side = 15

	elif file_name == '197 Supraorb python':
		x_tune_left_side = 12
		y_tune_left_side = 12 # needs further tuning (nerve start is in skull, red is floating)
		z_tune_left_side = 12
		x_tune_right_side = 5
		y_tune_right_side = 0
		z_tune_right_side = 0 # needs further tuning (nerve start is too high)



	####### Left Side #######

	# Extracting the Left side's reference points
	right_eye = [old_reference_points.loc[0, 'x1_l'], old_reference_points.loc[0, 'y1_l'], old_reference_points.loc[0, 'z1_l']]
	left_eye  = [old_reference_points.loc[1, 'x1_l'], old_reference_points.loc[1, 'y1_l'], old_reference_points.loc[1, 'z1_l']]
	nose      = [old_reference_points.loc[2, 'x1_l'] + x_tune_left_side , old_reference_points.loc[2, 'y1_l']+ y_tune_left_side,
	             old_reference_points.loc[2, 'z1_l'] + z_tune_left_side]

	# Calculating the least square transform (check the helper function for further details)
	# The numerical coordinates were obtained from 3D Slicer
	T, _, _ = least_square_transform([         left_eye,   				right_eye, 					    nose            ],
	                                 [[-54.901, 84.476, -19.076], [58.355 , 85.368, -17.154], [1.123, 114.725, -23.732]])

	# Extracting the left side and dropping the unneeded columns of the right side
	old_points_left_side = old_coordinates_df.loc[0:20]

	del old_points_left_side['label_l']
	del old_points_left_side['x1_r']
	del old_points_left_side['y1_r']
	del old_points_left_side['z1_r']


	old_points_array = np.array(old_points_left_side)

	# Applying the transform
	homogeneous_points = np.concatenate([old_points_array, np.ones((old_points_left_side.shape[0], 1))], axis=1)
	transformed_points = np.dot(homogeneous_points, np.transpose(T))

	# Getting the new coordinates
	new_points = transformed_points[:, :3]

	# Saving the new coordinates in a df
	new_points_df_left_side = pd.DataFrame(new_points, columns=old_points_left_side.columns)

	# Adding colours again
	new_points_df_left_side['color'] = temporary_save_for_color_df

	# Switching the order of the first 2 columns so the nose is in the middle (for representation later)
	row1 = new_points_df_left_side.iloc[1].copy()
	row2 = new_points_df_left_side.iloc[2].copy()

	new_points_df_left_side.iloc[1] = row2
	new_points_df_left_side.iloc[2] = row1

	# Dropping last 2 vlueless rows
	new_points_df_left_side.drop(new_points_df_left_side.tail(2).index, inplace=True)


	####### Right Side #######

	# Extracting the Right side's reference points
	right_eye = [old_reference_points.loc[0, 'x1_r'], old_reference_points.loc[0, 'y1_r'], old_reference_points.loc[0, 'z1_r']]
	left_eye  = [old_reference_points.loc[1, 'x1_r'], old_reference_points.loc[1, 'y1_r'], old_reference_points.loc[1, 'z1_r']]
	nose      = [old_reference_points.loc[2, 'x1_r'] + x_tune_right_side, old_reference_points.loc[2, 'y1_r']+ y_tune_right_side,
	             old_reference_points.loc[2, 'z1_r'] + z_tune_right_side]

	# Calculating the least square transform (check the helper function for further details)
	T ,R ,t = least_square_transform([        left_eye,                     right_eye,                  nose           ],
	                                 [[-54.901, 84.476, -19.076], [58.355 , 85.368, -17.154], [1.123, 114.725, -23.732]])

	# Extracting the right side and dropping the unneeded columns of the left side
	old_points_right_side = old_coordinates_df.loc[0:20]

	del old_points_right_side['label_l']
	del old_points_right_side['x1_l']
	del old_points_right_side['y1_l']
	del old_points_right_side['z1_l']


	old_points_array = np.array(old_points_right_side)

	# Applying the transform
	homogeneous_points = np.concatenate([old_points_array, np.ones((old_points_right_side.shape[0], 1))], axis=1)
	transformed_points = np.dot(homogeneous_points, np.transpose(T))

	# Getting the new coordinates
	new_points = transformed_points[:, :3]

	# Saving the new coordinates in a df
	new_points_df_right_side = pd.DataFrame(new_points, columns=old_points_right_side.columns)

	# Switching the order of the first 2 columns so the nose is in the middle of the 2 eyes
	row1 = new_points_df_right_side.iloc[1].copy()
	row2 = new_points_df_right_side.iloc[2].copy()

	new_points_df_right_side.iloc[1] = row2
	new_points_df_right_side.iloc[2] = row1

	# Dropping last 2 vlueless rows
	new_points_df_right_side.drop(new_points_df_right_side.tail(2).index, inplace=True)


	###### Merge Both Sides ######

	# Constructing the absolute file path
	file_name_without_extension = file_name.split(".xlsx")[0]
	rel_path = f"Modified Datasets\\new_{file_name_without_extension}.csv"
	abs_file_path = os.path.join(script_dir, rel_path)

	new_points_df = pd.concat([new_points_df_right_side, new_points_df_left_side], axis=1)

	# Saving to a .cvs file for visualisation in Paraview if needed
	new_points_df.to_csv(abs_file_path, index=False)


################# Visualisation #################



# Loading mesh data from .STL file
src = mlab.pipeline.open("Skull-projections/Reference_Skull_103.stl")
mesh = mlab.pipeline.surface(src)

# Defining the color mapping dictionary
color_mapping = {
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
		if color != 1:
			if color not in points_right_side:
				points_right_side[color] = []
			points_right_side[color].append(line[:3])

	points_left_side = {}
	for line in lines_left_side:
		color = line[3]
		if color != 1:
			if color not in points_left_side :
				points_left_side[color] = []
			points_left_side[color].append(line[:3])

	# Drawing lines between points with the same color value
	for color, pts in points_right_side.items():
		pts = np.array(pts)
		if len(pts) > 1:
			line_color = color_mapping.get(color)
			mlab.plot3d(pts[:, 0], pts[:, 1], pts[:, 2], color=line_color, tube_radius=1, opacity=0.2)

	for color, pts in points_left_side.items():
		pts = np.array(pts)
		if len(pts) > 1:
			line_color = color_mapping.get(color)
			mlab.plot3d(pts[:, 0], pts[:, 1], pts[:, 2], color=line_color, tube_radius=1, opacity=0.2)

# Adding a custom legend using text annotations
mlab.text(-80, 0, 'Mediaal', z=40, width=0.2, color=(0.0, 1.0, 0.0))  # Green
mlab.text(-80, 0, 'Intermediaal', z=60, width=0.2, color=(0.0, 0.0, 1.0))  # Blue
mlab.text(-80, 0, 'Lateraal', z=80, width=0.2, color=(1.0, 0.0, 0.0))  # Red

# Setting the desired orientation when the file is opened
mlab.view(azimuth=90, elevation=90, distance=450)

# Showing the plot
mlab.show()