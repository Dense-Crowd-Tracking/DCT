# DCT
Dense crowd tracking

## [Tracking Pedestrian Heads in Dense Crowd](https://openaccess.thecvf.com/content/CVPR2021/html/Sundararaman_Tracking_Pedestrian_Heads_in_Dense_Crowd_CVPR_2021_paper.html?ref=https://githubhelp.com)
- Used dataset: [Crowd of Heads Dataset(CroHD)](https://motchallenge.net/data/Head_Tracking_21/)
- model: 


## From Docs:
22 Nov 2023
ODD: Avro
EVEN: topu
____________________________________________________________________________________
Crowd Evacuation in Hajj Stoning Area: Planning through Modeling and Simulation 
____________________________________________________________________________________
Homography based multiple camera detection and tracking of people in a dense crowd
Floor Fields for Tracking in High Density Crowd Scenes
Fusing Crowd Density Maps and Visual Object Trackers for People Tracking in Crowd Scenes  
An Intelligent IoT Approach for Analyzing and Managing Crowds
Tracking in a Dense Crowd Using Multiple Cameras
Tracking Pedestrian Heads in Dense Crowd
Link through it:
https://project.inria.fr/crowdscience/category/publications/


 LC-Net: Localized Counting Network for Extremely Dense Crowds

 LC-Net: Localized Counting Network for Extremely Dense Crowds
Other networks can count people in a crowd but can not provide information of a person's position in a crowd. Very little research proposes some networks to solve the problem use Dense-Net, VGG-16 which require high computational resources that's possible in real-time estimation. In the paper, it proposes Localised Counting Network(LC-Net) with two parts: backbone network and head network. In the backbone network part, they take image input and summarise features. This part can localise a person accurately. In the head network part, they try to know the deep down feature by applying dilation without reducing resolution. Sometimes data preprocessing is required to get better results from the LC-net model. They claim real-time crowd counting and try to establish their claim with a real-life experiment with their designed client-server model.  

LCDnet: a lightweight crowd density estimation model for real‑time
video surveillance




Blog
https://medium.com/nanonets/dense-and-sparse-crowd-counting-methods-and-techniques-a-review-bae04fdbf062
https://www.crcv.ucf.edu/research/projects/counting-in-extremely-dense-crowd-images/



Dataset
https://paperswithcode.com/datasets?task=crowd-counting

https://www.kaggle.com/datasets/danaelisanicolas/high-density-crowd-counting    (4-year ago)

https://github.com/VisDrone/DroneRGBT


Model : 
C-3 framework (https://github.com/gjy3035/C-3-Framework)


An Intelligent IoT Approach for Analyzing and Managing Crowds
Data is collected via RFID sensors, cameras and environmental sensors. Then DNs that are distributed over paths receive that information. Then it calculates risk factors depending on the classification of the paths, congestion level, and pilgrims’ condition. The paths are classified into different priorities based on the distance from key services as lesser distance often means more congestion. Congestion level is classified based on crowd intensity and once it exceeds the threshold system initiates congestion-avoidance approach. Pilgrims are classified into groups based on medical condition, age and gender. DNs find directions locally and can also communicate with other DNs for the computation and also report the congestion to the cloud. Cloud can access all DNs and can find the evacuation paths globally. It then can communicate with authorities and lcd screens whenever congestion is detected and can also update DNs. The Monitoring module collects data then the Simulation and Routing module calculate some factors and predict movement, load and impact. The risk factors calculated by DNs depend on pilgrims and paths. DNs calculate the optimal routes to all possible destinations by calculating the next hop, expected time for reaching it and its state. Next the module calculates the congestion factors for all nearby paths and if the congestion level is higher than the threshold, alternative evacuation paths are determined. The module also reports congestion to the predecessor paths to perform rerouting and to avoid congestion. The Guidance module using the information collected by the DNs updates the routes to all possible destinations. From the experiments it is to note that critical congestion decreases by considering environmental conditions and the number of injuries depends on pilgrims' health conditions.


Tracking Pedestrian Heads in Dense Crowd
