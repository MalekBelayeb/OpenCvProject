import cv2
import pytesseract

#v = cv2.imread('ImagesPermis/akthem_permis.png')
#v = cv2.imread('ImagesPermis/permis.jpg')
#v = cv2.imread('ImagesPermis/outail_permis.png')
#v = cv2.imread('ImagesPermis/hamza_permis.png')
#v = cv2.imread('ImagesPermis/emir_permis.jpg')
#v = cv2.imread('ImagesPermis/oumaima_permis.jpg')

v = cv2.imread('Uploads/permis.PNG')


face_cascade = cv2.CascadeClassifier('HaarCascades/haarcascade_frontalface_default.xml')
face_list = []

def getPossibleFace(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:

        img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_face = img[y:y + h, x:x + w]
        face_list.append(roi_face)

def filterAndExtractFace(v):

    v = cv2.resize(v, (600, 700))
    v = cv2.rotate(v, cv2.ROTATE_90_COUNTERCLOCKWISE)

    s = cv2.cvtColor(v, cv2.COLOR_BGR2GRAY)
    s = cv2.equalizeHist(s)
    s = cv2.GaussianBlur(s, (1, 1), 3)
    s = cv2.medianBlur(s, 5)

    s = cv2.Laplacian(s, cv2.CV_8U, ksize=3)
    cv2.imshow('laplacian', s)
    s = cv2.convertScaleAbs(s)

    im2, contours, hierarchy = cv2.findContours(s, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = sorted(contours, key=cv2.contourArea, reverse=True)[:5]

    x_count = 0
    for c in cnts:
        x, y, w, h = cv2.boundingRect(cnts[x_count])
        ROI = v[y:y + h, x:x + w]
        ROI = cv2.convertScaleAbs(ROI, alpha=1.1, beta=0)
        x_count += 1
        getPossibleFace(ROI)


def getFaceFromCard():
    filterAndExtractFace(v)
    #cv2.imshow('Original Permis', v)

    if len(face_list) >0:
        return max(face_list, key=lambda face: face.shape[0]*face.shape[1])
    else:
        return None


def main():
    print(getFaceFromCard())
    #filterAndExtractInfo()
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
