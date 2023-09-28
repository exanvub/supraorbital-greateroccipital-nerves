import json

import math

# Load the JSON data from the file
#with open('/Users/nicolas/Library/CloudStorage/OneDrive-VrijeUniversiteitBrussel/Github/exanvub/supraorbital-greateroccipital-nerves/src/Calculations/DATA/torus-json-files/41-GON-torusdata.mrk.json', 'r') as json_file:
#with open('/Users/nicolas/Library/CloudStorage/OneDrive-VrijeUniversiteitBrussel/Github/exanvub/supraorbital-greateroccipital-nerves/src/Calculations/DATA/torus-json-files/70-GON-torusdata.mrk.json', 'r') as json_file:
#with open('/Users/nicolas/Library/CloudStorage/OneDrive-VrijeUniversiteitBrussel/Github/exanvub/supraorbital-greateroccipital-nerves/src/Calculations/DATA/torus-json-files/74-GON-torusdata.mrk.json', 'r') as json_file:
#with open('/Users/nicolas/Library/CloudStorage/OneDrive-VrijeUniversiteitBrussel/Github/exanvub/supraorbital-greateroccipital-nerves/src/Calculations/DATA/torus-json-files/80-GON-torusdata.mrk.json', 'r') as json_file:
#with open('/Users/nicolas/Library/CloudStorage/OneDrive-VrijeUniversiteitBrussel/Github/exanvub/supraorbital-greateroccipital-nerves/src/Calculations/DATA/torus-json-files/103-GON-torusdata.mrk.json', 'r') as json_file:
#with open('/Users/nicolas/Library/CloudStorage/OneDrive-VrijeUniversiteitBrussel/Github/exanvub/supraorbital-greateroccipital-nerves/src/Calculations/DATA/torus-json-files/122-GON-torusdata.mrk.json', 'r') as json_file:
#with open('/Users/nicolas/Library/CloudStorage/OneDrive-VrijeUniversiteitBrussel/Github/exanvub/supraorbital-greateroccipital-nerves/src/Calculations/DATA/torus-json-files/157-GON-torusdata.mrk.json', 'r') as json_file:
#with open('/Users/nicolas/Library/CloudStorage/OneDrive-VrijeUniversiteitBrussel/Github/exanvub/supraorbital-greateroccipital-nerves/src/Calculations/DATA/torus-json-files/158-GON-torusdata.mrk.json', 'r') as json_file:
#with open('/Users/nicolas/Library/CloudStorage/OneDrive-VrijeUniversiteitBrussel/Github/exanvub/supraorbital-greateroccipital-nerves/src/Calculations/DATA/torus-json-files/183-GON-torusdata.mrk.json', 'r') as json_file:
with open('/Users/nicolas/Library/CloudStorage/OneDrive-VrijeUniversiteitBrussel/Github/exanvub/supraorbital-greateroccipital-nerves/src/Calculations/DATA/torus-json-files/197-GON-torusdata.mrk.json', 'r') as json_file:



    data = json.load(json_file)

# Create a dictionary to store the variables
fiducial_variables = {}

# Iterate through the 'controlPoints' in the 'markups' section
for control_point in data['markups'][0]['controlPoints']:
    label = control_point['label']
    position = control_point['position']
    fiducial_variables[label] = position

# Function to calculate the Euclidean distance between two 3D points
def calculate_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2 + (point1[2] - point2[2])**2)

# Calculate the distance between FL-c and FL-L-gon
try:
    distance_FL_c_FL_L_gon = calculate_distance(fiducial_variables['FL-c'], fiducial_variables['FL-L-gon'])
except KeyError:
    distance_FL_c_FL_L_gon = 'N/A'

# Calculate the distance between FL-c and FL-R-gon
try:
    distance_FL_c_FL_R_gon = calculate_distance(fiducial_variables['FL-c'], fiducial_variables['FL-R-gon'])
except KeyError:
    distance_FL_c_FL_R_gon = 'N/A'

# Calculate the sum of distances between EOP-c, EOP-L-1, EOP-L-2, and EOP-L-med
try:
    EOP_c_EOP_L_1 = calculate_distance(fiducial_variables['EOP-c'], fiducial_variables['EOP-L-1'])
    EOP_L_1_EOP_L_2 = calculate_distance(fiducial_variables['EOP-L-1'], fiducial_variables['EOP-L-2'])
    EOP_L_2_EOP_L_med = calculate_distance(fiducial_variables['EOP-L-2'], fiducial_variables['EOP-L-med'])
    sum_EOP_c_EOP_med = EOP_c_EOP_L_1 + EOP_L_1_EOP_L_2 + EOP_L_2_EOP_L_med
