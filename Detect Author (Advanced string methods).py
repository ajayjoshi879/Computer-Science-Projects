'''
A program which can take a text file and a set of author names and determine by which of the
given authors the text is written.

Written as classwork project by Andrew Qi at Carleton College Fall 2015
'''
import os
import os.path
import math

# Functions for getting words and sentences
def getWords(text):
    ''' Returns a list of the words (in order) that are stored
    in text. text is a list of strings.
    '''
    list = []
    for string in text:
        string = cleanUp(string) #removes punctuation from the beginning and the end of a string
        list += string.split()
    return list 
        
def getSentences(text):
    ''' Returns a list of the sentences (in order) that are stored
    in text. text is a list of strings; sentences may extend across
    multiple items in the list (e.g., text might be a list
    with each item corresponding to one line in a file; sentences
    don't automatically end with new lines in a file).
    '''
    list = []
    emptyString = ""
    for sentence in text:
        for i in range(len(sentence)):
            emptyString += sentence[i]   #accumulating each character that is iterated
                                         #until a punctuation is reached
            if sentence[i] == "." or sentence[i] == "!" or sentence[i] == "?":
                list.append(emptyString)  #adds whatever is stored in emptyString thus far
                                          #as a string into list
                emptyString = ""
    return list

def cleanUp(s):
    ''' Returns a string which is a copy of s in which all letters have been
    converted to lowercase and punctuation characters have been stripped 
    from both ends. Inner punctuation is left untouched. 
    '''
    punctuation = '''!"',;:.-?)([]<>*#\n\t\r'''
    result = s.lower().strip(punctuation)
    return result

# Functions for linguistic features

def averageWordLength(text):
    '''This is calculating the average length of all words in text.
    '''
    totalCounts = 0
    sentenceList = getSentences(text)  #gets list of complete sentences from text
    wordsList = getWords(sentenceList)  #gets list of all the words we are working with
    for word in wordsList:
        totalCounts += len(word) 
    averageCount = totalCounts / len(wordsList)
    return averageCount

def averageSentenceLength(text):
    '''Calculates the average number of words in each sentence in text.
    '''    
    list = []
    totalCounts = 0
    sentenceList = getSentences(text)
    for sentence in sentenceList:
        list.append(sentence)  #sentence is added to list as
                               #getWords only takes a list as a parameter
        wordsList = getWords(list)
        totalCounts += len(wordsList)
        list = []   #reset list for the next sentence in the loop
    averageCount = totalCounts / len(sentenceList)
    return averageCount

def averageSentenceComplexity(text):
    '''Calculates the average number of phrases in each sentence in text.
    '''    
    list = []
    sentenceList = getSentences(text)
    emptyString = ""
    punctuation = ",;:.!?"
    for sentence in sentenceList:
        for i in range(len(sentence)):
            emptyString += sentence[i]  #accumulating each character in the sentence
                                        #until a punctuation is reached
            if sentence[i] in punctuation:
                list.append(emptyString)  #adds characters accumulated as a phrase into list
                emptyString = ""  #resets emptyString to store next phrase
    averageCount = len(list) / len(sentenceList)
    return averageCount
    
def typeToTokenRatio(text):
    '''Calculates the ratio between the number of distinct words in a text divided by the 
    total number of words in text.
    '''    
    sentenceList = getSentences(text)
    wordsList = getWords(sentenceList)
    copyList = []
    totalCount = 0
    count = 0
    for word in wordsList:
        totalCount += 1  #counts the total number of words
        if word not in copyList:
            copyList.append(word)  #adds the word if it has not occurred before in the text
            count += 1     #counts the number of distinct words
    tokenRatio = count / totalCount
    return tokenRatio
    
def hapaxLegomanaRatio(text):
    '''Calculates the ratio between the total number of words that occur exactly once 
    divided by the total number of words in text.
    '''
    sentenceList = getSentences(text)
    wordsList = getWords(sentenceList)
    copyList = []
    totalCount = 0
    uniqueCount = 0
    for word in wordsList:
        totalCount += 1   #counts the total number of words
        count = wordsList.count(word)  #count number of times word appears in wordsList
        if count == 1:   #if word only occurs once in text
            uniqueCount += 1
    legomanaRatio = uniqueCount / totalCount
    return legomanaRatio
    
    
def functionWordRatios(text):
    '''Calculates a list of ratios. Each ratio is the number of times a particular function 
    word occurs divided by the total number of words in text.
    '''
    sentenceList = getSentences(text)
    wordsList = getWords(sentenceList)
    functionList = getAllFunctionWords()
    ratioList = []
    for word in functionList:  #for each function word we are searching
        count = 0
        totalCount = 0
        for aWord in wordsList: #iterating through all the words in the text
            totalCount += 1  #counts total number of words
            if word == aWord:  #if the word in text is a function word
                count += 1
        ratio = count / totalCount
        ratioList.append(ratio)
    return ratioList
    
def getAllFunctionWords():
    '''Returns a list of function words stored
    in the function word file ('FunctionWordList.txt').
    Each item in the list is a function word. This function
    does not check the format of the file, so make sure you 
    do not modify FunctionWordList.txt and that it is
    in the same directory as detectAuthor.py
    '''
    file = open('FunctionWordList.txt', 'r')
    wordList = []
    for line in file:
        wordList.append(line.strip().split()[0])
    file.close()
    return wordList

# Functions for calculating, reading, and writing signatures
def calculateSignatureFromURL(url):
    '''TODO: Implement this function, filling in this comment to match 
    the assignment.
    '''
    pass # remove this and add your own code instead

