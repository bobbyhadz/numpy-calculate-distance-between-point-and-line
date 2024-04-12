# NumPy: Calculate the distance between a Point and a Line

import numpy as np

p1 = np.array([0, 0])
p2 = np.array([20, 20])
p3 = np.array([10, 14])


distance = np.cross(p2 - p1, p3 - p1) / np.linalg.norm(p2 - p1)

print(distance)  # 👉️ 2.82842712474619