except KeyError:
    sum_EOP_c_EOP_med = 'N/A'

# Calculate the sum of distances between EOP-c, EOP-R-1, EOP-R-2, and EOP-R-med
try:
    EOP_c_EOP_R_1 = calculate_distance(fiducial_variables['EOP-c'], fiducial_variables['EOP-R-1'])
    EOP_R_1_EOP_R_2 = calculate_distance(fiducial_variables['EOP-R-1'], fiducial_variables['EOP-R-2'])
    EOP_R_2_EOP_R_med = calculate_distance(fiducial_variables['EOP-R-2'], fiducial_variables['EOP-R-med'])
    sum_EOP_R_c_EOP_R_med = EOP_c_EOP_R_1 + EOP_R_1_EOP_R_2 + EOP_R_2_EOP_R_med
except KeyError:
    sum_EOP_R_c_EOP_R_med = 'N/A'

# Calculate the distance between EOP-c, EOP-L-1, EOP-L-2 and EOP-L-lat
try:
    EOP_c_EOP_L_1 = calculate_distance(fiducial_variables['EOP-c'], fiducial_variables['EOP-L-1'])
    EOP_L_1_EOP_L_2 = calculate_distance(fiducial_variables['EOP-L-1'], fiducial_variables['EOP-L-2'])
    EOP_L_2_EOP_L_lat = calculate_distance(fiducial_variables['EOP-L-2'], fiducial_variables['EOP-L-lat'])
    sum_EOP_c_EOP_L_lat = EOP_c_EOP_L_1 + EOP_L_1_EOP_L_2 + EOP_L_2_EOP_L_lat
except KeyError:
    sum_EOP_c_EOP_L_lat = 'N/A'

# Calculate the distance between EOP-c, EOP-R-1, EOP-R-2 and EOP-R-lat
try:
    EOP_c_EOP_R_1 = calculate_distance(fiducial_variables['EOP-c'], fiducial_variables['EOP-R-1'])
    EOP_R_1_EOP_R_2 = calculate_distance(fiducial_variables['EOP-R-1'], fiducial_variables['EOP-R-2'])
    EOP_R_2_EOP_R_lat = calculate_distance(fiducial_variables['EOP-R-2'], fiducial_variables['EOP-R-lat'])
    sum_EOP_c_EOP_R_lat = EOP_c_EOP_R_1 + EOP_R_1_EOP_R_2 + EOP_R_2_EOP_R_lat
except KeyError:
    sum_EOP_c_EOP_R_lat = 'N/A'

# Calculate the distance between EOP-c, EOP-L-1, EOP-L-2 and EOP-L-latmed
try:
    EOP_c_EOP_L_1 = calculate_distance(fiducial_variables['EOP-c'], fiducial_variables['EOP-L-1'])
    EOP_L_1_EOP_L_2 = calculate_distance(fiducial_variables['EOP-L-1'], fiducial_variables['EOP-L-2'])
    EOP_L_2_EOP_L_latmed = calculate_distance(fiducial_variables['EOP-L-2'], fiducial_variables['EOP-L-latmed'])
    sum_EOP_c_EOP_L_latmed = EOP_c_EOP_L_1 + EOP_L_1_EOP_L_2 + EOP_L_2_EOP_L_latmed
except KeyError:
    sum_EOP_c_EOP_L_latmed = 'N/A'

# Calculate the distance between EOP-c, EOP-R-1, EOP-R-2 and EOP-R-latmed
try:
    EOP_c_EOP_R_1 = calculate_distance(fiducial_variables['EOP-c'], fiducial_variables['EOP-R-1'])
    EOP_R_1_EOP_R_2 = calculate_distance(fiducial_variables['EOP-R-1'], fiducial_variables['EOP-R-2'])
    EOP_R_2_EOP_R_latmed = calculate_distance(fiducial_variables['EOP-R-2'], fiducial_variables['EOP-R-latmed'])
    sum_EOP_c_EOP_R_latmed = EOP_c_EOP_R_1 + EOP_R_1_EOP_R_2 + EOP_R_2_EOP_R_latmed
except KeyError:
    sum_EOP_c_EOP_R_latmed = 'N/A'

