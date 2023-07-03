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
#src = mlab.pipeline.open("3D-models/model-41/Segmentation_41.stl")
#src = mlab.pipeline.open("3D-models/model-70/Segmentation_70-LPS.stl")
src = mlab.pipeline.open("3D-models/model-74/Segmentation_74.stl")
#src = mlab.pipeline.open("3D-models/model-80/Segmentation_80-LPS.stl")
#src = mlab.pipeline.open("3D-models/model-103/Segmentation_103-LPS.stl")
#src = mlab.pipeline.open("3D-models/model-122/Segmentation_122-LPS.stl")
#src = mlab.pipeline.open("3D-models/model-158/Segmentation_158-LPS.stl")
#src = mlab.pipeline.open("3D-models/model-197/Segmentation_197-LPS.stl")

# List of file names to process
file_names = [
	        #'41 Supraorb', 
	        #'70 Supraorb',
	        '74 Supraorb',
            #'80 Supraorb',
	        #'103 Supraorb',
	        #'122 Supraorb',
			#'158 Supraorb',
            #'197 Supraorb',
			#'74 Supraorb copy'

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

	# Tuning the reference points by adding some offset, in this case to the Nose Point
	x_tune_left_eye  = 0; y_tune_left_eye  = 0; z_tune_left_eye  = 0
	x_tune_right_eye = 0; y_tune_right_eye = 0; z_tune_right_eye = 0
	if   file_name == '41 Supraorb':
		x_tune_left_eye = 0   #
		y_tune_left_eye = -2    #
		z_tune_left_eye = 0   #
		x_tune_right_eye = -2 #
		y_tune_right_eye = 0 #
		z_tune_right_eye = 0 #
		x_tune_nose = 0
		y_tune_nose = 5
		z_tune_nose = 0
		FRONTREF = [55.25961685180664, -87.12602996826172, -135.50506591796876],[-56.16524124145508, -84.362548828125, -128.65228271484376],[1.966705322265625, -122.24573516845703, -138.52085876464845]
		
	elif file_name == '70 Supraorb':
		x_tune_left_eye = 0
		y_tune_left_eye = 0 
		z_tune_left_eye = -2
		x_tune_right_eye = 0
		y_tune_right_eye = 0
		z_tune_right_eye = -2
		x_tune_nose = 0
		y_tune_nose = 0
		z_tune_nose = 0
		FRONTREF = [51.78400421142578, -73.97721862792969, 20.209863662719728], [-56.1229133605957, -76.30559539794922, 12.934329986572266], [-2.1589505672454836, -107.05281829833985, 14.846169471740723]

	elif file_name ==  '74 Supraorb':
		x_tune_left_eye = 0
		y_tune_left_eye = -4  
		z_tune_left_eye = 0
		x_tune_right_eye = 0
		y_tune_right_eye = 0 
		z_tune_right_eye = 0 
		x_tune_nose = -3
		y_tune_nose = 0
		z_tune_nose = 0
		FRONTREF = [44.21689224243164, -71.94463348388672, 14.214385986328125], [-58.45985412597656, -67.92092895507813, 20.508426666259767], [-8.899336814880371, -98.78041076660156, 13.033451080322266]
	elif file_name ==  '74 Supraorb copy':
		x_tune_left_eye = 0
		y_tune_left_eye = -4  
		z_tune_left_eye = 0
		x_tune_right_eye = 0
		y_tune_right_eye = 0 
		z_tune_right_eye = 0 
		x_tune_nose = -3
		y_tune_nose = 0
		z_tune_nose = 0
		FRONTREF = [44.21689224243164, -71.94463348388672, 14.214385986328125], [-58.45985412597656, -67.92092895507813, 20.508426666259767], [-8.899336814880371, -98.78041076660156, 13.033451080322266]

	elif file_name == '80 Supraorb':
		x_tune_left_eye = 0
		y_tune_left_eye = 0  
		z_tune_left_eye = 0
		x_tune_right_eye = 0
		y_tune_right_eye = 0 
		z_tune_right_eye = 0
		x_tune_nose = 0
		y_tune_nose = 0
		z_tune_nose = 0
		FRONTREF = [50.04569625854492, -70.22789764404297, 13.373350143432618], [-59.88399124145508, -62.80413818359375, 9.427675247192383], [-8.124140739440918, -93.5909194946289, 6.681548118591309] 

	elif file_name == '103 Supraorb':
		x_tune_left_eye = 0
		y_tune_left_eye = 0  
		z_tune_left_eye = 0
		x_tune_right_eye = 0
		y_tune_right_eye = 0
		z_tune_right_eye = 0
		x_tune_nose = 0
		y_tune_nose = 3
		z_tune_nose = 0
		FRONTREF = [55.579071044921878, -86.44158172607422, 24.30135726928711], [-59.00012969970703, -87.49335479736328, 25.803449630737306], [-1.1131476627790938, -115.92743167807599, 15.733926443472117]

	elif file_name == '122 Supraorb':
		x_tune_left_eye = 0
		y_tune_left_eye = 0
		z_tune_left_eye = 0
		x_tune_right_eye = 0
		y_tune_right_eye = 0
		z_tune_right_eye = 0
		x_tune_nose = 0
		y_tune_nose = -2
		z_tune_nose = 0
		FRONTREF = [55.142173767089847, -44.00822448730469, -150.07098388671876], [-49.563716888427737, -37.93690872192383, -156.22598266601563], [0.7237986326217651, -72.89681243896485, -154.26702880859376]

	elif file_name == '158 Supraorb':
		x_tune_left_eye = 0
		y_tune_left_eye = 0
		z_tune_left_eye = 0
		x_tune_right_eye = 0
		y_tune_right_eye = 0
		z_tune_right_eye = 0
		x_tune_nose = 0
		y_tune_nose = 0
		z_tune_nose = 0
		FRONTREF = [57.80643844604492, -88.92672729492188, -117.39237213134766], [-59.856101989746097, -86.77534484863281, -126.3244857788086], [-0.5251496434211731, -125.59642028808594, -120.52300262451172]

	elif file_name == '197 Supraorb':
		x_tune_left_eye = 0
		y_tune_left_eye = 0
		z_tune_left_eye = 0
		x_tune_right_eye = 0
		y_tune_right_eye = 0
		z_tune_right_eye = 0 
		x_tune_nose = 0
		y_tune_nose = -2
		z_tune_nose = 0
		FRONTREF = [54.441688537597659, -83.47369384765625, 23.737031936645509], [-57.96451187133789, -80.4339828491211, 22.889888763427736], [-1.3099538087844849, -98.52961730957031, 21.30008888244629]

	# Extracting reference points
	right_eye = [old_reference_points.loc[0, 'x1_l'] + x_tune_right_eye , old_reference_points.loc[0, 'y1_l'] + y_tune_right_eye , old_reference_points.loc[0, 'z1_l'] + z_tune_right_eye]
	left_eye  = [old_reference_points.loc[1, 'x1_l'] + x_tune_left_eye, old_reference_points.loc[1, 'y1_l'] + y_tune_left_eye, old_reference_points.loc[1, 'z1_l'] + y_tune_left_eye]
	nose      = [old_reference_points.loc[2, 'x1_l'] + x_tune_nose , old_reference_points.loc[2, 'y1_l']+ y_tune_nose, old_reference_points.loc[2, 'z1_l'] + z_tune_nose]

	####### Left Side #######

	# Calculating the least square transform (check the helper function for further details)
	# The numerical coordinates were obtained from 3D Slicer
	T, _, _ = least_square_transform([         left_eye,   				right_eye, 					    nose            ],
	                                 [FRONTREF[0], FRONTREF[1], FRONTREF[2]])

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
	
	# Calculating the least square transform (check the helper function for further details)
	T, _, _ = least_square_transform([         left_eye,   				right_eye, 					    nose            ],
	                                 [FRONTREF[0], FRONTREF[1], FRONTREF[2]])
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
mlab.view(azimuth=0, elevation=90, distance=450)

# Showing the plot
mlab.show()