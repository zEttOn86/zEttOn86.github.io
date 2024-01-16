import os
import argparse
import cv2
import numpy as np
import scipy.io as sio
from math import cos, sin

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--datasets_root',
                        help='Path to the root directory of AFLW2000 datasets',
                        type=str)
    parser.add_argument('--filename',
                        help='Filename without extension to load the data',
                        type=str)
    args = parser.parse_args()
    return args


def get_R(x,y,z):
    ''' Get rotation matrix from three rotation angles (radians). right-handed.
    Args:
        angles: [3,]. x, y, z angles
    Returns:
        R: [3, 3]. rotation matrix.
    '''
    # x
    Rx = np.array([[1, 0, 0],
                   [0, np.cos(x), -np.sin(x)],
                   [0, np.sin(x), np.cos(x)]])
    # y
    Ry = np.array([[np.cos(y), 0, np.sin(y)],
                   [0, 1, 0],
                   [-np.sin(y), 0, np.cos(y)]])
    # z
    Rz = np.array([[np.cos(z), -np.sin(z), 0],
                   [np.sin(z), np.cos(z), 0],
                   [0, 0, 1]])

    R = Rx.dot(Ry.dot(Rz))
    return R


if __name__ == "__main__":
    args = parse_args()

    image_file = os.path.join(args.datasets_root, '{}.jpg'.format(args.filename))
    mat_file = os.path.join(args.datasets_root, '{}.mat'.format(args.filename))

    # Load .jpg
    img = cv2.imread(image_file)
    # Load .mat
    mat = sio.loadmat(mat_file)

    # [pitch yaw roll tdx tdy tdz scale_factor]
    pre_pose_params = mat['Pose_Para'][0]
    # Get [pitch, yaw, roll]
    pitch, yaw, roll = pre_pose_params[:3]

    # Covert to R
    x = pitch
    y = -yaw
    z = roll
    R = get_R(x, y, z)
    print("Rotation matrix:\n", R)

    # Draw Axis
    cx = img.shape[1]//2
    cy = img.shape[0]//2
    size = 100
    # X-axis pointing to right. drawn in red
    x1 = size * R[0, 0] + cx
    y1 = size * R[1, 0] + cy
    # Y-axis drawn in green
    x2 = size * R[0, 1] + cx
    y2 = size * R[1, 1] + cy
    # Z-axis (out of the screen) drawn in blue
    x3 = size * R[0, 2] + cx
    y3 = size * R[1, 2] + cy

    cv2.line(img, (int(cx), int(cy)), (int(x1),int(y1)), (0,0,255), 2)
    cv2.line(img, (int(cx), int(cy)), (int(x2),int(y2)), (0,255,0), 2)
    cv2.line(img, (int(cx), int(cy)), (int(x3),int(y3)), (255,0,0), 2)

    cv2.imshow("View", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print("End")