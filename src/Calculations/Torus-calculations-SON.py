import json
import numpy as np


# Load JSON data from file
with open('/Users/nicolas/Library/CloudStorage/OneDrive-VrijeUniversiteitBrussel/Onderzoek/n supraorbi occipitalis major/Torus-data/197-SON.mrk.json', 'r') as file:
    data = json.load(file)

# Extract markups data
markups_data = data['markups'][0]['controlPoints']

# Create variables for each label with the corresponding position
for markup in markups_data:
    label = markup['label']
    position = markup['position']
    
    # Create variables dynamically as NumPy arrays
    globals()[label.replace('-', '_')] = np.array(position)

# Print all labels and their positions
for markup in markups_data:
    label = markup['label']
    variable_name = label.replace('-', '_')
    position = globals().get(variable_name)

    if position is not None:
        print(f"Position of {label}: {position}")
    else:
        print(f"Variable {variable_name} not defined.")

# # Calculate Euclidean distance between SON-C, SON-CL, and SON-Lnotch
# distance = np.linalg.norm(SON_C - SON_CL) + np.linalg.norm(SON_CL - SON_Lnotch)
# print(f"Euclidean distance between SON-C, SON-CL, and SON-Lnotch: {distance}")

# # Calculate Euclidean distance between SON-C, SON-CR, and SON-Rnotch
# distance = np.linalg.norm(SON_C - SON_CR) + np.linalg.norm(SON_CR - SON_Rnotch)
# print(f"Euclidean distance between SON-C, SON-CR, and SON-Rnotch: {distance}")

# # Calculate Euclidean distance between SON-C1, SON-C1L, and SON-MedL
# distance = np.linalg.norm(SON_C1 - SON_C1L) + np.linalg.norm(SON_C1L - SON_MedL)
# print(f"Euclidean distance between SON-C1, SON-C1L, and SON-MedL: {distance}")

# # Calculate Euclidean distance between SON-C1, SON-C1R, and SON-MedR
# distance = np.linalg.norm(SON_C1 - SON_C1R) + np.linalg.norm(SON_C1R - SON_MedR)
# print(f"Euclidean distance between SON-C1, SON-C1R, and SON-MedR: {distance}")

# # Calculate Euclidean distance between SON-C1, SON-C1L, and SON-INTL
# distance = np.linalg.norm(SON_C1 - SON_C1L) + np.linalg.norm(SON_C1L - SON_INTL)
# print(f"Euclidean distance between SON-C1, SON-C1L, and SON-INTL: {distance}")

# # Calculate Euclidean distance between SON-C1, SON-C1R, and SON-INTR
# distance = np.linalg.norm(SON_C1 - SON_C1R) + np.linalg.norm(SON_C1R - SON_INTR)
# print(f"Euclidean distance between SON-C1, SON-C1R, and SON-INTR: {distance}")
        
# # Calculate Euclidean distance between SON-C2, SON-C2L, and SON-LatL
# distance = np.linalg.norm(SON_C2 - SON_C2L) + np.linalg.norm(SON_C2L - SON_LatL)
# print(f"Euclidean distance between SON-C2, SON-C2L, and SON-LatL: {distance}")
        
# # Calculate Euclidean distance between SON-C2, SON-C2R, and SON-LatR
# distance = np.linalg.norm(SON_C2 - SON_C2R) + np.linalg.norm(SON_C2R - SON_LatR)
# print(f"Euclidean distance between SON-C2, SON-C2R, and SON-LatR: {distance}")
        

# # Calculate Euclidean distance between SON-C2, SON-C2L, and SON-MedL2
# distance = np.linalg.norm(SON_C2 - SON_C2L) + np.linalg.norm(SON_C2L - SON_MedL2)
# print(f"Euclidean distance between SON-C2, SON-C2L, and SON-MedL2: {distance}")

# # Calculate Euclidean distance between SON-C2, SON-C2R, and SON-MedR2
# distance = np.linalg.norm(SON_C2 - SON_C2R) + np.linalg.norm(SON_C2R - SON_MedR2)
# print(f"Euclidean distance between SON-C2, SON-C2R, and SON-MedR2: {distance}")

# # Calculate Euclidean distance between SON-C2, SON-C2L, and SON-INTL2
# distance = np.linalg.norm(SON_C2 - SON_C2L) + np.linalg.norm(SON_C2L - SON_INTL2)
# print(f"Euclidean distance between SON-C2, SON-C2L, and SON-INTL2: {distance}")

