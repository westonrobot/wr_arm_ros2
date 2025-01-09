import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node
from launch.substitutions import Command, FindExecutable, LaunchConfiguration

import xacro

def generate_launch_description():
    # 声明参数 link7_type
    declare_link7_type_arg = DeclareLaunchArgument(
        'link7_type',
        default_value='Link7_6f',
        description='Type of link7'
    )
    realman_xacro_file = os.path.join(get_package_share_directory('rm_description'), 'urdf',
                                        'rm_75.urdf.xacro')
    robot_description = Command(
        [FindExecutable(name='xacro'), ' ', realman_xacro_file, ' ','link7_type:=', LaunchConfiguration('link7_type')])

    return LaunchDescription([
            Node(
                package='robot_state_publisher',
                executable='robot_state_publisher',
                name='robot_state_publisher',
                respawn=True,
                parameters=[{'robot_description': robot_description}],
                output='screen'
            )
        ])
