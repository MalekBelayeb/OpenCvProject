import cv2
import pytesseract







def compare(str_taken,str_original):
    score = 0
    total = len(str_original)
    for w in str_taken:
        if w in str_original:
            score +=1

    print((score/total)*100)
    return str(round((score/total)*100,2))

def ExecuteDiplomaProcess():

    img2 = cv2.imread('Uploads/diplome1.jpg')
    img2= cv2.resize(img2, (600, 700))

    img3 = cv2.imread('Uploads/diplome.jpg')
    img3= cv2.resize(img3, (600, 700))

    cv2.imshow('img2', img2)
    cv2.imshow('img3', img3)

    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    str2 = pytesseract.image_to_string(img2)
    str3 = pytesseract.image_to_string(img3)

    str2 = str2.replace("\n", " ")
    str3 = str3.replace("\n", " ")
    print(str3.split())

    if len(str2.split()) <20:
        return "IMG_NOT_CLEAR"
    else:
        return compare(str2.split(),str3.split())


def main():

    print(ExecuteDiplomaProcess())
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()