# # Calculate Euclidean distance between SON-C2, SON-C2R, and SON-INTR2
# distance = np.linalg.norm(SON_C2 - SON_C2R) + np.linalg.norm(SON_C2R - SON_INTR2)
# print(f"Euclidean distance between SON-C2, SON-C2R, and SON-INTR2: {distance}")

# # Calculate Euclidean distance between SON-C2, SON-C2L, and SON-LatL2
# distance = np.linalg.norm(SON_C2 - SON_C2L) + np.linalg.norm(SON_C2L - SON_LatL2)
# print(f"Euclidean distance between SON-C2, SON-C2L, and SON-LatL2: {distance}")

# # Calculate Euclidean distance between SON-C2, SON-C2R, and SON-LatR2
# distance = np.linalg.norm(SON_C2 - SON_C2R) + np.linalg.norm(SON_C2R - SON_LatR2)
# print(f"Euclidean distance between SON-C2, SON-C2R, and SON-LatR2: {distance}")











# Calculate Euclidean distance between SON-C, SON-CL, and SON-Lnotch
distance = np.linalg.norm(SON_C - SON_CL) + np.linalg.norm(SON_CL - SON_Lnotch)
print(f"{distance}")

# Calculate Euclidean distance between SON-C, SON-CR, and SON-Rnotch
distance = np.linalg.norm(SON_C - SON_CR) + np.linalg.norm(SON_CR - SON_Rnotch)
print(f"{distance}")

# Calculate Euclidean distance between SON-C1, SON-C1L, and SON-MedL
distance = np.linalg.norm(SON_C1 - SON_C1L) + np.linalg.norm(SON_C1L - SON_MedL)
print(f"{distance}")

# Calculate Euclidean distance between SON-C1, SON-C1R, and SON-MedR
distance = np.linalg.norm(SON_C1 - SON_C1R) + np.linalg.norm(SON_C1R - SON_MedR)
print(f"{distance}")

# Calculate Euclidean distance between SON-C1, SON-C1L, and SON-INTL
distance = np.linalg.norm(SON_C1 - SON_C1L) + np.linalg.norm(SON_C1L - SON_INTL)
print(f"{distance}")

# Calculate Euclidean distance between SON-C1, SON-C1R, and SON-INTR
distance = np.linalg.norm(SON_C1 - SON_C1R) + np.linalg.norm(SON_C1R - SON_INTR)
print(f"{distance}")
        
# Calculate Euclidean distance between SON-C2, SON-C2L, and SON-LatL
distance = np.linalg.norm(SON_C2 - SON_C2L) + np.linalg.norm(SON_C2L - SON_LatL)
print(f"{distance}")

# Calculate Euclidean distance between SON-C2, SON-C2R, and SON-LatR
distance = np.linalg.norm(SON_C2 - SON_C2R) + np.linalg.norm(SON_C2R - SON_LatR)
print(f"{distance}")


# Calculate Euclidean distance between SON-C2, SON-C2L, and SON-MedL2
distance = np.linalg.norm(SON_C2 - SON_C2L) + np.linalg.norm(SON_C2L - SON_MedL2)
print(f"{distance}")

# Calculate Euclidean distance between SON-C2, SON-C2R, and SON-MedR2
distance = np.linalg.norm(SON_C2 - SON_C2R) + np.linalg.norm(SON_C2R - SON_MedR2)
print(f"{distance}")

# Calculate Euclidean distance between SON-C2, SON-C2L, and SON-INTL2
distance = np.linalg.norm(SON_C2 - SON_C2L) + np.linalg.norm(SON_C2L - SON_INTL2)
print(f"{distance}")

# Calculate Euclidean distance between SON-C2, SON-C2R, and SON-INTR2
distance = np.linalg.norm(SON_C2 - SON_C2R) + np.linalg.norm(SON_C2R - SON_INTR2)
print(f"{distance}")

# Calculate Euclidean distance between SON-C2, SON-C2L, and SON-LatL2
distance = np.linalg.norm(SON_C2 - SON_C2L) + np.linalg.norm(SON_C2L - SON_LatL2)
print(f"{distance}")

# Calculate Euclidean distance between SON-C2, SON-C2R, and SON-LatR2
distance = np.linalg.norm(SON_C2 - SON_C2R) + np.linalg.norm(SON_C2R - SON_LatR2)
print(f"{distance}")