# Calculate the distance between EOP-c, EOP-L-1, EOP-L-2 and EOP-L-latlat
try:
    EOP_c_EOP_L_1 = calculate_distance(fiducial_variables['EOP-c'], fiducial_variables['EOP-L-1'])
    EOP_L_1_EOP_L_2 = calculate_distance(fiducial_variables['EOP-L-1'], fiducial_variables['EOP-L-2'])
    EOP_L_2_EOP_L_latlat = calculate_distance(fiducial_variables['EOP-L-2'], fiducial_variables['EOP-L-latlat'])
    sum_EOP_c_EOP_L_latlat = EOP_c_EOP_L_1 + EOP_L_1_EOP_L_2 + EOP_L_2_EOP_L_latlat
except KeyError:
    sum_EOP_c_EOP_L_latlat = 'N/A'

# Calculate the distance between EOP-c, EOP-R-1, EOP-R-2 and EOP-R-latlat
try:
    EOP_c_EOP_R_1 = calculate_distance(fiducial_variables['EOP-c'], fiducial_variables['EOP-R-1'])
    EOP_R_1_EOP_R_2 = calculate_distance(fiducial_variables['EOP-R-1'], fiducial_variables['EOP-R-2'])
    EOP_R_2_EOP_R_latlat = calculate_distance(fiducial_variables['EOP-R-2'], fiducial_variables['EOP-R-latlat'])
    sum_EOP_c_EOP_R_latlat = EOP_c_EOP_R_1 + EOP_R_1_EOP_R_2 + EOP_R_2_EOP_R_latlat
except KeyError:
    sum_EOP_c_EOP_R_latlat = 'N/A'

# Calculate the distance between L1-c, L1-L-1, L1-L-2 and L1-L-med
try:
    L1_c_L1_L_1 = calculate_distance(fiducial_variables['L1-c'], fiducial_variables['L1-L-1'])
    L1_L_1_L1_L_2 = calculate_distance(fiducial_variables['L1-L-1'], fiducial_variables['L1-L-2'])
    L1_L_2_L1_L_med = calculate_distance(fiducial_variables['L1-L-2'], fiducial_variables['L1-L-med'])
    sum_L1_c_L1_L_med = L1_c_L1_L_1 + L1_L_1_L1_L_2 + L1_L_2_L1_L_med
except KeyError:
    sum_L1_c_L1_L_med = 'N/A'

# Calculate the distance between L1-c, L1-R-1, L1-R-2 and L1-R-med
try:
    L1_c_L1_R_1 = calculate_distance(fiducial_variables['L1-c'], fiducial_variables['L1-R-1'])
    L1_R_1_L1_R_2 = calculate_distance(fiducial_variables['L1-R-1'], fiducial_variables['L1-R-2'])
    L1_R_2_L1_R_med = calculate_distance(fiducial_variables['L1-R-2'], fiducial_variables['L1-R-med'])
    sum_L1_c_L1_R_med = L1_c_L1_R_1 + L1_R_1_L1_R_2 + L1_R_2_L1_R_med
except KeyError:
    sum_L1_c_L1_R_med = 'N/A'

# Calculate the distance between L1-c, L1-L-1, L1-L-2 and L1-L-lat
try:
    L1_c_L1_L_1 = calculate_distance(fiducial_variables['L1-c'], fiducial_variables['L1-L-1'])
    L1_L_1_L1_L_2 = calculate_distance(fiducial_variables['L1-L-1'], fiducial_variables['L1-L-2'])
    L1_L_2_L1_L_lat = calculate_distance(fiducial_variables['L1-L-2'], fiducial_variables['L1-L-lat'])
    sum_L1_c_L1_L_lat = L1_c_L1_L_1 + L1_L_1_L1_L_2 + L1_L_2_L1_L_lat
except KeyError:
    sum_L1_c_L1_L_lat = 'N/A'

# Calculate the distance between L1-c, L1-R-1, L1-R-2 and L1-R-lat
try:
    L1_c_L1_R_1 = calculate_distance(fiducial_variables['L1-c'], fiducial_variables['L1-R-1'])
    L1_R_1_L1_R_2 = calculate_distance(fiducial_variables['L1-R-1'], fiducial_variables['L1-R-2'])
    L1_R_2_L1_R_lat = calculate_distance(fiducial_variables['L1-R-2'], fiducial_variables['L1-R-lat'])
    sum_L1_c_L1_R_lat = L1_c_L1_R_1 + L1_R_1_L1_R_2 + L1_R_2_L1_R_lat
