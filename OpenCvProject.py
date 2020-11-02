import cv2
import numpy as np
import VGG_test as vgg
face_cascade = cv2.CascadeClassifier('HaarCascades/haarcascade_frontalface_default.xml')

def strechContrast(img):
    xp = [0, 64, 128, 192, 255]
    fp = [0, 16, 128, 240, 255]
    x = np.arange(256)
    table = np.interp(x, xp, fp).astype('uint8')
    img = cv2.LUT(img, table)
    return img

def filter_card_image(img):
    stretchedImg = strechContrast(img)
    rotateImg = cv2.rotate(stretchedImg, cv2.ROTATE_90_COUNTERCLOCKWISE)
    resizedImg = cv2.resize(rotateImg, (400, 400))

    contrastedImg = cv2.convertScaleAbs(resizedImg, alpha=1.4, beta=0)
    smoothedImg = cv2.GaussianBlur(contrastedImg, (3, 3), 0)
    cv2.medianBlur(smoothedImg,3,smoothedImg)
    cv2.imshow("Filtred", smoothedImg)
    return smoothedImg


def extract_face_card_image(face_cascade,img,filename):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)

    faces = face_cascade.detectMultiScale(gray, 2, 5)
    for (x, y, w, h) in faces:
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_face = img[y:y + h, x:x + w]
        cv2.imshow("Haar_cascade"+filename, img)
        cv2.imshow('Roi'+filename, roi_face)
        cv2.imwrite(filename+'.jpg', roi_face)
        return roi_face


def extract_face_cv_image(face_cascade,img,filename):

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)
    #cv2.imshow('qqRoi' + filename, gray)

    faces = face_cascade.detectMultiScale(gray, 2, 5)
    for (x, y, w, h) in faces:
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_face = img[y:y + h, x:x + w]
        cv2.imshow("Haar_cascade"+filename, img)
        cv2.imshow('Roi'+filename, roi_face)
        cv2.imwrite(filename+'.jpg', roi_face)
        return roi_face


#img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
#cv2.imshow("thresh",thresh)


"""
#detected_face = detect_face(faces,img)
#detected_face_test = detect_face(faces2,img2)
"""

"""
orb = cv2.ORB_create()
kp1_, des1 = orb.detectAndCompute(detected_face,None)
kp2_, des2 = orb.detectAndCompute(detected_face_test,None)
bf= cv2.BFMatcher(cv2.NORM_HAMMING,crossCheck=True)
matches = bf.match(des1,des2)

matchesSorted = sorted(matches,key=lambda x:x.distance)
img3 =cv2.drawMatches(detected_face,kp1_,detected_face_test,kp2_,matchesSorted[:10],None, flags=2)
for m in matchesSorted:
    print(m.distance)

"""

#cv2.imshow('detected_face_test',detected_face_test)
#cv2.imshow('detected_face_test99',img3)

#cv2.imshow('img',img)

def main():
    img = cv2.imread('ImagesPermis/permis.jpg')
    img2 = cv2.imread('outail.jpg')

    cv2.imshow("cv_ Original", img2)
    cv2.imshow("permis_Original", img)

    img= filter_card_image(img)

    permis_roi=extract_face_card_image(face_cascade,img,"permis_roi")
    cv_roi = extract_face_cv_image(face_cascade, img2, "cv_roi")


    vgg.verifyFace(permis_roi, cv_roi, distance_de_similarite=0.40)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
