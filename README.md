# Point-cloud-noise-reduction
## 1. About this test: 
Normally, we use outlier removal methods for point cloud noise reduction. However, useful points may sometimes be removed because outliers are typically defined as points outside the range of their neighbors. For example, a point that appears distant from its neighbors. But, when we check the noisy points from a sectional view, the point could be close to the "middle face" of the point cloud. Its coordinate information is precious in surface reconstruction or face interpolation in the the future.

<p align="center">
<img src=https://github.com/Plus-1000/Point-cloud-noise-reduction/blob/main/pic/outlier1.jpg width="600" >
<img src=https://github.com/Plus-1000/Point-cloud-noise-reduction/blob/main/pic/outlier2.jpg width="600" >
<b>


This test aims to adjust outlier points (as seen from the sectional view) by compressing them toward the "middle face," effectively pressing the point cloud into a thin layer from both the positive and negative face vector directions.

<p align="center">

<img src=https://github.com/Plus-1000/Point-cloud-noise-reduction/blob/main/pic/outlier3.jpg width="600" >
<b>

