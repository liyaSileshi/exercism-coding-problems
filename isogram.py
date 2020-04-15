# Determine if a word or phrase is an isogram.
# An isogram (also known as a "nonpattern word") 
# is a word or phrase without a repeating letter, 
# however spaces and hyphens are allowed to appear 
# multiple times.
# Examples of isograms(inputs):
#1, Good inputs
    # 'lumberjacks'
    # 'background'
    # 'downstream'
    # 'six-year-old'

#2, Bad inputs
    # 3425
    #2.55

#3, Edge case input
    # '' - empty string
    #

def isIsogram(word):
    #make a histogram
    #if key is letter and value is > 1: return False
    word = word.strip() #to remove all whitespaces
    
    if len(word) == 0:
        return 'Please enter a valid word'

    hist = dict()
    #create a histogram
    try:
        for i in word:
            if i in hist:
                hist[i] += 1
            else:
                hist[i] = 1
        print(hist)
        #loop through the histogram keys and values
        #check if it's a letter and if value == 1
        for key, value in hist.items():
            if key.isalpha() and value > 1:
                return False
        return True

    except TypeError:
        return 'Sorry only strings allowed'



print(isIsogram('    '))