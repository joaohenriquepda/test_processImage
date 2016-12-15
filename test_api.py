# - *- coding: utf- 8 - *-
# import the necessary packages
import requests
import cv2
import urllib
import time
import numpy as np

# define the URL to our face detection API
url = "http://localhost:8000/face_detection/detect/"

# use our face detection API to find faces in images via image URL
#image = urllib.urlopen("")

#image = urllib.urlopen("https://scontent-gru2-1.xx.fbcdn.net/v/t1.0-9/1071_428356690554276_2078489730_n.jpg?oh=085d79a7dba9969471b0e158bd63af91&oe=58F729BF")
#image1 = urllib.urlopen("https://scontent-gru2-1.xx.fbcdn.net/v/t1.0-9/10154374_887236344701678_2835358613574848918_n.jpg?oh=1dc31d79b8eb6e1a37b7d1461e94552e&oe=58B2E94D")
#image2 = urllib.urlretrieve("https://scontent-gru2-1.xx.fbcdn.net/v/t1.0-9/r270/12115481_972095072848255_4032544286627409172_n.jpg?oh=b9faa0642d0584e9e24180c06c5563fe&oe=58B192D7", "image2.jpg")
#image3 = urllib.urlopen("https://scontent-gru2-1.xx.fbcdn.net/v/t1.0-9/12299367_748838145220475_529083328194189411_n.jpg?oh=a68f94b6c023d52bd1f56835ce13256d&oe=58B1C857")

# output = open("image.jpg","wb")
# output.write(image.read())
# output.close()
#a
# output = open("image1.jpg","wb")
# output.write(image1.read())
# output.close()
#
# output = open("image3.jpg","wb")
# output.write(image3.read())
# output.close()




image = cv2.imread("image.jpg")
payload = {"image": open("image.jpg", "rb")}

print payload

r = requests.post(url, files=payload).json()
print r["num_faces"]

# loop over the faces and draw them on the image
for (startX, startY, endX, endY) in r["faces"]:
    cv2.rectangle(image, (startX, startY), (endX, endY), (0, 255, 0), 2)

# # show the output image
cv2.imshow("image.jpg", image)


lap = cv2.Laplacian(image, cv2.CV_64F)
lap = np.uint8(np.absolute(lap))
cv2.imshow(" Laplacian" , lap)






print ""
print u"Próxima imagem".encode('utf-8')
print ""
#time.sleep(5)


image1 = cv2.imread("image1.jpg")
payload = {"image": open("image1.jpg", "rb")}
r = requests.post(url, files=payload).json()


# loop over the faces and draw them on the image
for (startX, startY, endX, endY) in r["faces"]:
	cv2.rectangle(image1, (startX, startY), (endX, endY), (0, 250, 0), 2)

# show the output image
cv2.imshow("image1.jpg", image1)





image2 = cv2.imread("image2.jpg")
payload = {"image": open("image2.jpg", "rb")}
r = requests.post(url, files=payload).json()

# loop over the faces and draw them on the image
for (startX, startY, endX, endY) in r["faces"]:
	cv2.rectangle(image2, (startX, startY), (endX, endY), (0, 250, 0), 2)

# show the output image
cv2.imshow("image2.jpg", image2)




image3 = cv2.imread("image3.jpg")
payload = {"image": open("image3.jpg", "rb")}
r = requests.post(url, files=payload).json()

# loop over the faces and draw them on the image
for (startX, startY, endX, endY) in r["faces"]:
	cv2.rectangle(image3, (startX, startY), (endX, endY), (0, 250, 0), 2)

# show the output image
cv2.imshow("image3.jpg", image3)



#cv2.waitKey(0)

# load our image and now use the face detection API to find faces in
# images by uploading an image directly
#image = cv2.imread("adrian.jpg")
#payload = {"image": open("adrian.jpg", "rb")}
# r = requests.post(url, files=payload).json()
# print "adrian.jpg: {}".format(r)
#
# # loop over the faces and draw them on the image
# for (startX, startY, endX, endY) in r["faces"]:
# 	cv2.rectangle(image, (startX, startY), (endX, endY), (0, 255, 0), 2)

# show the output image
#cv2.imshow("adrian.jpg", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
