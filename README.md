# Point-cloud-noise-reduction
Normally, we use outlier removal methods for point cloud noise reduction. However, the useful points may be removed because outliers are typically defined as points outside their neighbors' range, for example, this point is along from its neighbors and could be removed with outlier removal algorithms, but from the section view, is located close to "middle face" of the point cloud, the coordinate info of this point is important for rebuilding surface or doing face interpolation lately. 



This test will try to move the outlier point (from section view), and compress them toward the "middle face", likely to press the point cloud to a thin layer from both position and negative face vector. 
