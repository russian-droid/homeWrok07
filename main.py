#from codewars.com
#alphabet_position("The sunset sets at twelve o' clock.")
#Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" (as a string)

def alphabet_position(text):
    letters = {
    'A':1, 'B':2, 'C':3, 'D':4,
    'E':5, 'F':6, 'G':7, 'H':8,
    'I':9, 'J':10, 'K':11, 'L':12,
    'M':13, 'N':14, 'O':15, 'P':16,
    'Q':17, 'R':18, 'S':19, 'T':20,
    'U': 21, 'V': 22, 'W': 23, 'X': 24,
    'Y': 25, 'Z': 26,
    ' ':'', '.':'' ,'\'':''
    } 

    text = text.upper() #transform to all caps
    listLetters=list(text) #get rid of hyphens and split into words
    #print(listLetters) #check on what's going on

    listNew=[]
    for item in listLetters:
        a=letters.get(item) #get values (digits) from dict
        listNew.append(a) #and create a new list with digits
    #print(listNew) #check on what's going on

    while ("" in listNew): 
        listNew.remove("") #remove empty elements from list
    #print(listNew) #check on what's going on
        
    #print(*listDigits)
    #print(*listNew)
    sent_str = ""
    for i in listNew:
        sent_str += str(i) + " "
    sent_str = sent_str[:-1]
    
    return sent_str


text="The sunset sets at twelve o' clock."
alphabet_position(text)
