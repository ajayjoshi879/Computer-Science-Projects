'''
This module includes functions to encode and decode messages using autokey double-Caesar cipher.
There are two options for encoding (and decoding): the leave out non-letter characters, or encode
the non-letter characters " " and "\n"

A main function allows the user to run the encode and decode functions by getting user input
'''

def encodeOrEncodeSpace(message, stringS, n, alphabet):
    ''' This function carries out encode function or encodeSpace function, depending on the
Boolean expression.
    '''
    message = message.lower()
    stringS = stringS.lower()
    encrypt = ""
        
    if len(alphabet) == 26:   #if we do not wish to encode spaces
        message = message.replace(" ", "")
        
    for i in range(n*len(stringS)):   #range up to the number of times stringS can be used
        if i == len(message):         #return if message is fully encoded before n times stringS is all used up
            return encrypt
        stringIndex = letterToIndex(alphabet, stringS[i% len(stringS)])   #% operator makes sure we don't index past
                                                                          #the length of the string
        messageIndex = letterToIndex(alphabet, message[i])
        newIndex = (stringIndex + messageIndex) % len(alphabet)  #% operator makes sure newIndex is within the alphabet length
        newChar = indexToLetter(alphabet, newIndex)
        encrypt += newChar
            
    if len(message) > (n*len(stringS)):   #if message is not fully encoded after n times stringS is used up
        remainingChar = len(message) - (n*len(stringS))    #number of characters left to encode
        for i in range(remainingChar):
            messageIndex = letterToIndex(alphabet, message[i + (n*len(stringS))])   #ensures we index from the
                                                                                    #message from where we left off
            stringIndex = letterToIndex(alphabet, message[i])
            newIndex = (stringIndex + messageIndex) % len(alphabet)
            newChar = indexToLetter(alphabet, newIndex)
            encrypt += newChar
            
    return encrypt 
         
def encode(message, stringS, n):
    ''' This function encodes a message by removing non-letter characters in the encrypted 
message.
    '''
    encryptMsg = encodeOrEncodeSpace(message, stringS, n, 'abcdefghijklmnopqrstuvwxyz')  #calls the encoding function
                                                                                         #by passing an a-z alphabet
                                                                                         #for function to reference
    return encryptMsg

def encodeSpace(message, stringS, n):
    ''' This function encodes the message, including non-letter characters.
    '''
    encryptSpaceMsg = encodeOrEncodeSpace(message, stringS, n, 'abcdefghijklmnopqrstuvwxyz \n')  #calls the encoding function
                                                                                                 #by passing an a-z + " " +
                                                                                                 #"\n" alphabet to reference
    return encryptSpaceMsg

def decodeOrDecodeSpace(message, stringS, n, alphabet):
    ''' This function carries out decode function or decodeSpace function, depending on the
Boolean expression.
    '''
    message = message.lower()
    stringS = stringS.lower()
    decrypt = ""

    if len(alphabet) == 26:  #if we are to decode a message whose space and new line characters aren't encoded
        message = message.replace(" ", "")
        
    for i in range(n*len(stringS)):
            if i == len(message):   #if we finish decoding before using up all the stringS characters n times
                return decrypt
            stringIndex = letterToIndex(alphabet, stringS[i % len(stringS)]) 
            messageIndex = letterToIndex(alphabet, message[i])
            newIndex = messageIndex - stringIndex
            if newIndex < 0:                  
                newIndex = newIndex + len(alphabet)   #wrapping the newIndex back around the alphabet
            decryptChar = indexToLetter(alphabet, newIndex)
            decrypt += decryptChar

    if len(message) > (n*len(stringS)):       #if message is not fully decoded after stringS characters are used n times
        remainingChar = len(message) - (n*len(stringS))
        for i in range(remainingChar):
            messageIndex = letterToIndex(alphabet, message[i + (n*len(stringS))])   #indexing from where the previous
                                                                                    #for loop finished off
            stringIndex = letterToIndex(alphabet, decrypt[i])    #indexing back into the decrypted string that we have compiled
            newIndex = messageIndex - stringIndex
            if newIndex < 0:
                newIndex = newIndex + len(alphabet)
            decryptChar = indexToLetter(alphabet, newIndex)
            decrypt += decryptChar 
    
    return decrypt

def decode(message, stringS, n):
    ''' This function decodes a message and preserves non-letter characters in the decrypted 
message.
    '''
    decryptMsg = decodeOrDecodeSpace(message, stringS, n, 'abcdefghijklmnopqrstuvwxyz')   #calls the encoding function
                                                                                          #by passing an a-z
                                                                                          #alphabet to reference
    return decryptMsg

def decodeSpace(message, stringS, n):
    ''' This function decodes the message, including non-letter characters.
    '''
    decryptSpaceMsg = decodeOrDecodeSpace(message, stringS, n, 'abcdefghijklmnopqrstuvwxyz \n')  #calls the encoding function
                                                                                                 #by passing an a-z + " " +
                                                                                                 #"\n" alphabet to reference
    return decryptSpaceMsg


def main():
    ''' This function allows the user to choose whether to encode or decode, what message to
encode/decode, a key, and how many times the key is going to be used.
    '''
    userInput = input("Do you want to encode or decode? ")
    useInput = userInput.lower()
    if userInput == "encode":
        message = input("What message would you like to encode? ")
        key = input("Please type in a key: ")
        n = input("How many times would you like the key to be used? ")
        int_n = int(n)     #converting the input from a string to integer
        encryptedMsg = encode(message, key, int_n)   #call encode with all the user input given
        print("Encrypted Message:", encryptedMsg)
    elif useInput == "decode":
        message = input("What message would you like to decode? ")
        key = input("Please type in a key: ")
        n = input("How many times would you like the key to be used? ")
        int_n = int(n)
        decryptedMsg = decode(message, key, int_n)
        print("Decrypted Message:", decryptedMsg)
    
if __name__ == '__main__':
    main()

    
#Referenced from course textbook p.93 Listing 3.1
def letterToIndex(alphabet, ch):
    ''' This function converts letter characters to index values.
    '''
    idx = alphabet.find(ch)
    if idx < 0:
        print("error: letter not in the alphabet", ch)
    return idx

#Referenced from course textbook p.93 Listing 3.1
def indexToLetter(alphabet, idx):
    ''' This function converts index values back to letter characters.
    '''
    if idx > len(alphabet):
        print('error:', idx, 'is too large')
        letter = ''
    elif idx < 0:
        print('error:', idx, 'is less than 0')
        letter = ''
    else:
        letter = alphabet[idx]
    return letter