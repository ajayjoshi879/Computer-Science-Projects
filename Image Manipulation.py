'''This module contains three image processing functions: a deuteranopic function,
a grayscale function, and a green screening function. Deuteranopic changes the red and green
values of each pixel in an image. Gray scale converts an image into black and white format.
Green screening creates a pictures of a person added to a new background.

One difficulty encountered with green screening was that light patches on a person's face
may sometimes be identified as a background pixel because of its intensity and become replaced. 

To solve this problem, an if statement would be useful. For example, if pixel is identified
as background pixel, check the 50 pixels left and right of the pixel, and if more than half
of them are not background pixels, then don't replace the pixel in question with a pixel
from the background image. 

This will ensure that only light patches within large areas of light patches are replaced
by pixels from the given background image and avoid certain pixels within the person's image
being replaced by background image pixels. 

If the pixel testes is on the edge of a person, it will not be replaced, which is what we want,
as theoretically only half of its surrounding pixels left / right should be background pixels
(whereas more than half is the requirement for a pixel to be replaced).

'''

import cImage
from cImage import *
import math
import os
import os.path

def pixelMapper(oldImage, rgbFunction):
    '''Referenced from Miller & Ranum textbook. This function provides a generalized method to
    iterate over each pixel in a picture and perform some function onto each pixel.
    '''
    
    width = oldImage.getWidth()
    height = oldImage.getHeight()
    newIm = EmptyImage(width, height)
    
    for row in range(height):
        for col in range(width):
            originalPixel = oldImage.getPixel(col, row)
            newPixel = rgbFunction(originalPixel)   #calling whichever function we wish
                                                    #to perform on the pixel
            newIm.setPixel(col, row, newPixel)
    
    return newIm


def deuteranopicPixel(oldPixel):
    '''Gets the rgb values of an original pixel, finds the average of the red and
    green values, and creates a new pixel in the format: Pixel(redGreenAverage,
    redGreenAverage, originalBlue) to achieve a deuteranopic effect.
    '''
    
    red = oldPixel.getRed()
    green = oldPixel.getGreen()
    blue = oldPixel.getBlue()
    newRedGreen = int((red + green) / 2)   #since rgb values must be integers.
    newPixel = Pixel(newRedGreen, newRedGreen, blue)
    
    return newPixel
    
def deuteranopic(oldImage):
    '''Returns a new image where the new image is a deuteranopic version of the oldImage given
    '''  
      
    newImage = pixelMapper(oldImage, deuteranopicPixel)
    
    return newImage
    
def testDeuteranopic():
    '''Draws the image returned by deuteranopic function. Also checks deuteranopic function
    by checking whether each of the deuteranopic picture's pixels have the identical red
    and green value. Also makes sure original image isn't changed after deuteranopic is
    called.
    '''
    
    file = input("Which photo would you like to test?")
    while not os.path.exists(file):   #prompt user until valid file given
        file = input("Which photo would you like to test?")
    image = FileImage(file)
    list = []  #used to store the pixels of the original image for comparison later
    noErrorMessage = "No errors found"
    errorMessage = "Error found"
    width = image.getWidth()
    height = image.getHeight()
    
    for row in range(height):
        for col in range(width):
            pixel = image.getPixel(col, row)
            list.append(pixel)   #stores the pixel values of the original image before
                                 #deuteranopic is called to check against later
            
    myImageWindow = ImageWin("Image Processing", image.getWidth() * 2, image.getHeight())
    #ensures the display of the original and the new image side by side
    image.draw(myImageWindow)
    
    newImage = deuteranopic(image)
    
    newImage.setPosition(image.getWidth() + 1, 0)
    newImage.draw(myImageWindow)
    myImageWindow.exitOnClick()
    
    for row in range(height):
        for col in range(width):
            pixel = newImage.getPixel(col, row)
            red = pixel.getRed()
            green = pixel.getGreen()
            if red != green:  #checks if every one of deuteranopic picture's pixels have
                              #identical red and green values
                return errorMessage
    
    counter = 0   #used to index into the list that stored all the pixel values of the
                  #original image
    for row in range(height):
        for col in range(width):
            pixel = image.getPixel(col, row)
            if str(list[counter]) != str(pixel):  #checks if the pixel in the original image has same
                                        #values it had before deuteranopic function was called
                return errorMessage
            counter += 1
            
    return noErrorMessage
            
