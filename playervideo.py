import cv2
import numpy as np
import Encryption_Decryption 
from PIL import Image

capture = cv2.VideoCapture("output.mp4")
frame_width = int(capture.get(3))

size = (frame_width, frame_width)
result = cv2.VideoWriter('filename.mp4', 
                         cv2.VideoWriter_fourcc(*'MP4V'),
                         10, size)
if capture.isOpened() == False:
	print("error")
while capture.isOpened():
	ret,frame = capture.read()
	#print(frame.shape)
	if ret:
		#cv2.imwrite('image_decryption/' + str(c) + '.jpg', frame)
		frame = Encryption_Decryption.HenonEncryption(frame.shape[0],frame,True,(0.1,0.1))
		#print(frame)
		frame = np.array(frame)
		result.write(frame)
		#print(frame.shape)
		cv2.imshow("frame",frame)
		if cv2.waitKey(25) & 0xFF == ord('q'):
			break
	else:
		break
capture.release()
result.release()

cv2.destroyAllWindows()
print("The video was successfully saved")
