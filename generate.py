from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os
open('test.txt','w').close()
open('training.txt','w').close()
fp = open('training.txt', 'a')
size=50,50
for num in range(10):
	for filename in os.listdir(r"./train/"+str(num)):
		libsvm_format=''
		libsvm_format=libsvm_format+str(num)
		im=Image.open("./train/"+str(num)+'/'+filename)
		im.thumbnail(size) #size=>50,50
		#im = im.convert('L') #gray image
		#print im.getpixel((1,1))
		
		#plt.figure("dog")
		#plt.imshow(im)
		#plt.show()
		width,height=im.size
		for i in range(height):
			x_cnt=0
			for j in range(width):
				if im.getpixel((i,j))[2] <150:
					x_cnt+=1
			libsvm_format=libsvm_format+' '+str(i+1)+':'+str(x_cnt)
		for i in range(width):
			y_cnt=0
			for j in range(height):
				if im.getpixel((i,j))[2] <150:
					y_cnt+=1
			libsvm_format=libsvm_format+' '+str(i+height+1)+':'+str(y_cnt)
		libsvm_format=libsvm_format+'\n'
		print filename+'  completed!'
		fp.write(libsvm_format)
fp.close()
fp = open('test.txt', 'a')
for num in range(10):
	for filename in os.listdir(r"./test/"+str(num)):
		libsvm_format=''
		libsvm_format=libsvm_format+str(num)
		im=Image.open("./test/"+str(num)+'/'+filename)
		im.thumbnail(size) #size=>50,50
		#im = im.convert('L') #gray image
		width,height=im.size
		for i in range(height):
			x_cnt=0
			for j in range(width):
				if im.getpixel((i,j))[2] <150:
					x_cnt+=1
			libsvm_format=libsvm_format+' '+str(i+1)+':'+str(x_cnt)
		for i in range(width):
			y_cnt=0
			for j in range(height):
				if im.getpixel((i,j))[2] <150:
					y_cnt+=1
			libsvm_format=libsvm_format+' '+str(i+height+1)+':'+str(y_cnt)
		libsvm_format=libsvm_format+'\n'
		print filename+'  completed!'
		fp.write(libsvm_format)
fp.close()

