# Point-cloud-noise-reduction
## 1. About this test: 
Normally, we use outlier removal methods for point cloud noise reduction. However, useful points may sometimes be removed because outliers are typically defined as points that fall outside the range of their neighbors—for example, a point that appears distant from its surrounding neighbors. However, when we examine the noisy points in a sectional view, such a point might actually be close to the "middle face" of the point cloud. Its coordinate information is valuable for surface reconstruction or face interpolation at a later stage.

<p align="center">
<img src=https://github.com/Plus-1000/Point-cloud-noise-reduction/blob/main/pic/p1.jpg width="600" >
<b>
&nbsp;<br>
&nbsp;<br>

Due to this situation, this test aims to adjust outlier points (as observed in the section view) by compressing them toward the 'middle face,' effectively flattening the point cloud into a thin layer from both the positive and negative face vector directions.

<p align="center">
<img src=https://github.com/Plus-1000/Point-cloud-noise-reduction/blob/main/pic/p2.jpg width="600" >
<b>
&nbsp;<br>


## 2. How the calculation works: 
Few elements introduced before proceed.

Refering to a current-point i (as a point from the point cloud):  
* Point-normal: the normal vector at the current-point i, representing the local surface orientation.
* Neighbour-points: the points within the radius of the point i
* Average-position: the centroid of the neighboring-points.
* Direction: the vector from the neighbour-points centroid to the current-point.
* Correction: a vector used to adjust the position of the current-point i, aligned with the point-normal.
* New-points[i]: the updated position of the current-point after applying the correction.

<p align="center">
<img src=https://github.com/Plus-1000/Point-cloud-noise-reduction/blob/main/pic/p3.jpg width="600" >
<b>
&nbsp;<br>
  
The calculation details include: 
* Finds neighboring points within a specified radius.
* Skips the point if it has fewer than 2 neighbors.
* Computes the average position of the neighboring points.
* Calculates the direction from the current point to the average position.
* Projects this direction onto the point's normal to compute a correction vector.
* Adjusts the point's position using the correction vector to smooth the surface.
  
<p align="center">
<img src=https://github.com/Plus-1000/Point-cloud-noise-reduction/blob/main/pic/p4.jpg width="1280" >
<b>
&nbsp;<br>


## 3. Prepare point sets and test noise reduction scrips: 
We designed a face within NX CADCAM interface, create points on the face, we name these points as pts_ori.csv
<p align="center">
<img src=https://github.com/Plus-1000/Point-cloud-noise-reduction/blob/main/pic/p5.jpg width="600" >
<b>
&nbsp;<br>
<p align="center">
<img src=https://github.com/Plus-1000/Point-cloud-noise-reduction/blob/main/pic/p6.jpg width="600" >
<b>
&nbsp;<br>

Then we add noisy to pts_ori.csv, get the point set pts_noisy.
<p align="center">
<img src=https://github.com/Plus-1000/Point-cloud-noise-reduction/blob/main/pic/p7.jpg width="600" >
<b>
&nbsp;<br>

We run point_cloud_noise_reduction.py with pts_noisy.csv as the input, and the result is saved as pts_after_noisy_reduction.csv.
<p align="center">
<img src=https://github.com/Plus-1000/Point-cloud-noise-reduction/blob/main/pic/p8.jpg width="600" >
<b>
&nbsp;<br>

## 4. Check the result: 
Our checking plan is: 
* Select an area from original points, we name the point set of this area as pts_ori_Large.csv,  then do a polynomial fitting and get the face formula.

<p align="center">
<img src=https://github.com/Plus-1000/Point-cloud-noise-reduction/blob/main/pic/p9.jpg width="1280" >
<b>
&nbsp;<br>
&nbsp;<br>
  
* After run the distance check scrips fit_check.py, we get distance from the point set to the fitted face. For simplicity, we use the Z-direction distance to represent the point-to-face distance, which ideally should be measured along the face normal, as our face approximately lies in the XY plane."

<p align="center">
<img src=https://github.com/Plus-1000/Point-cloud-noise-reduction/blob/main/pic/p10.jpg width="1280" >
<b>
&nbsp;<br>
&nbsp;<br>

<p align="center">
<img src=https://github.com/Plus-1000/Point-cloud-noise-reduction/blob/main/pic/p9a.jpg width="600" >
<b>
&nbsp;<br>
&nbsp;<br>
<p align="center">
<img src=https://github.com/Plus-1000/Point-cloud-noise-reduction/blob/main/pic/p9b.jpg width="600" >
<b>
&nbsp;<br>
&nbsp;<br>


## 5. The conculations: 
We designed a face within NX CADCAM interface, create points on the face, we name these points as pts_ori.csv






























