import matplotlib.image as img
import matplotlib.pyplot as plt
import cv2
import argparse


def show_image(img):
    plt.imshow(img, cmap='gray')
    plt.show()


parser = argparse.ArgumentParser("Sketcher")
parser.add_argument("InputImage", help="Output image name.")
parser.add_argument("-o", help="Output image name.", default='final.jpg')
args = parser.parse_args()
params = vars(args)

orig = img.imread(params.get('InputImage'))
# show_image(orig)
grayScaled = cv2.cvtColor(orig, cv2.COLOR_BGR2GRAY)
# show_image(grayScaled)
inverted = cv2.bitwise_not(grayScaled)
# show_image(inverted)
blurred = cv2.GaussianBlur(inverted, (23, 23), sigmaX=20, sigmaY=20)
# show_image(blurred)
finalResult = cv2.divide(grayScaled, 255 - blurred, scale=256)
# show_image(finalResult)
plt.imsave(params.get('o'), finalResult, cmap='gray', vmin=0, vmax=255)
