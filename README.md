# Point-cloud-noise-reduction
## 1. About this test: 
Normally, we use outlier removal methods for point cloud noise reduction. However, useful points may sometimes be removed because outliers are typically defined as points outside the range of their neighbors. For example, a point that appears distant from its neighbors might be removed by outlier removal algorithms. However, from a sectional view, this point could actually be close to the "middle face" of the point cloud. The coordinate information of such a point is crucial for surface reconstruction or face interpolation later.



This test aims to adjust outlier points (as seen from the sectional view) by compressing them toward the "middle face," effectively pressing the point cloud into a thin layer from both the positive and negative face vectors.
