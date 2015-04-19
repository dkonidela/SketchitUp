from flask import Flask, render_template, request, url_for, json
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2

width=1000
height=1000

app=Flask(__name__)


@app.route('/home')
def home():
	print "Rendering"
	return render_template('home.html')

@app.route('/intro')
def intro():
	print "Inside Intro"
	return render_template('intro.html')


@app.route('/hello', methods	=['GET', 'POST'])
def login():
	if request.method == "POST":
		print "POST Request Successful"
		name=request.form['fname']
		request.files['file'].save('file.png')
		points=processImage()
		#width, height= points.shape
		print "returned"
		#data=json.dumps(points)
		#data=json.dumps(points)
		#data=map(json.dumps, points)
		return render_template('canvas.html',points=points,row = row, col = col,width=width,height=height)
	
def processImage():
	global row
	global col
	print "processImage method"

	'''img = cv2.imread('/Users/KonidelaDileep/Documents/FlaskApps/app/file.jpg')
	cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
	kernel = np.ones((5,5),np.float32)/25
	dst=cv2.filter2D(img,-1,kernel)

	# edge detection using Canny Edge Detection
	edges1 = cv2.Canny(dst,10,200)

	# image thresholding
	th2 = cv2.adaptiveThreshold(edges1,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
	cv2.THRESH_BINARY,11,2)
	ret,thresh2 = cv2.threshold(th2,127,255,cv2.THRESH_BINARY)

	# blurring the image
	blur2 = cv2.blur(thresh2,(5,5))

	# display the Plot
	plt.subplot(121),plt.imshow(img,'gray'),plt.title('Original')
	plt.xticks([]), plt.yticks([])
	plt.subplot(122),plt.imshow(blur2,'gray'),plt.title('Averaging')
	plt.xticks([]), plt.yticks([])
	'''


	lowThreshold = 0
	max_lowThreshold = 100
	ratio = 3
	kernel_size = 3
	global width
	global height

	img = cv2.imread('/Users/KonidelaDileep/Documents/FlaskApps/app/file.png')
	height,width,depth= img.shape
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

	detected_edges=cv2.GaussianBlur(gray,(3,3),0)
	#detected_edges = cv2.Canny(detected_edges,lowThreshold,lowThreshold*ratio,apertureSize = kernel_size)
	#dst = cv2.bitwise_and(img,img,mask = detected_edges)

	kernel = np.ones((5,5),np.float32)/25
	dst=cv2.filter2D(detected_edges,-1,kernel)

	# edge detection using Canny Edge Detection
	edges1 = cv2.Canny(dst,75,125)

	# image thresholding
	#th2 = cv2.adaptiveThreshold(edges1,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
	#cv2.THRESH_BINARY,11,2)
	ret,thresh2 = cv2.threshold(edges1,127,255,cv2.THRESH_BINARY_INV)

	# blurring the image
	#blur2 = cv2.blur(thresh2,(5,5))
	#print thresh2
	#plt.imshow(thresh2,'gray')
	#plt.show()
	#print np.array(thresh2)
	#print thresh2[10][2]
	#list=thresh2.tolist()
	#print list
	#row,  col=thresh2.shape

	# mainlist=[[]]
	# list1=[]
	# for i in range(0,row):
	# 	for j in range(0,col):
	# 		list1.append(thresh2[i][j])
	# 	mainlist.append(list1)

	# #print mainlist

	row, col=thresh2.shape
	points=[]

	#print thresh2[10][10]
	#print thresh2[100][101]


	for i in range(0,row):
		#localPoint=[]
		for j in range(0,col):
			if thresh2[i][j]==255:
				points.append(1)
			elif thresh2[i][j]==0:
				points.append(0)
		#points.append(localPoint)

	#print points

	#mainlist=thresh2.tolist()
	return points


if __name__=='__main__':
	app.run(debug=True)
