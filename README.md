# Maze Runner
In this project we have implemented a robot with the capability to escape from a Maze.

## Visualize URDF structure
This create a my_robot.pdf in the current folder.
```sh
roscd maze
sudo apt install liburdfdom-tools
rosrun xacro xacro urdf/my_robot_x.xacro --inorder > urdf/my_robot_x.urdf
urdf_to_graphiz urdf/my_robot_x.urdf
```
## Visualize transformation tree
After run the system, this command create a frames.pdf file in the current folder.
```sh
rosrun tf view_frames
```

## Run Simualtion
To launch the simulation:
```sh
roslaunch maze display_x.launch
```

## Run Gmapping
Install package:
```sh
sudo apt install ros-melodic-gmapping
```
Launch Gmapping
```sh
roslaunch maze gmapping.launch
```
After launched gmapping, to show in rviz the map scanned, go in rviz:
Add - Map - /map in topic space

