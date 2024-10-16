# Drawing Shapes in turtlesim

This ROS 2 package controls the turtle in turtlesim to draw a circle.

## Drawing the Circle Manually

1. Start a turtlesim node:

   ```bash
   ros2 run turtlesim turtlesim_node
   ```   
   
2. Run the following command in a new terminal:

    ```bash
    ros2 topic pub /turtle1/cmd_vel geometry_msgs/Twist "{linear: {x: 2.0, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 1.0}}"
    ```
![Screenshot 2024-10-15 202110](https://github.com/user-attachments/assets/b5cc9fa0-7a52-46f7-9d6b-07f6f3d2f624)

## Installation


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
   
3. Run the script in a new terminal:

    ```bash
    ros2 run turtle_circle draw_circle
    ```

## Dependencies

- Linux
- ROS 2 (Foxy, Humble, or Rolling) 
- turtlesim

Ensure that ROS 2 and turtlesim are installed on your machine.

