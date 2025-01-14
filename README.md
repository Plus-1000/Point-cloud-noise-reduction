# Point-cloud-noise-reduction
## 1. About this test: 
Normally, we use outlier removal methods for point cloud noise reduction. However, useful points may sometimes be removed because outliers are typically defined as points outside the range of their neighbors. For example, a point that appears distant from its neighbors. But, when we check the noisy points from a section view, the point could be close to the "middle face" of the point cloud. Its coordinate information is precious in surface reconstruction or face interpolation in the the future.

<p align="center">
<img src=https://github.com/Plus-1000/Point-cloud-noise-reduction/blob/main/pic/p1.jpg width="600" >
<b>
&nbsp;<br>
&nbsp;<br>

Duo to this situlation, this test aims to adjust outlier points (as seen from the section view) by compressing them toward the "middle face," effectively pressing the point cloud into a thin layer from both the positive and negative face vector directions.

<p align="center">
<img src=https://github.com/Plus-1000/Point-cloud-noise-reduction/blob/main/pic/p2.jpg width="600" >
<b>
&nbsp;<br>


## 2. How the calculation works: 
Few concepts need to be declear:

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

<p align="center">
<img src=https://github.com/Plus-1000/Point-cloud-noise-reduction/blob/main/pic/p4.jpg width="600" >
<b>
&nbsp;<br>

## 2. Check the result: 
We designed a face within NX CADCAM interface, create points on the face, we name these points as pts_ori.csv
<p align="center">
<img src=https://github.com/Plus-1000/Point-cloud-noise-reduction/blob/main/pic/p5.jpg width="600" >
<b>
&nbsp;<br>
<p align="center">
<img src=https://github.com/Plus-1000/Point-cloud-noise-reduction/blob/main/pic/p6.jpg width="600" >
<b>
&nbsp;<br>

Then we add noisy to pts_ori.csv, get the point set pts_noisy
<p align="center">
<img src=https://github.com/Plus-1000/Point-cloud-noise-reduction/blob/main/pic/p7.jpg width="600" >
<b>
&nbsp;<br>

We run Python script to process the noisy reduction, we get the result pts_after_noisy_reduction.csv, we dia a visual check from NX CADCAM interface. 
<p align="center">
<img src=https://github.com/Plus-1000/Point-cloud-noise-reduction/blob/main/pic/p8.jpg width="600" >
<b>
&nbsp;<br>

Our checking plan is: 
* Select an area from original points, we name the point set of this area as pts_ori_Large.csv,  then do a polynomial fitting and get the face formula. 
* We narrow down the point area above, and name the point set as pts_ori_small.csv, when we do a point to face distance check, any point from pts_ori_small.csv to the face formula should be 0, or lesser than 0.001 after consider the fitting error. 
* Same way, we define the checking point set pts_noisy_small.csv, pts_after_noisy_reduction_small.csv, we hope the averge distance from noisy reduction point set to face should be much smaller than that before noisy reduction.  


































