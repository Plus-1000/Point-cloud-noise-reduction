# tested on 2025 Jan 02

import open3d as o3d
import numpy as np
import pandas as pd
import sys
import os
import time
curr_path = os.getcwd() + '\\'

# Smooth the point cloud along point normal
def smooth_along_normals(pcd, radius_normal, smoothing_factor, iterations):
    points = np.asarray(pcd.points) # Converts the point_cloud points to a NumPy array.
    normals = np.asarray(pcd.normals) # Converts the point_cloud normals to a NumPy array.
    kdtree = o3d.geometry.KDTreeFlann(pcd) # Creates a KD-tree for fast nearest-neighbor searches.
    # print('iterations:  ', iterations)
    
    for _ in range(iterations):
        new_points = np.copy(points)
        
        for i in range(points.shape[0]): # rows of data, the counts of points
            [_, idx, _] = kdtree.search_radius_vector_3d(points[i], radius_normal) #Finds all points within a specified radius.
            
            if len(idx) < 2: # if this point's neighbour poins count is lesser than 2, go to next point
                continue
            neighbors = points[idx[1:]]  # Exclude the point itself
          
            average_position = np.mean(neighbors, axis=0) # Computes the average position of the neighboring points
            
            direction = points[i] - average_position # direction is the vector that from current point to the average position of its neighbors.
            
            # correction, projecting the direction onto point normal 
            correction = smoothing_factor * np.dot(direction, normals[i]) * normals[i]
            
            new_points[i] = points[i] - correction  # move point from its original position to corrected position
    
        
        points = new_points
        pcd.points = o3d.utility.Vector3dVector(points)
    return pcd.points

if __name__=='__main__':
    start=time.time()
   
    # ---------Load pt cloud------------
    file_name='pts_noisy.csv'
    df = pd.read_csv(curr_path + '\\pts\\' + file_name)
    points = df.values

    # ---------Creates an empty Open3D point cloud object----------.
    pcd = o3d.geometry.PointCloud() 
    pcd.points = o3d.utility.Vector3dVector(points) 

    # -------parameters------------
    radius_ = 3.0 # radius used for normal estimation, adjust based on point cloud scale (1.5 is fine)
    max_n=30   # maximum number of nearest neighbors (max_nn=20)
    smoothing_factor = 0.2  # a scaling factor that controls the amount of smoothing, adjust based on noise level
    iterations = 10 # The number of times the smoothing process is repeated.

    # ------Estimates the normals for each point in the point cloud using a hybrid search parameter---------
    pcd.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=radius_, max_nn=max_n))
    
    # ---------Removes statistical outliers from the point cloud, based on neighbors and standard deviation--------
    # pcd, ind = pcd.remove_statistical_outlier(nb_neighbors=max_n, std_ratio=radius_)
    
    # -------noise reduction along point normal and distance to face (pts group center)-----------
    pts=smooth_along_normals(pcd, radius_, smoothing_factor, iterations) # call func

    # ---------Save the smoothed point cloud to CSV----------
    smoothed_points = np.asarray(pts)
    output_path = curr_path + '\\pts\\' +  'pts_after_noise_reduction.csv'
    np.savetxt(output_path, smoothed_points, delimiter=',')

    end = time.time()
    print('Noise reduction takes '+(str(round((end - start),1))+' seconds'))