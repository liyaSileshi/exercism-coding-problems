#Parse and evaluate simple math word problems returning the answer as an integer.

# Problems with no operations simply evaluate to the number given.


#1, Good inputs
    #What is 5?
    #What is 5 plus 13?
    # What is 7 minus 5?
    # What is 6 multiplied by 4?
    # What is 25 divided by 5?

#2, Bad inputs
    #what is my name?
    #What is 5 plus plus?
    # What is 7 and 5?

#3, Edge case inputs
    # '' - empty string
    #What is 5?


def wordyOperation(string):
    #remove question mark
    string = string[:-1]
    # op_dict = {'plus': "+"}
    #split string into array
    arr = string.split()

    if len(arr) == 3: #problem with no operation
        print(arr[-1])

    elif len(arr) == 5:
        #remove the first two words ('what is')
        arr = arr[2:]
        #check what operator it is
        # print(arr[1] + arr[2])
        if arr[1] == 'plus':
            return int(arr[0]) + int(arr[2])
        if arr[1] == 'minus':
            return int(arr[0]) - int(arr[2])

    elif len(arr) == 6:
        arr = arr[2:] #remove the first two words
        if arr[1] + ' ' + arr[2] == 'multiplied by':
            return int(arr[0]) * int(arr[3])
        if arr[1] + ' ' + arr[2] == 'divided by':
             return int(arr[0]) / int(arr[3])

print(wordyOperation('What is 5 plus 5?'))
print(wordyOperation(' '))
