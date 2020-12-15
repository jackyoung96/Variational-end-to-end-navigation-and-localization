# Variational-end-to-end-navigation-and-localization

Personal implementation of variational end to end navigation and localization paper

## Original paper

> Amini, Alexander, et al. "Variational end-to-end navigation and localization." 2019 International Conference on Robotics and Automation (ICRA). IEEE, 2019.
> [paperlink](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=8793579)

## Making dataset from Carla environment

you can find codes in carla_code folder  

+ end2end_map.py : get simple topological map (Coarse Grained map) from carla based on location. Data will be published with ROS topic.
  
+ end_to_end.py : get camera image data from carla. You can achieve data with autopilot function(Alt+P). Data will be published with ROS topic.
  
+ topic_saver.py : Subscribing image and topological map topic and save.
  
You should modify path which will contain images.
  
**Sample videos are like below.**
  
[![carla_get_data](https://www.youtube.com/watch?v=lvRUbiX5r1U&feature=youtu.be.jpg)](https://youtu.be/lvRUbiX5r1U?t=0s) 
  
## Training with dataset

You can find codes in training_code folder. Codes are based on jupyter notebook and Pytorch
  
+ end2end_training_v2.ipynb : Training part. All the model structures are built based on original paper.
  
+ make_dataset_v2.ipynb : Making dataset into pickle. It makes easy to training in Pytorch
  
+ path_projection_v2.ipynb : For visualizing generated path into camera image. You can modify code depends on your vehicles height and FOV(field of view) of front camera.
  
You should modify path whiche will contain dataset of something else.

## Result

Actually result is not good. The reason I assume is lack of dataset. Anyway the result is like below.  
