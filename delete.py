from enum import Enum
class Finger(Enum):
  INDEX_LEFT = 1
  MIDDLE_LEFT = 2
  RING_LEFT = 3
  PINKY_LEFT = 4
  INDEX_RIGHT = 5
  MIDDLE_RIGHT = 6
  RING_RIGHT = 7
  PINKY_RIGHT = 8

finger_map = {
	Finger.PINKY_LEFT: [0, 1, 2, 3, 26, 27, 52, 53, 74, 75],
	Finger.RING_LEFT: [4, 5, 28, 29, 54, 55, 76, 77],
	Finger.MIDDLE_LEFT: [6, 7, 30, 31, 56, 57],
	Finger.INDEX_LEFT: [8, 9, 10, 11, 32, 33, 34, 35, 58, 59, 60, 61, 78, 79, 80, 81, 82, 83],
	Finger.INDEX_RIGHT: [12, 13, 14, 15, 36, 37, 38, 39, 62, 63, 64, 65, 84, 85, 86, 87],
	Finger.MIDDLE_RIGHT: [16, 17, 40, 41, 66, 67, 88, 89],
	Finger.RING_RIGHT: [18, 19, 42, 43, 44, 45, 68, 69, 90, 91],
	Finger.PINKY_RIGHT: [20, 21, 22, 23, 24, 25, 46, 47, 48, 49, 50, 51, 70, 71, 72, 73, 92, 93]
}

# invert the finger_map
finger_map = {key: [k for k, v in finger_map.items() if key in v][0] for key in range(94)}
print(finger_map)
