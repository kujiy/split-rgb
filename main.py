"""
Split RGB channel sample

Refer to Maximinusjoshus on https://medium.com/featurepreneur/understanding-the-concept-of-channels-in-an-image-6d59d4dafaa9
"""

if __name__ == '__main__':

    import cv2 as cv
    import numpy as np

    # read the image
    image = cv.imread("./chikuwa.png")
    # convert the image to RGB (images are read in BGR in OpenCV)
    image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
    # split the image into its three channels
    (R, G, B) = cv.split(image)
    # create named windows for each of the images we are going to display
    cv.namedWindow("Blue", cv.WINDOW_NORMAL)
    cv.namedWindow("Green", cv.WINDOW_NORMAL)
    cv.namedWindow("Red", cv.WINDOW_NORMAL)
    # display the images
    cv.imshow("Blue", B)
    cv.imshow("Green", G)
    cv.imshow("Red", R)
    # write the images to disk
    cv.imwrite("./channel_red.png", R)
    cv.imwrite("./channel_green.png", G)
    cv.imwrite("./channel_blue.png", B)


    """
    blend the images back
    """
    imageR = cv.imread("./channel_red.png", 0)
    imageG = cv.imread("./channel_green.png", 0)
    imageB = cv.imread("./channel_blue.png", 0)

    img = cv.merge((imageB, imageG, imageR))

    cv.imwrite('blended.png', img)

    # cv.imwrite("./channel_red_green_blue.jpg", dst)
    cv.namedWindow("RGB_blend", cv.WINDOW_NORMAL)
    cv.imshow('RGB_blend', img)

    if cv.waitKey(0):
        cv.destroyAllWindows()