except KeyError:
    sum_L1_c_L1_R_lat = 'N/A'

# Calculate the distance between L1-c, L1-L-1, L1-L-2 and L1-L-latmed
try:
    L1_c_L1_L_1 = calculate_distance(fiducial_variables['L1-c'], fiducial_variables['L1-L-1'])
    L1_L_1_L1_L_2 = calculate_distance(fiducial_variables['L1-L-1'], fiducial_variables['L1-L-2'])
    L1_L_2_L1_L_latmed = calculate_distance(fiducial_variables['L1-L-2'], fiducial_variables['L1-L-latmed'])
    sum_L1_c_L1_L_latmed = L1_c_L1_L_1 + L1_L_1_L1_L_2 + L1_L_2_L1_L_latmed
except KeyError:
    sum_L1_c_L1_L_latmed = 'N/A'

# Calculate the distance between L1-c, L1-R-1, L1-R-2 and L1-R-latmed
try:
    L1_c_L1_R_1 = calculate_distance(fiducial_variables['L1-c'], fiducial_variables['L1-R-1'])
    L1_R_1_L1_R_2 = calculate_distance(fiducial_variables['L1-R-1'], fiducial_variables['L1-R-2'])
    L1_R_2_L1_R_latmed = calculate_distance(fiducial_variables['L1-R-2'], fiducial_variables['L1-R-latmed'])
    sum_L1_c_L1_R_latmed = L1_c_L1_R_1 + L1_R_1_L1_R_2 + L1_R_2_L1_R_latmed
except KeyError:
    sum_L1_c_L1_R_latmed = 'N/A'

# Calculate the distance between L1-c, L1-L-1, L1-L-2 and L1-L-latlat
try:
    L1_c_L1_L_1 = calculate_distance(fiducial_variables['L1-c'], fiducial_variables['L1-L-1'])
    L1_L_1_L1_L_2 = calculate_distance(fiducial_variables['L1-L-1'], fiducial_variables['L1-L-2'])
    L1_L_2_L1_L_latlat = calculate_distance(fiducial_variables['L1-L-2'], fiducial_variables['L1-L-latlat'])
    sum_L1_c_L1_L_latlat = L1_c_L1_L_1 + L1_L_1_L1_L_2 + L1_L_2_L1_L_latlat
except KeyError:
    sum_L1_c_L1_L_latlat = 'N/A'

# Calculate the distance between L1-c, L1-R-1, L1-R-2 and L1-R-latlat
try:
    L1_c_L1_R_1 = calculate_distance(fiducial_variables['L1-c'], fiducial_variables['L1-R-1'])
    L1_R_1_L1_R_2 = calculate_distance(fiducial_variables['L1-R-1'], fiducial_variables['L1-R-2'])
    L1_R_2_L1_R_latlat = calculate_distance(fiducial_variables['L1-R-2'], fiducial_variables['L1-R-latlat'])
    sum_L1_c_L1_R_latlat = L1_c_L1_R_1 + L1_R_1_L1_R_2 + L1_R_2_L1_R_latlat
except KeyError:
    sum_L1_c_L1_R_latlat = 'N/A'

# Calculate the distance between L2-c, L2-L-1, L2-L-2 and L2-L-med
try:
    L2_c_L2_L_1 = calculate_distance(fiducial_variables['L2-c'], fiducial_variables['L2-L-1'])
    L2_L_1_L2_L_2 = calculate_distance(fiducial_variables['L2-L-1'], fiducial_variables['L2-L-2'])
    L2_L_2_L2_L_med = calculate_distance(fiducial_variables['L2-L-2'], fiducial_variables['L2-L-med'])
    sum_L2_c_L2_L_med = L2_c_L2_L_1 + L2_L_1_L2_L_2 + L2_L_2_L2_L_med
except KeyError:
    sum_L2_c_L2_L_med = 'N/A'

# Calculate the distance between L2-c, L2-R-1, L2-R-2 and L2-R-med
try:
    L2_c_L2_R_1 = calculate_distance(fiducial_variables['L2-c'], fiducial_variables['L2-R-1'])
    L2_R_1_L2_R_2 = calculate_distance(fiducial_variables['L2-R-1'], fiducial_variables['L2-R-2'])
    L2_R_2_L2_R_med = calculate_distance(fiducial_variables['L2-R-2'], fiducial_variables['L2-R-med'])
    sum_L2_c_L2_R_med = L2_c_L2_R_1 + L2_R_1_L2_R_2 + L2_R_2_L2_R_med
