import os
from  ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import SetEnvironmentVariable
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument
from launch.conditions import IfCondition
from launch.actions import (DeclareLaunchArgument, GroupAction,
                            IncludeLaunchDescription, SetEnvironmentVariable)
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():

    rm_eco65_gazebo_up = IncludeLaunchDescription(
            PythonLaunchDescriptionSource(os.path.join(get_package_share_directory(('rm_gazebo')),'launch', 'gazebo_eco65_6fb_demo.launch.py'))
    )

    rm_eco65_gazebo_moveit = IncludeLaunchDescription(
            PythonLaunchDescriptionSource(os.path.join(get_package_share_directory(('rm_eco65_config')),'launch', 'gazebo_moveit_demo_6fb.launch.py'))
    )

    return LaunchDescription([
    rm_eco65_gazebo_up,
    rm_eco65_gazebo_moveit
    ])