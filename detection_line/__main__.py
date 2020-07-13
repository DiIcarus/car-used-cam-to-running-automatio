import cv2
from detection import preprocessImage
import numpy as np

cam_url = 'demo/04 - Nen go, duong cong, nhieu.avi'
cap = cv2.VideoCapture(cam_url)
while(True):
  ret, frame = cap.read()
  cv2.imshow("frame",frame)
  preim = preprocessImage(frame)
  if preim is None:
    print(preim)
  else:
    cv2.imshow("crop",preim)
  if cv2.waitKey(1) & 0xFF == ord('q'):
    cv2.destroyAllWindows()
    break;