import cv2

face_cascade = cv2.CascadeClassifier('HaarCascades/haarcascade_frontalface_default.xml')

face_cv_list = []

def extract_face_cv_image(face_cascade,img,filename):

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)

    faces = face_cascade.detectMultiScale(gray, 2, 5)
    for (x, y, w, h) in faces:
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_face = img[y:y + h, x:x + w]
        face_cv_list.append(roi_face)


def getFaceFromCV():
    img2 = cv2.imread('ImagesCV/outail_cvv.png')
    extract_face_cv_image(face_cascade, img2, "cv_roi")
    cv2.imshow('Original CV', img2)
    if len(face_cv_list) >0:
        return max(face_cv_list, key=lambda face: face.shape[0]*face.shape[1])
    else:
        return None



def main():
    print(getFaceFromCV())

    # filterAndExtractInfo(v)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()