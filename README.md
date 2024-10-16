# Drawing Shapes in turtlesim

This ROS 2 package controls the turtle in turtlesim to draw a circle.

## Installation

1. Clone and Build the package:

    ```bash
    cd /path/to/ros2/workspace # replace with path to ros2 workspace directory
    git clone 
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
- turtlesim

Ensure that ROS 2 and turtlesim are installed on your machine.