def calculateSignatureFromTextFile(filename):
    '''Returns a list of the results of each linguistic feature calculation
    '''
    list = [""]
    file = open(filename, 'r')
    text = file.readlines()
    result1 = averageWordLength(text)
    list.append(result1)
    result2 = averageSentenceLength(text)
    list.append(result2)
    result3 = averageSentenceComplexity(text)
    list.append(result3)
    result4 = typeToTokenRatio(text)
    list.append(result4)
    result5 = hapaxLegomanaRatio(text)
    list.append(result5)
    result6 = functionWordRatios(text)
    for i in range(len(result6)): 
        list.append(result6[i])  #adding each value in result6 as a new item into the list,
                                 #to prevent having a list within a list
    return list

def readSignature(filename):
    '''Read a linguistic signature from filename and return it as 
    list of features. 
    '''
    file = open(filename, 'r')
    # The first feature is the name of the author (a string) so it 
    # doesn't need casting to float
    result = [file.readline().strip()]
    # All remaining features are real numbers
    for line in file:
        result.append(float(line.strip()))
    file.close()
    return result
    
def writeSignature(signature, signatureFile):
    '''Writes the signature (list of feature weights) to a new file named 
    signatureFile.  Overwrites any existing file in that location.
    '''
    file = open(signatureFile, 'w')
    for i in range(len(signature)):
        file.write(str(signature[i]) + '\n')
    file.close()

def calculateAuthorSignature(directoryWithAuthorsWork, authorName):
    '''TODO: Implement this function, filling in this comment to match 
    the assignment.
    '''
    pass # remove this and add your own code instead 

# Functions related to similarity
def computeSimilarity(signature1, signature2, weights):
    '''Returns the similarity between signature1 and signature2,
    computed as the absolute value of the difference between the two
    signatures, multiplied by the weights and summed. signature1,
    signature2, and weights are all lists where the 0th value in
    the list is ignored.
    '''
    sum = 0
    for i in range(1, len(signature1)):
        value = math.fabs(signature1[i] - signature2[i]) * weights[i] 
        sum += value 
    return sum    #the similarity between the two signatures
    
            
    
def getWeights():
    '''Returns a list of weights for the similarity calculation.
    The weights are in the order of the features: average word
    length, average sentence length, average sentence complexity,
    type to token ratio, hapax legomana ratio, and then all of the
    function word weights. This function assumes FunctionWordList.txt
    is in the same directory as detectAuthor.py.
    '''
    featureWeights = [0, 11, 0.4, 4,33 , 50]
    file = open('FunctionWordList.txt', 'r')
    for line in file:
        featureWeights.append(float(line.strip().split()[1]))
    file.close()
    return featureWeights
    
def getMostSimilarAuthor(signatureDirectory, mysterySignature):
    '''Returns the author name for the signature
    that has the smallest similarity score (smaller = more similar).
    The code for going through a directory of files and reading the 
    signatures is provided for you. You need to modify this function
    to find and return the most similar author. 
    '''
    # The weights are a mixture of hardcoded weights for the non-function
    # word features and specified in the function word file.
    featureWeights = getWeights()
    
    # The line below lists all files that are in the directory
    # signature directory.
    files = os.listdir(signatureDirectory)

    minSimilarity = 1000    #used to store the smallest similarity found to compare to later values;
                             #initiating at 1000 ensures first similarity found in the loop
                             #will be smaller than minSimilarity
    for currentFile in files:
        # The condition below ignores hidden files that may be created 
        # by your operating system
        if not currentFile.startswith('.'):
            # The line below calculates the signature for the current file
            signature = readSignature(signatureDirectory + os.sep + currentFile)
            #Line below computes the similarity between unknown signature and known signature
            similarity = computeSimilarity(mysterySignature, signature, featureWeights)
            if similarity < minSimilarity: #lower similarity value means
                                                    #more similar signature
                author = signature[0]  #keep track of author with most similar signature
                minSimilarity = similarity  #keeps track of lowest similarity found thus
                                             #far to compare to in subsequent iterations
    
    return author    
    
    
    
# Printing and user interface
def printSignature(signature):
    '''Prints a signature to the console, one
    line per feature.
    '''
    features = ['Average word length', 'Average sentence length', 
                'Average sentence complexity','Type to token ratio',
                ' Hapax Legomana ratio']
    print('Signature:')
    # First, print all the features that are not related to fn words
    for i in range(1,len(features)):
        print(features[i-1] + ':', str(signature[i]))
        
    # Now, print all the function word features.
    # Note that the indices differ between where the word is in the
    # list of function words and where the value is for that feature
    # in the signature.
    fnWords = getAllFunctionWords()
    for i in range(len(features)+1,len(signature)):
        print(fnWords[i - (len(features)+1)] + ':', str(signature[i]))

def main():
    '''This function asks the user for a filename and directory to analyze.
    '''
    print("Welcome! This program guesses the author of a mystery text!")
    filename = input("What file would you like to analyze? ")
    while not os.path.exists(filename):  #prompts user until valid response given
        filename = input("What file would you like to analyze? ")
    file = open(filename, 'r')
    text = file.readlines()
    directory = input("Please enter the name of the directory with the signature files: ")
    while not os.path.isdir(directory):  #prompts user until valid response given
        directory = input("Please enter the name of the directory with the signature files: ")
    
    mysterySig = calculateSignatureFromTextFile(filename)  #gets the signature of the file
                                                           #we wish to test
    author = getMostSimilarAuthor(directory, mysterySig)
    print("The most similar author was", author, ".")
    
    file.close()
    

if __name__ == '__main__':
    main()


    