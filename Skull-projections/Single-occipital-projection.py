# Imports
import pandas as pd
import numpy as np
from helper_functions import *
from mayavi import mlab
import os
import csv


# Getting the absolute path of the directory of our script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Select the mesh to be used
src = mlab.pipeline.open("3D-models/model-41/Segmentation_41.stl")
#src = mlab.pipeline.open("3D-models/model-70/Segmentation_70-LPS.stl")
#src = mlab.pipeline.open("3D-models/model-74/Segmentation_74-LPS.stl")
#src = mlab.pipeline.open("3D-models/model-80/Segmentation_80-LPS.stl")
#src = mlab.pipeline.open("3D-models/model-103/Segmentation_103-LPS.stl")
#src = mlab.pipeline.open("3D-models/model-122/Segmentation_122-LPS.stl")
#src = mlab.pipeline.open("3D-models/model-158/Segmentation_158-LPS.stl")
#src = mlab.pipeline.open("3D-models/model-197/Segmentation_197-LPS.stl")

# List of file names to process
file_names = [
			'41 occip',
			#'70 occip',
			#'74 occip',
			#'80 occip'
			#'103 occip',
			#'122 occip'
			#'158 occip',
			#'197 occip',
	    ]

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

	# Tuning the reference points by adding some offset, in this case to the occip Point
	x_tune_left_mast  = 0; y_tune_left_mast  = 0; z_tune_left_mast  = 0
	x_tune_right_mast = 0; y_tune_right_mast = 0; z_tune_right_mast = 0
	if   file_name == '41 occip':
		x_tune_left_mast = 0  
		y_tune_left_mast = 0    
		z_tune_left_mast = 0    
		x_tune_right_mast = 0 
		y_tune_right_mast = 0 
		z_tune_right_mast = 0 
		x_tune_occip = 0
		y_tune_occip = 0
		z_tune_occip = 0
		BACKREF = [70.24827575683594, 4.429444789886475, -160.20277404785157], [-60.652923583984378, 2.278567314147949, -170.90626525878907], [2.59171462059021, 70.44351196289063, -143.6399383544922]
		

	elif file_name == '70 occip':
		x_tune_left_mast = 0
		y_tune_left_mast = 0
		z_tune_left_mast = 0
		x_tune_right_mast = 0
		y_tune_right_mast = 0
		z_tune_right_mast = 0
		x_tune_occip = 0
		y_tune_occip = 0
		z_tune_occip = 0
		BACKREF = [47.76381301879883, 10.53895092010498, -7.34036922454834], [-60.14876937866211, 7.620923042297363, -8.089339256286621], [-10.045451164245606, 78.60271453857422, 25.53517723083496]

	elif file_name == '74 occip':
		x_tune_left_mast = 0
		y_tune_left_mast = 0
		z_tune_left_mast = 0
		x_tune_right_mast = 0
		y_tune_right_mast = 0
		z_tune_right_mast = 0
		x_tune_occip = 0
		y_tune_occip = 0
		z_tune_occip = 0
		BACKREF = [63.61101150512695, 50.00296401977539, -172.4718780517578], [-53.986854553222659, 53.37822723388672, -176.2224578857422], [4.411401271820068, 111.36182403564453, -143.51705932617188]


	elif file_name == '80 occip':
		x_tune_left_mast = -5
		y_tune_left_mast = 0 
		z_tune_left_mast = 0
		x_tune_right_mast = 0
		y_tune_right_mast = 0
		z_tune_right_mast = 0
		x_tune_occip = 2
		y_tune_occip = 0
		z_tune_occip = 0
		BACKREF = [61.21136474609375, 23.564613342285158, 6.267281532287598], [-69.81128692626953, 25.006391525268556, 0.920551598072052], [1.7626334428787232, 77.40547180175781, 21.632661819458009]

	elif file_name == '103 occip':
		x_tune_left_mast = 2
		y_tune_left_mast = 0
		z_tune_left_mast = 0
		x_tune_right_mast = 10
		y_tune_right_mast = 0
		z_tune_right_mast = 0
		x_tune_occip = 0
		y_tune_occip = 2
		z_tune_occip = 0
		BACKREF = [49.011940002441409, 5.087569713592529, -4.8318634033203129], [-59.19563674926758, 4.938868522644043, -2.5156471729278566], [-3.6546974182128908, 76.3985824584961, 30.335678100585939]

	elif file_name == '122 occip':
		x_tune_left_mast = 0
		y_tune_left_mast = 0
		z_tune_left_mast = 0
		x_tune_right_mast = 0
		y_tune_right_mast = 0
		z_tune_right_mast = 0
		x_tune_occip = 0
		y_tune_occip = -6
		z_tune_occip = 0
		BACKREF = [63.61101150512695, 50.00296401977539, -172.4718780517578], [-53.986854553222659, 53.37822723388672, -176.2224578857422], [4.411401271820068, 111.36182403564453, -143.51705932617188]

	elif file_name == '158 occip':
		x_tune_left_mast = 0
		y_tune_left_mast = 0
		z_tune_left_mast = 0
		x_tune_right_mast = 0
		y_tune_right_mast = 0
		z_tune_right_mast = 0
		x_tune_occip = 0
		y_tune_occip = 5
		z_tune_occip = 0
		BACKREF = [68.57957458496094, 13.81441593170166, -170.11367797851563], [-65.59436798095703, 1.4701181650161744, -178.40963745117188],[-5.299604415893555, 74.41988372802735, -163.0026397705078] 

	elif file_name == '197 occip':
		x_tune_left_mast = 0
		y_tune_left_mast = -5
		z_tune_left_mast = 0
		x_tune_right_mast = 0
		y_tune_right_mast = -10
		z_tune_right_mast = 0
		x_tune_occip = 0
		y_tune_occip = 0
		z_tune_occip = 0
		BACKREF = [60.52559280395508, 8.54175853729248, -9.985729217529297], [-58.57665252685547, 7.98490571975708, -4.698486328125], [7.323022842407227, 83.48851776123047, 29.42506980895996]


	# Extracting and tuning reference points
	left_mast = [old_reference_points.loc[0, 'x1_l'] + x_tune_right_mast , old_reference_points.loc[0, 'y1_l'] + y_tune_right_mast , old_reference_points.loc[0, 'z1_l'] + z_tune_right_mast]
	right_mast  = [old_reference_points.loc[1, 'x1_l'] + x_tune_left_mast, old_reference_points.loc[1, 'y1_l'] + y_tune_left_mast, old_reference_points.loc[1, 'z1_l'] + y_tune_left_mast]
	occip      = [old_reference_points.loc[2, 'x1_l'] + x_tune_occip , old_reference_points.loc[2, 'y1_l']+ y_tune_occip, old_reference_points.loc[2, 'z1_l'] + z_tune_occip]

	####### Left Side #######

	# Calculating the least square transform (check the helper function for further details)
	# The numerical coordinates were obtained from 3D Slicer
	T, _, _ = least_square_transform([         left_mast,   				right_mast, 					    occip            ],
	                                 [BACKREF[0], BACKREF[1], BACKREF[2]])

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

	# Switching the order of the first 2 columns so the occip is in the middle (for representation later)
	row1 = new_points_df_left_side.iloc[1].copy()
	row2 = new_points_df_left_side.iloc[2].copy()

	new_points_df_left_side.iloc[1] = row2
	new_points_df_left_side.iloc[2] = row1
	
	# Dropping last 2 vlueless rows
	#new_points_df_left_side.drop(new_points_df_left_side.tail(2).index, inplace=True)

	####### Right Side #######
	
	# Calculating the least square transform (check the helper function for further details)
	T, _, _ = least_square_transform([         left_mast,   				right_mast, 					    occip            ],
	                                 [BACKREF[0], BACKREF[1], BACKREF[2]])
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

	# Switching the order of the first 2 columns so the occip is in the middle of the 2 masts
	row1 = new_points_df_right_side.iloc[1].copy()
	row2 = new_points_df_right_side.iloc[2].copy()

	new_points_df_right_side.iloc[1] = row2
	new_points_df_right_side.iloc[2] = row1

	# Dropping last 2 vlueless rows
	#new_points_df_right_side.drop(new_points_df_right_side.tail(2).index, inplace=True)


	###### Merge Both Sides ######

	# Constructing the absolute file path
	file_name_without_extension = file_name.split(".xlsx")[0]
	rel_path = f"Modified Datasets/new_{file_name_without_extension}.csv"
	abs_file_path = os.path.join(script_dir, rel_path)

	new_points_df = pd.concat([new_points_df_right_side, new_points_df_left_side], axis=1)
	
    # Saving to a .cvs file for visualisation in Paraview if needed
	new_points_df.to_csv(abs_file_path, index=False)


