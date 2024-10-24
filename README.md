# Drawing Shapes in turtlesim

## Drawing a Circle Manually

1. Start a turtlesim node:

   ```bash
   ros2 run turtlesim turtlesim_node
   ```
   
![image](https://github.com/user-attachments/assets/274f676e-1268-42e7-b093-9bc86a069c82)
   
2. Run the following command in a new terminal:

    ```bash
    ros2 topic pub /turtle1/cmd_vel geometry_msgs/Twist "{linear: {x: 2.0, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 1.0}}"
    ```
![image](https://github.com/user-attachments/assets/acde34b6-ba82-4287-b67f-108d67bd17a5)

## Installing the Custom Package

This ROS 2 package controls the turtle in turtlesim to draw a circle automatically.

1. Clone and Build the package:

    ```bash
    cd /path/to/ros2/workspace # replace with path to ros2 workspace directory
    git clone https://github.com/AvinashCheeranjie/Drawing-Shapes-in-turtlesim.git
    colcon build
    source install/setup.bash
    ```
    
2. Start a turtlesim node:

   ```bash
   ros2 run turtlesim turtlesim_node
   ```   
   
3. Run the `draw_circle.py` script in a new terminal:

    ```bash
    ros2 run turtle_circle draw_circle
    ```

## Dependencies

- Linux
- [ROS 2]
  (https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debs.html)
- turtlesim

Ensure that ROS 2 and turtlesim are installed on your Linux machine.