except KeyError:
    sum_L2_c_L2_R_med = 'N/A'

# Calculate the distance between L2-c, L2-L-1, L2-L-2 and L2-L-lat
try:
    L2_c_L2_L_1 = calculate_distance(fiducial_variables['L2-c'], fiducial_variables['L2-L-1'])
    L2_L_1_L2_L_2 = calculate_distance(fiducial_variables['L2-L-1'], fiducial_variables['L2-L-2'])
    L2_L_2_L2_L_lat = calculate_distance(fiducial_variables['L2-L-2'], fiducial_variables['L2-L-lat'])
    sum_L2_c_L2_L_lat = L2_c_L2_L_1 + L2_L_1_L2_L_2 + L2_L_2_L2_L_lat
except KeyError:
    sum_L2_c_L2_L_lat = 'N/A'

# Calculate the distance between L2-c, L2-R-1, L2-R-2 and L2-R-lat
try:
    L2_c_L2_R_1 = calculate_distance(fiducial_variables['L2-c'], fiducial_variables['L2-R-1'])
    L2_R_1_L2_R_2 = calculate_distance(fiducial_variables['L2-R-1'], fiducial_variables['L2-R-2'])
    L2_R_2_L2_R_lat = calculate_distance(fiducial_variables['L2-R-2'], fiducial_variables['L2-R-lat'])
    sum_L2_c_L2_R_lat = L2_c_L2_R_1 + L2_R_1_L2_R_2 + L2_R_2_L2_R_lat
except KeyError:
    sum_L2_c_L2_R_lat = 'N/A'

# Calculate the distance between L2-c, L2-L-1, L2-L-2 and L2-L-latmed
try:
    L2_c_L2_L_1 = calculate_distance(fiducial_variables['L2-c'], fiducial_variables['L2-L-1'])
    L2_L_1_L2_L_2 = calculate_distance(fiducial_variables['L2-L-1'], fiducial_variables['L2-L-2'])
    L2_L_2_L2_L_latmed = calculate_distance(fiducial_variables['L2-L-2'], fiducial_variables['L2-L-latmed'])
    sum_L2_c_L2_L_latmed = L2_c_L2_L_1 + L2_L_1_L2_L_2 + L2_L_2_L2_L_latmed
except KeyError:
    sum_L2_c_L2_L_latmed = 'N/A'

# Calculate the distance between L2-c, L2-R-1, L2-R-2 and L2-R-latmed
try:
    L2_c_L2_R_1 = calculate_distance(fiducial_variables['L2-c'], fiducial_variables['L2-R-1'])
    L2_R_1_L2_R_2 = calculate_distance(fiducial_variables['L2-R-1'], fiducial_variables['L2-R-2'])
    L2_R_2_L2_R_latmed = calculate_distance(fiducial_variables['L2-R-2'], fiducial_variables['L2-R-latmed'])
    sum_L2_c_L2_R_latmed = L2_c_L2_R_1 + L2_R_1_L2_R_2 + L2_R_2_L2_R_latmed
except KeyError:
    sum_L2_c_L2_R_latmed = 'N/A'

# Calculate the distance between L2-c, L2-L-1, L2-L-2 and L2-L-latlat
try:
    L2_c_L2_L_1 = calculate_distance(fiducial_variables['L2-c'], fiducial_variables['L2-L-1'])
    L2_L_1_L2_L_2 = calculate_distance(fiducial_variables['L2-L-1'], fiducial_variables['L2-L-2'])
    L2_L_2_L2_L_latlat = calculate_distance(fiducial_variables['L2-L-2'], fiducial_variables['L2-L-latlat'])
    sum_L2_c_L2_L_latlat = L2_c_L2_L_1 + L2_L_1_L2_L_2 + L2_L_2_L2_L_latlat
except KeyError:
    sum_L2_c_L2_L_latlat = 'N/A'

# Calculate the distance between L2-c, L2-R-1, L2-R-2 and L2-R-latlat
try:
    L2_c_L2_R_1 = calculate_distance(fiducial_variables['L2-c'], fiducial_variables['L2-R-1'])
    L2_R_1_L2_R_2 = calculate_distance(fiducial_variables['L2-R-1'], fiducial_variables['L2-R-2'])
    L2_R_2_L2_R_latlat = calculate_distance(fiducial_variables['L2-R-2'], fiducial_variables['L2-R-latlat'])
    sum_L2_c_L2_R_latlat = L2_c_L2_R_1 + L2_R_1_L2_R_2 + L2_R_2_L2_R_latlat
