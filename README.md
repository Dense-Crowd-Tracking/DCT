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
