'''
This program cotains two functions: blur and reduce colors.
Blur returns a blurred version of a given image, and reduce colors 
returns an image that is modified by reducing the number of
colors in an original given image.
'''
import cImage
from cImage import *
import random
import math
import os
import os.path

def blur(image, radius):
    '''
    This function creates and returns a blurry version of an image.
    For each pixel, its rgb values are the average all of the pixels in the original image
    that are within a circle of a given radius, centered at that pixel.
    '''
    height = image.getHeight()
    width = image.getWidth()
    newim = EmptyImage(width, height)
    
    for row in range(height):  
        for col in range(width):   #iterating through each pixel of the image
            pixel = blurPixel(col, row, radius, image)
            newim.setPixel(col, row, pixel)
    
    return newim
    
def blurPixel(xcoordinate, ycoordinate, radius, image):
    '''
    Carries out the blurring process, as described in blur function, on a pixel by pixel basis.
    Returns a new pixel, where the pixel is a blurred version of the pixel from the original
    image, based on the algorithm described in blur function.
    '''
    counter = 0
    red = 0
    blue = 0
    green = 0

    for row in range(ycoordinate - radius, ycoordinate + radius + 1):  
    #iterate through the rows within the range of the radius, from the ycoordinate given
        for col in range(xcoordinate - radius, xcoordinate + radius + 1):
        #iterate through the columns within the range of the radius from the xcoordinate given
            if col <= (image.getWidth() - 1) and (row <= image.getHeight() - 1) and col >= 0 and row >= 0:
            #makes sure the coordinate is within the range of the image
                distanceY = (row - ycoordinate)**2
                distanceX = (col - xcoordinate)**2
                if math.sqrt(distanceY + distanceX) <= radius:
                #checks if the distance from coordinates to-be-tested to given coordinates
                #is within the range of the radius
                    pixel = image.getPixel(col, row)
                    red += pixel.getRed()   #accumulating each pixel's rgb values
                    green += pixel.getGreen()
                    blue += pixel.getBlue()
                    counter += 1   #keeps track of how many pixel's values are summed
            
    averageRed = int(red / counter)
    averageBlue = int(blue / counter)
    averageGreen = int(green / counter)
    
    pixel = Pixel(averageRed, averageGreen, averageBlue)
    return pixel

def reduceColors(image, numberOfColors):
    '''
    Creates a new image by reducing the number of colors of a given image.
    ''' 
    height = image.getHeight()
    width = image.getWidth()
    
    pixelList = []       #used later for storing the values of pixels that are assigned to
                         #each respective cluster
    clusterColors = []   #stores cluster colors' values
    for i in range(numberOfColors):
        red = random.randint(0, 256)
        green = random.randint(0, 256)
        blue = random.randint(0, 256)
        tuple = (red, green, blue)
        clusterColors.append(tuple)
        pixelList.append([])  #creates n empty lists within pixelList, where n is the
                              #numberOfColors
    
    assignedList = assignPixelsToCluster(pixelList, clusterColors, numberOfColors, image, height, width)
    #retrieves list of which cluster each pixel is assigned to
    for i in range(9):
        newClusterColors = modifyClusterValues(assignedList)  #calculate new cluster colors
                                                              #based on assigned pixels
        pixelList = []
        for i in range(numberOfColors):
            pixelList.append([]) #clears pixelList by making a new empty pixelList to be
                                 #passed used for the next iteration
        assignedList = assignPixelsToCluster(pixelList, newClusterColors, numberOfColors, image, height, width)
        
        
    
    newClusterColors = modifyClusterValues(assignedList)
    newim = createImage(newClusterColors, image, height, width, numberOfColors)
    #create new image based on the final new cluster color values obtained
    
    return newim
    
