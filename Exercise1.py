import numpy as np

theta1 = np.radians(90)
theta2 = np.radians(45)

# Rotation matrix around y-axis
R_y = np.array([[np.cos(theta1), 0, np.sin(theta1)],
              [0, 1, 0],
              [-np.sin(theta1), 0, np.cos(theta1)]])

# Rotation matrix around z-axis
R_z = np.array([[np.cos(theta2), -np.sin(theta2), 0],
              [np.sin(theta2), np.cos(theta2), 0],
              [0, 0, 1]])

result = np.dot(R_y,R_z)
print(R_y)
print(R_z)
print(result)
