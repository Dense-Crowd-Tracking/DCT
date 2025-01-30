# DCT
Dense crowd tracking

## Datasets
5 dataset on human head with bounding box annotations

1. Data_S-HEAD
2. Head Detection (CCTV)
3. Human head detection OpenVM + C270
4. JHU-CROWD++
5. SCUT-HEAD
### Training Process
- first attempt with jhu-crowd++ on yolov10
- second attempt with all 5 datasets merged on yolov10

## Detectors
- yolo models trained on jhu-crowd++
find the model [here](https://www.kaggle.com/models/faihajalamtopu/yolov8n_jhu_crowd/) at kaggle.
- yolov10 from scratch and pretrained with jhu-crowd++
find the model [here](https://www.kaggle.com/models/faihajalamtopu/yolov10_jhucrowd/) at kaggle.
### possible modifications
#### Architecture:

##### Input: 
1024×1024 frame → Split into 256×256 overlapping tiles.

##### Preprocessing:

###### FFT High-Pass Filter: Enhances edges of small heads in low-resolution regions.

###### Circular Hough Attention Layer: Highlights regions with arc-like contours (head candidates).

##### Backbone:

###### Hierarchical Dilated Convolution Blocks:

Layer 1: Dilation rate=2 (captures head edges).

Layer 2: Dilation rate=4 (groups nearby heads).

###### Adaptive Anchors: 3 anchor sizes (4px, 8px, 12px) dynamically assigned via density heatmap.

##### Head:

###### Multi-Spectral Classification: Uses RGB + frequency domain features to separate heads from noise.