def assignPixelsToCluster(pixelList, clusterColors, numberOfColors, image, height, width):
    '''
    Assigns each pixel in an image to the closest cluster color. Returns a list that contains
    lists within it, i.e. [[], [], [], ...[]], where each of these lists
    stores the values of the pixels that are assigned to a each cluster color.
    '''
    for row in range(height):
        for col in range(width):
            pixel = image.getPixel(col, row)
            red = pixel.getRed()
            green = pixel.getGreen()
            blue = pixel.getBlue()
            
            differences = []  #stores the pixel's difference with each cluster
            for n in range(numberOfColors):
                redDiff = math.fabs(red - clusterColors[n][0])
                greenDiff = math.fabs(green - clusterColors[n][1])
                blueDiff = math.fabs(blue - clusterColors[n][2])
                totalDiff = redDiff + greenDiff + blueDiff
                differences.append(totalDiff)
            smallestDiff = min(differences)   
            clusterNumber = differences.index(smallestDiff)   #finds the cluster number
                                                              #that the pixel was assigned to
            pixelList[clusterNumber].append(pixel)   #appends the pixel's values to the
                                                     #list within pixelList that corresponds
                                                     #to the assigned cluster color
    
    return pixelList
    
def modifyClusterValues(pixelList):
    '''
    Assigns each cluster color to equal the average rgb values of the pixels that were
    assigned to the cluster. 
    The new set of cluster colors is returned as lists within lists.
    '''
    newClusterColors = []
    for list in pixelList:  #iterate through each color cluster
        red = 0
        green = 0
        blue = 0
        for tuple in list:  #iterate through values of each pixel assigned to the cluster
            red += tuple[0]   #sums the rgb values of each pixel in assigned to the cluster
            green += tuple[1]
            blue += tuple[2]
        if list != []:  #if at least one pixel was assigned to the cluster
            averageRed = int(red / len(list))
            averageGreen = int(green / len(list))
            averageBlue = int(blue / len(list))
            clusterColor = (averageRed, averageGreen, averageBlue)
            newClusterColors.append(clusterColor)
        else:     #in case no pixels were assigned to the cluster
            clusterColor = (0, 0, 0)
            newClusterColors.append(clusterColor)
    
    return newClusterColors

def createImage(clusterColors, image, height, width, numberOfColors):
    '''
    Creates a new image where each pixel value is the value of the final assigned
    cluster color for the pixel at that location, based on the given image. 
    '''
    newim = EmptyImage(width, height)
    
    for row in range(height):
        for col in range(width):
            pixel = image.getPixel(col, row)
            red = pixel.getRed()
            green = pixel.getGreen()
            blue = pixel.getBlue()
            
            differences = []
            for n in range(numberOfColors):
                redDiff = math.fabs(red - clusterColors[n][0])
                greenDiff = math.fabs(green - clusterColors[n][1])
                blueDiff = math.fabs(blue - clusterColors[n][2])
                totalDiff = redDiff + greenDiff + blueDiff
                differences.append(totalDiff)
            smallestDiff = min(differences)
            clusterNumber = differences.index(smallestDiff)
            newPixel = Pixel(clusterColors[clusterNumber][0], clusterColors[clusterNumber][1], clusterColors[clusterNumber][2])
            #creates a new pixel by using the rgb values of the cluster to which
            #the original pixel is closest to
            newim.setPixel(col, row, newPixel)
    
    return newim
    
def main():
    '''
    Prompts user input for the functions they want to call, the file they wish to edit,
    and the filename to which they would like the result to be saved to.
    Saves the new image under the filename given.
    '''
    response = input("Would you like to blur or to reduce colors?")
    while response not in ["blur", "reduce colors"]:
        response = input("Would you like to blur or to reduce colors?")
    file = input("Which file would you like to edit?")
    while not os.path.exists(file):
        file = input("Which file would you like to edit?")
    image = FileImage(file)
    newFilename = input("What filename would you like the image to be saved to?")
    while os.path.exists(newFilename):
        newFilename = input("What filename would you like the image to be saved to?")
    if response == "blur":
        radius = input("What would you like the radius of the blur to be?")
        radius = int(radius)
        newim = blur(image, radius)
    elif response == "reduce colors":
        colors = input("How many colors would you like the image to be reduced to?")
        colors = int(colors)
        newim = reduceColors(image, colors)
    newim.save(newFilename)
    
    myImageWindow = ImageWin("Image Processing", image.getWidth() * 2, image.getHeight())
    #ensures the display of the original and the new image side by side
    image.draw(myImageWindow)
    newim.setPosition(image.getWidth() + 1, 0)
    newim.draw(myImageWindow)
    myImageWindow.exitOnClick()
    
if __name__ == "__main__":
    main()

    

                
            
        