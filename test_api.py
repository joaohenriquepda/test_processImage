# import the necessary packages
import requests
import cv2
import urllib
import time

# define the URL to our face detection API
url = "http://localhost:8000/face_detection/detect/"

# use our face detection API to find faces in images via image URL
#image = urllib.urlretrieve("http://dicasboaspracachorro.com.br/wp-content/uploads/2014/06/hotel-para-cachorro.jpeg", "obama.jpg")
#image = urllib.urlopen("")
image1 = urllib.urlopen("https://scontent-gru2-1.xx.fbcdn.net/v/t1.0-9/10154374_887236344701678_2835358613574848918_n.jpg?oh=1dc31d79b8eb6e1a37b7d1461e94552e&oe=58B2E94D")
image = urllib.urlopen("https://scontent-gru2-1.xx.fbcdn.net/v/t1.0-9/1071_428356690554276_2078489730_n.jpg?oh=085d79a7dba9969471b0e158bd63af91&oe=58F729BF")


#https://scontent-gru2-1.xx.fbcdn.net/v/t1.0-9/1071_428356690554276_2078489730_n.jpg?oh=085d79a7dba9969471b0e158bd63af91&oe=58F729BF

output = open("image.jpg","wb")
output.write(image.read())
output.close()

image = cv2.imread("image.jpg")
payload = {"image": open("image.jpg", "rb")}

print payload

r = requests.post(url, files=payload).json()

# loop over the faces and draw them on the image
for (startX, startY, endX, endY) in r["faces"]:
    cv2.rectangle(image, (startX, startY), (endX, endY), (0, 255, 0), 2)

# # show the output image
cv2.imshow("image.jpg", image)

print "esperar"
time.sleep(10)


output = open("image1.jpg","wb")
output.write(image1.read())
output.close()
image1 = cv2.imread("image1.jpg")
pay = {"image1": open("image1.jpg", "rb")}

print pay
url = "http://localhost:8000/face_detection/detect/"

r1 = requests.post(url, files=pay).json()
print r1


# loop over the faces and draw them on the image
for (startX1, startY1, endX1, endY1) in r1["faces"]:
    cv2.rectangle(image1, (startX1, startY1), (endX1, endY1), (0, 250, 0), 2)

# # show the output image
cv2.imshow("image1.jpg", image1)

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
