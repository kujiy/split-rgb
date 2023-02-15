

# Press the green button in the gutter to run the script.
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
    cv.imwrite("./channel_red.jpg", R)
    cv.imwrite("./channel_green.jpg", G)
    cv.imwrite("./channel_blue.jpg", B)
    if cv.waitKey(0):
        cv.destroyAllWindows()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/