from importRosbag.importRosbag import importRosbag
import numpy as np


def test_pose_stamped():
    bag = importRosbag("geometry_msgs.bag")
    poses = bag["PoseStamped"]
    assert np.allclose(poses["ts"], 1234 + 5678e-9)
    assert np.all(poses["point"] == [(1, 2, 3)])
    assert np.all(poses["rotation"] == [(4, 1, 2, 3)])


def test_transform():
    bag = importRosbag("geometry_msgs.bag")
    transforms = bag["Transform"]
    assert np.all(transforms["point"] == [(1, 2, 3)])
    assert np.all(transforms["rotation"] == [(4, 1, 2, 3)])


def test_transform_stamped():
    bag = importRosbag("geometry_msgs.bag")
    transforms = bag["TransformStamped"]
    assert np.allclose(transforms["ts"], 1234 + 5678e-9)
    # TODO: why is this broken?
    assert np.all(transforms["point"] == [(1, 2, 3)])
    assert np.all(transforms["rotation"] == [(4, 1, 2, 3)])
