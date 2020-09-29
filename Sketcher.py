import matplotlib.image as img
import matplotlib.pyplot as plt
import cv2


def show_image(img):
    plt.imshow(img, cmap='gray')
    plt.show()


orig = img.imread("img.jpg")
# show_image(orig)
grayScaled = cv2.cvtColor(orig, cv2.COLOR_BGR2GRAY)
# show_image(grayScaled)
inverted = cv2.bitwise_not(grayScaled)
# show_image(inverted)
blurred = cv2.GaussianBlur(inverted, (23, 23), sigmaX=20, sigmaY=20)
# show_image(blurred)
finalResult = cv2.divide(grayScaled, 255 - blurred, scale=256)
# show_image(finalResult)
plt.imsave('FinalResult.png', finalResult, cmap='gray', vmin=0, vmax=255)