except KeyError:
    sum_L2_c_L2_R_latlat = 'N/A'




# Print the calculated distances
print(f"Distance between FL-c and FL-L-gon: {distance_FL_c_FL_L_gon}")
print(f"Distance between FL-c and FL-R-gon: {distance_FL_c_FL_R_gon}")
print(f"Distance between EOP-c and EOP-L-med: {sum_EOP_c_EOP_med}")
print(f"Distance between EOP-c and EOP-R-med: {sum_EOP_R_c_EOP_R_med}")
print(f"Distance between EOP-c and EOP-L-lat: {sum_EOP_c_EOP_L_lat}")
print(f"Distance between EOP-c and EOP-R-lat: {sum_EOP_c_EOP_R_lat}")
print(f"Distance between EOP-c and EOP-L-latmed: {sum_EOP_c_EOP_L_latmed}")
print(f"Distance between EOP-c and EOP-R-latmed: {sum_EOP_c_EOP_R_latmed}")
print(f"Distance between EOP-c and EOP-L-latlat: {sum_EOP_c_EOP_L_latlat}")
print(f"Distance between EOP-c and EOP-R-latlat: {sum_EOP_c_EOP_R_latlat}")
print(f"Distance between L1-c and L1-L-med: {sum_L1_c_L1_L_med}")
print(f"Distance between L1-c and L1-R-med: {sum_L1_c_L1_R_med}")
print(f"Distance between L1-c and L1-L-lat: {sum_L1_c_L1_L_lat}")
print(f"Distance between L1-c and L1-R-lat: {sum_L1_c_L1_R_lat}")
print(f"Distance between L1-c and L1-L-latmed: {sum_L1_c_L1_L_latmed}")
print(f"Distance between L1-c and L1-R-latmed: {sum_L1_c_L1_R_latmed}")
print(f"Distance between L1-c and L1-L-latlat: {sum_L1_c_L1_L_latlat}")
print(f"Distance between L1-c and L1-R-latlat: {sum_L1_c_L1_R_latlat}")
print(f"Distance between L2-c and L2-L-med: {sum_L2_c_L2_L_med}")
print(f"Distance between L2-c and L2-R-med: {sum_L2_c_L2_R_med}")
print(f"Distance between L2-c and L2-L-lat: {sum_L2_c_L2_L_lat}")
print(f"Distance between L2-c and L2-R-lat: {sum_L2_c_L2_R_lat}")
print(f"Distance between L2-c and L2-L-latmed: {sum_L2_c_L2_L_latmed}")
print(f"Distance between L2-c and L2-R-latmed: {sum_L2_c_L2_R_latmed}")
print(f"Distance between L2-c and L2-L-latlat: {sum_L2_c_L2_L_latlat}")
print(f"Distance between L2-c and L2-R-latlat: {sum_L2_c_L2_R_latlat}")


print(distance_FL_c_FL_L_gon)
print(distance_FL_c_FL_R_gon)
print(sum_EOP_c_EOP_med)
print(sum_EOP_R_c_EOP_R_med)
print(sum_EOP_c_EOP_L_lat)
print(sum_EOP_c_EOP_R_lat)
print(sum_EOP_c_EOP_L_latmed)
print(sum_EOP_c_EOP_R_latmed)
print(sum_EOP_c_EOP_L_latlat)
print(sum_EOP_c_EOP_R_latlat)
print(sum_L1_c_L1_L_med)
print(sum_L1_c_L1_R_med)
print(sum_L1_c_L1_L_lat)
print(sum_L1_c_L1_R_lat)
print(sum_L1_c_L1_L_latmed)
print(sum_L1_c_L1_R_latmed)
print(sum_L1_c_L1_L_latlat)
print(sum_L1_c_L1_R_latlat)
print(sum_L2_c_L2_L_med)
print(sum_L2_c_L2_R_med)
print(sum_L2_c_L2_L_lat)
print(sum_L2_c_L2_R_lat)
print(sum_L2_c_L2_L_latmed)
print(sum_L2_c_L2_R_latmed)
print(sum_L2_c_L2_L_latlat)
print(sum_L2_c_L2_R_latlat)
