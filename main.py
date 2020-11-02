import cv2
import VGG_test as vgg
import ExtractInfoFromCard as InfoCard
import ExtractInfoFromCV as InfoCV

def main():

    cardFace=InfoCard.getFaceFromCard()
    cvFace=InfoCV.getFaceFromCV()
    cv2.imshow("cvFace", cvFace)
    cv2.imshow("cardFace", cardFace)
    vgg.verifyFace(cardFace, cvFace, distance_de_similarite=0.40)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()