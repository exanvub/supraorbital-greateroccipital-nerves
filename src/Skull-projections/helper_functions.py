import os, re, numpy as np,json


def least_square_transform(A, B):
    '''
    Calculates the least-squares best-fit transform between corresponding 3D points A->B
    Input:
        A: Nx3 numpy array of corresponding 3D points
        B: Nx3 numpy array of corresponding 3D points
    Returns:
        T: 4x4 homogeneous transformation matrix
        R: 3x3 rotation matrix
        t: 3x1 column vector
    '''
        
    # Compute centroid for each pointcloud
    centroid_A = np.mean(A, axis=0)
    centroid_B = np.mean(B, axis=0)
    
    # Subtract centroid from pointclouds
    AA = A - centroid_A
    BB = B - centroid_B

    # Calculate h Matrix
    H = np.dot(AA.T, BB)
    
    # Perform SVD
    U, S, Vt = np.linalg.svd(H)
    
    # Calculate rotation from upper and lower matrixes
    R = np.dot(Vt.T, U.T)

    # Handle Reflections
    if np.linalg.det(R) < 0:
        Vt[2,:] *= -1
        R = np.dot(Vt.T, U.T)

    # Calculate translation
    t = centroid_B.T - np.dot(R, centroid_A.T)

    # homogeneous transformation
    T = np.identity(4)
    T[0:3, 0:3] = R
    T[0:3, 3] = t


    return T.tolist(), R.tolist(), t