def grayScalePixel(oldPixel):
    '''Converts a pixel into gray scale using a set formula. The function calculates a lumosity
    and creates a new pixel in the format: Pixel(lumosity, lumosity, lumosity)
    '''
    
    red = oldPixel.getRed() * 0.21
    green = oldPixel.getGreen() * 0.72
    blue = oldPixel.getBlue() * 0.072
    lumosity = int(red + green + blue)  #finding the total lumosity index
    newPixel = Pixel(lumosity, lumosity, lumosity)
    
    return newPixel
    
def copyToGrayScale(originalImage):
    '''Creates a new image where the new image is a gray scale version of the originalImage given
    '''
    
    newImage = pixelMapper(originalImage, grayScalePixel)
    return newImage
    

def testGrayScale():
    '''Draws the image returned by copyToGrayScale function. Also checks copyToGrayScale function
    by checking whether each of the gray scale picture's pixels have the identical red,
    green, and blue values. Also makes sure original image isn't changed after copyToGrayScale is
    called.
    '''
    
    file = input("Which photo would you like to test?")
    while not os.path.exists(file):   #prompt user until valid file given
        file = input("Which photo would you like to test?")
    image = FileImage(file)
    list = []  #used to store the pixels of the original image for comparison later
    noErrorMessage = "No errors found"
    errorMessage = "Error found"
    width = image.getWidth()
    height = image.getHeight()
    
    for row in range(height):
        for col in range(width):
            pixel = image.getPixel(col, row)
            list.append(pixel)   #stores the pixel values of the original image before
                                 #copyToGrayScale is called to check against later
            
    myImageWindow = ImageWin("Image Processing", image.getWidth() * 2, image.getHeight())
    #ensures the display of the original and the new image side by side
    image.draw(myImageWindow)
    
    newImage = copyToGrayScale(image)
    
    newImage.setPosition(image.getWidth() + 1, 0)
    newImage.draw(myImageWindow)
    myImageWindow.exitOnClick()
    
    for row in range(height):
        for col in range(width):
            pixel = newImage.getPixel(col, row)
            red = pixel.getRed()
            green = pixel.getGreen()
            blue = pixel.getBlue()
            if red != green or red != blue or blue != green:
                              #checks if every one of grayScale picture's pixels have
                              #identical red, green, and blue values
                return errorMessage
    
    counter = 0    #used to index into the list that stored all the pixel values of the
                   #original image
    for row in range(height):
        for col in range(width):
            pixel = image.getPixel(col, row)
            if str(list[counter]) != str(pixel): #checks if the pixel in the original image has same
                                                 #values it had before copyToGrayScale function was called
                return errorMessage
            counter += 1
            
    return noErrorMessage
    
def replaceWall(oldImage, background):
    '''Takes an original picture with a person in it and replaces the picture's background
    with another background picture.
    '''
    
    width = oldImage.getWidth()
    height = oldImage.getHeight()
    newImage = EmptyImage(width, height)
    
    for row in range(height):
        for col in range(width):
            originalPixel = oldImage.getPixel(col, row)
            red = originalPixel.getRed()   #below are all the requirements needed to be met
                                            #for a pixel to be a background pixel
            green = originalPixel.getGreen()
            blue = originalPixel.getBlue()
            absValue1 = math.fabs(red - green)
            absValue2 = math.fabs(red - blue)
            absValue3 = math.fabs(green - blue)
            if red >= 100 and green >= 100 and absValue1 < 30 and absValue2 < 30 and absValue3 < 30:
                newPixel = background.getPixel(col, row)   
                newImage.setPixel(col, row, newPixel)
                #if the original pixel is background pixel, we get the pixel in the given background picture
                #at the same co-ordinates and copy that pixel onto newImage in place of the original pixel
            else:
                newImage.setPixel(col, row, originalPixel)  #copy non-background pixels onto newImage
    
    return newImage
    
def main():
    '''Draws a new picture by calling replaceWall. The new picture is one of a person
    in front of a different background to the background in his / her original photo.
    '''
    
    image = input("Which image would you like to edit?")
    oldImage = FileImage(image)
    background = input("Which background would you like to use?")
    backgroundImage = FileImage(background)
    myImageWindow = ImageWin("Image Processing", oldImage.getWidth() * 2, oldImage.getHeight())
    #ensures the display of the original and the new image side by side
    oldImage.draw(myImageWindow)
    
    newImage = replaceWall(oldImage, backgroundImage)
    
    newImage.setPosition(oldImage.getWidth() + 1, 0)
    newImage.draw(myImageWindow)
    myImageWindow.exitOnClick()
    
if __name__ == '__main__':
    main()
    