"""This script uses the real ROS rosbag module to generate test bags."""
import sys
# Thanks, PyCharm
sys.path.append("/opt/ros/melodic/lib/python2.7/dist-packages/")

import rosbag

from geometry_msgs.msg import Pose, PoseStamped, Transform, TransformStamped, Twist, TwistStamped
from sensor_msgs.msg import CameraInfo, Image, Imu, PointCloud2
from tf.msg import tfMessage


def generate_geometry_msgs_bag(bag):
    pose = Pose()
    pose.position.x = 1
    pose.position.y = 2
    pose.position.z = 3
    pose.orientation.x = 1
    pose.orientation.y = 2
    pose.orientation.z = 3
    pose.orientation.w = 4
    bag.write("Pose", pose)

    pose_stamped = PoseStamped()
    pose_stamped.header.stamp.secs = 1234
    pose_stamped.header.stamp.nsecs = 5678
    pose_stamped.header.frame_id = "frame"
    pose_stamped.pose = pose
    bag.write("PoseStamped", pose_stamped)

    transform = Transform()
    transform.translation.x = 1
    transform.translation.y = 2
    transform.translation.z = 3
    transform.rotation.x = 1
    transform.rotation.y = 2
    transform.rotation.z = 3
    transform.rotation.w = 4
    bag.write("Transform", transform)

    transform_stamped = TransformStamped()
    transform_stamped.header = pose_stamped.header
    transform_stamped.transform = transform
    bag.write("TransformStamped", transform_stamped)


def main():
    with rosbag.Bag('geometry_msgs.bag', 'w') as bag:
        generate_geometry_msgs_bag(bag)


if __name__ == '__main__':
    main()