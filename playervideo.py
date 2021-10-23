import cv2
import numpy as np
import Encryption_Decryption 
from PIL import Image

capture = cv2.VideoCapture("output.mp4")
frame_width = int(capture.get(3))
fps = capture.get(cv2.CAP_PROP_FPS)      # OpenCV2 version 2 used "CV_CAP_PROP_FPS"
frame_count = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))
duration = frame_count/fps
count = 0
size = (300, 300)
result = cv2.VideoWriter('filename.avi', 
                         cv2.VideoWriter_fourcc(*'XVID'),
                         fps, size)
if capture.isOpened() == False:
	print("error")
while capture.isOpened():
	ret,frame = capture.read()
	#print(frame.shape)
	if ret:
		#cv2.imwrite('image_decryption/' + str(c) + '.jpg', frame)
		frame = Encryption_Decryption.HenonEncryption(300,frame,True,(0.1,0.1))
		#print(frame)
		count+=1
		print(count,frame_count)
		frame = np.array(frame)
		result.write(frame)
		#print(frame.shape)
		#cv2.imshow("frame",frame)
		if cv2.waitKey(25) & 0xFF == ord('q'):
			break
	else:
		break
capture.release()
result.release()

cv2.destroyAllWindows()
print("The video was successfully saved")
