import cv2
from detection import preprocessImage
import numpy as np
cam_url = './demo/01 - Nen tham, duong thang.avi'
cap = cv2.VideoCapture(cam_url)
while(True):
  ret, frame = cap.read()
  cv2.imshow("frame",frame)
  preprocessImage(frame)
  if cv2.waitKey(1) & 0xFF == ord('q'):
    cv2.destroyAllWindows()
    break;