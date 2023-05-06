# python-Image-to-Cartoon

In my Python project, I created a program that converts a regular image into a cartoon-style image using advanced image processing techniques. The program uses the OpenCV library to apply various transformations on the input image.

The program starts by loading the input image using the ```cv2.imread()``` function. The loaded image is in the BGR color format, so we need to convert it to a grayscale image using the ```cv2.cvtColor()``` function.

Next, I applied a blur effect on the grayscale image using the ```cv2.medianBlur()``` function. This helps to remove noise from the image and smooth out any sharp edges.

After that, I applied adaptive thresholding on the blurred image using the ```cv2.adaptiveThreshold()``` function. This function converts the grayscale image into a binary image by thresholding the pixels based on their local neighborhood. The threshold value is determined dynamically for each pixel based on the mean of its local neighborhood.

Then, I applied a bilateral filter on the original color image using the ```cv2.bilateralFilter()``` function. This filter helps to smooth out the image while preserving the edges.

Finally, I combined the edge and color images using the bitwise AND operation ```(cv2.bitwise_and())``` to create the final cartoon-style image.

To see the results, I displayed the original image, the edge-detected image, and the final cartoon-style image using the ```cv2.imshow()``` function. I used ```cv2.waitKey(0)``` to wait for a key press and then used cv2.destroyAllWindows() to close all open windows.

Overall, this Python program is a fun and creative way to transform any image into a cartoon-style image using advanced image processing techniques. The program can be used by artists, designers, or anyone who wants to create unique and eye-catching images.

# Example

![06 05 2023_14 13 16_REC](https://user-images.githubusercontent.com/61588132/236615093-deb26e25-d803-498a-9e5d-723d963b6410.png)
