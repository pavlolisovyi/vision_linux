import numpy as np
import autocrop as crop
import label_image
import label_image_gender
import cv2


cap = cv2.VideoCapture(0)

while(True):
	ret, frame = cap.read()
	gray = cv2.cvtColor(frame, 1)
	cv2.imshow('Output Video', gray)
	if cv2.waitKey(1) & 0xFF == ord('p'):
		cv2.imwrite('cropped.jpg', frame)
		print('created new image')
		filename = 'cropped.jpg'
		img = cv2.imread(filename)
		gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

		gray = np.float32(gray)
		dst = cv2.cornerHarris(gray,2,3,0.04)

		#result is dilated for marking the corners, not important
		dst = cv2.dilate(dst,None)

		# Threshold for an optimal value, it may vary depending on the image.
		img[dst>0.01*dst.max()]=[0,0,255]

		cv2.imshow('dst',img)

		#Cropping
		initiate_label = crop.main()
		if initiate_label == 1:
			print("Tensorflow initiated")
		else:
			print("The Image is not initialized. Cannot proceed with tensorflow")
		label_image.main()
		label_image_gender.main()
		if cv2.waitKey(0) & 0xff == 5:
   			 cv2.destroyAllWindows()
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
cap.release()
cv2.destroyAllWindows()
