import numpy as np 
import cv2
import sys

def CatVideo():
	cv2.namedWindow("shibie")
	#1调用摄像头
	cap=cv2.VideoCapture(0)
	#2人脸识别器分类器
	classfier=cv2.CascadeClassifier("Train.xml")
	color=(0,255,0)
	while cap.isOpened():
		ok,frame=cap.read()
		if not ok:
			break
		#2灰度转换
		grey=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
		#人脸检测，1.2和2分别为图片缩放比例和需要检测的有效点数
		faceRects = classfier.detectMultiScale(grey, scaleFactor = 1.2, minNeighbors = 3, minSize = (32, 32))
		if len(faceRects) > 0:            #大于0则检测到人脸      
			print("测试1")                             
			for faceRect in faceRects:  #单独框出每一张人脸
				print(faceRect)
				x, y, w, h = faceRect        
				cv2.rectangle(frame, (x - 10, y - 10), (x + w + 10, y + h + 10), color, 3)
		cv2.imshow("shibie",frame)
		print("ceshi2")
		if cv2.waitKey(10)&0xFF==ord('q'):
			break

	cap.release()
	cv2.destroyAllWindows()



CatVideo()