import cv2
import VGG_test as vgg
import ExtractInfoFromCard as InfoCard
import ExtractInfoFromCV as InfoCV

def ExecuteProcess():

    cardFace=InfoCard.getFaceFromCard()
    cvFace=InfoCV.getFaceFromCV()

    if(cardFace == None):

        print("no face detected on idcard")
        return "NO_CARD_FACE"
    else:
        return vgg.verifyFace(cardFace, cvFace, distance_de_similarite=0.40)

    """
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    """


if __name__ == '__main__':
    ExecuteProcess()