################# Visualisation #################



# Loading mesh data from .STL file

mesh = mlab.pipeline.surface(src)

# Defining the color mapping dictionary
color_mapping = {
    1: (0.0, 0.0, 0.0),  # Black for Skull
    2: (0.0, 0.0, 0.0),  # Black for Skull
    3: (0.0, 0.0, 0.0),  # Black for Skull
    4: (0.0, 0.0, 0.0),  # Black for Skull
	5: (0.0, 1.0, 0.0),  # Green for Mediaal
	6: (0.0, 0.0, 1.0),  # Blue for Intermediaal
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
			mlab.plot3d(pts[:, 0], pts[:, 1], pts[:, 2], color=line_color, tube_radius=1.5, opacity=0.2)

	for color, pts in points_left_side.items():
		pts = np.array(pts)
		if len(pts) > 1:
			line_color = color_mapping.get(color)
			mlab.plot3d(pts[:, 0], pts[:, 1], pts[:, 2], color=line_color, tube_radius=1.5, opacity=0.2)

# Adding a custom legend using text annotations
mlab.text(-80, 0, 'Mediaal', z=40, width=0.2, color=(0.0, 1.0, 0.0))  # Green
mlab.text(-80, 0, 'Intermediaal', z=60, width=0.2, color=(0.0, 0.0, 1.0))  # Blue
mlab.text(-80, 0, 'Lateraal', z=80, width=0.2, color=(1.0, 0.0, 0.0))  # Red

# Setting the desired orientation when the file is opened
mlab.view(azimuth=90, elevation=90, distance=450)

# Showing the plot
mlab.show()
print(lines_left_side)