# Maze

To launch the simulation:
```sh
roscd maze

roslaunch maze display_x.launch
```

# Gmapping
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