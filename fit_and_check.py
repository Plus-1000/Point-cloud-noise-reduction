import numpy as np
import os
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Function to fit polynomial surface and return formula
def polynomial_fit(data, degree):
    # Extract x, y, z
    x = data[:, 0]
    y = data[:, 1]
    z = data[:, 2]
    
    # Prepare design matrix for 2D polynomial fitting
    X = np.vstack([x**i * y**j for i in range(degree + 1) for j in range(degree + 1 - i)]).T
    
    # Solve for coefficients using least squares
    coeffs, *_ = np.linalg.lstsq(X, z, rcond=None)
    
    # Build the formula as a string
    terms = [f"{coeff:.3f} * x**{i} * y**{j}" for (coeff, (i, j)) in zip(coeffs, [(i, j) for i in range(degree + 1) for j in range(degree + 1 - i)])]
    formula = " + ".join(terms)
    return formula, coeffs

# Function to calculate the distance between a point and the fitted surface
def one_pt_to_face_dist(x, y, z1, coeffs, degree):
    # Evaluate the polynomial surface at (x, y)
    z_face = sum(coeff * (x**i) * (y**j) for (coeff, (i, j)) in zip(coeffs, [(i, j) for i in range(degree + 1) for j in range(degree + 1 - i)]))
    
    # Calculate the distance
    distance = abs(z1 - z_face)
    return distance


def avg_dist(data, data_new, degree):
    dist_list=[]
    ddist=0
    _, coeffs = polynomial_fit(data, degree)  # Get coefficients for the fitted polynomial

    for i in range(len(data_new)):
        x = data_new[i, 0]
        y = data_new[i, 1]
        z = data_new[i, 2]
        dist = one_pt_to_face_dist(x, y, z, coeffs, degree)
        # print(f"Point {i}: ({x}, {y}, {z}) -> Distance: {dist}")
        dist_list.append(dist)
        ddist=ddist+abs(dist)
    avg_dist=ddist/(len(data_new))
    return avg_dist

# Function to evaluate the polynomial surface on a grid
def evaluate_polynomial_surface(x_grid, y_grid, coeffs, degree):
    z_grid = np.zeros_like(x_grid)
    for (coeff, (i, j)) in zip(coeffs, [(i, j) for i in range(degree + 1) for j in range(degree + 1 - i)]):
        z_grid += coeff * (x_grid**i) * (y_grid**j)
    return z_grid

# ------------Create a grid for plotting the polynomial surface---------
def grid_set(data,degree): # x,y,z grid for plot
    _, coeffs = polynomial_fit(data, degree)
    x_min, x_max = data[:, 0].min(), data[:, 0].max()
    y_min, y_max = data[:, 1].min(), data[:, 1].max()
    x_grid, y_grid = np.meshgrid(np.linspace(x_min, x_max, 100), np.linspace(y_min, y_max, 100))
    z_grid = evaluate_polynomial_surface(x_grid, y_grid, coeffs, degree)
    return x_grid, y_grid, z_grid

if __name__=='__main__': 
    curr_path = os.getcwd()
    degree = 3 # Use the same degree as in the polynomial fit
    data = np.loadtxt(os.path.join(curr_path, 'pts', 'pts_ori_fit.csv'), delimiter=",")
      
    #-----------------
    file_name='pts_ori_check.csv'
    data_new = np.loadtxt(os.path.join(curr_path, 'pts', file_name), delimiter=",")
    dist1=avg_dist(data, data_new, degree)
    print('avg dist of '+ file_name[0:-4]+' is:' +str(dist1))
    data_new1=data_new
    
    #----------------
    file_name='pts_noisy_check.csv'
    data_new = np.loadtxt(os.path.join(curr_path, 'pts', file_name), delimiter=",")
    dist2=avg_dist(data, data_new, degree)
    print('avg dist of '+ file_name[0:-4]+' is:' +str(dist2))
    data_new2=data_new
    
    #---------------
    file_name='pts_after_noise_reduction_check.csv'
    data_new = np.loadtxt(os.path.join(curr_path, 'pts', file_name), delimiter=",")
    dist3=avg_dist(data, data_new, degree)
    print('avg dist of '+ file_name[0:-4]+' is:' +str(dist3))
    data_new3=data_new
    
    # Fit polynomials for degrees 1 through 30 and save formulas
    output_file = "fitted_formulas.txt"
    with open(os.path.join(curr_path, 'pts', output_file), "w") as file:
        formula, coeffs = polynomial_fit(data, degree)
        file.write(f"{degree} degree formula:\n")
        file.write(f"{formula}")
    
    print(f"Formulas saved to {output_file}")
        
# Plot the polynomial surface, original points, and denoised points
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
x_grid, y_grid, z_grid=grid_set(data,degree)

# ------Plot the polynomial surface-----
ax.plot_surface(x_grid, y_grid, z_grid, color='blue', alpha=0.2, label=str(degree)+' degree polynomial fitted area')

# ------Plot the original points-------
# ax.scatter(data[:, 0], data[:, 1], data[:, 2], color='grey', s=20, label='Original Points (small_polyfit_face)')

# Plot the denoised points
ax.scatter(data_new1[:, 0], data_new1[:, 1], data_new1[:, 2], color='red', 
           s=10, label='original Points,avg dist to face='+str(round(dist1, 4)))

# Plot the denoised points
ax.scatter(data_new2[:, 0], data_new2[:, 1], data_new2[:, 2], color='green', 
           s=10, label='noised Points, avg dist to face='+str(round(dist2, 4)))

# Plot the denoised points
ax.scatter(data_new3[:, 0], data_new3[:, 1], data_new3[:, 2], color='cyan', 
           s=10, label='Denoised Points, avg dist to face='+str(round(dist3, 4)))

# Add labels and legend
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_zlim(68, 73)
ax.legend()

plt.title('Original Pts and its grid face, Noisy points, Denoised Points')
plt.show()