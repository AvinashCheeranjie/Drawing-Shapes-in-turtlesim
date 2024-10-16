# Drawing Shapes in turtlesim

This ROS 2 package controls the turtle in turtlesim to draw a circle.

## Installation

1. Build the package:

    ```bash
    cd ~/ros2_ws
    colcon build
    source install/setup.bash
    ```
    
2. Start a turtlesim node

   ```bash
   ros2 run turtlesim turtlesim_node
   ```   
   
3. Run the script in a new terminal:

    ```bash
    ros2 run turtle_circle draw_circle
    ```

## Dependencies

- ROS 2 (Foxy, Humble, or Rolling)
- Turtlesim

Ensure that ROS 2 and Turtlesim are installed on your machine.

