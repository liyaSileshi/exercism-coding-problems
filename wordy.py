#Parse and evaluate simple math word problems returning the answer as an integer.

# Iteration 0 — Numbers
# Problems with no operations simply evaluate to the number given.

# What is 5?
# Evaluates to 5.

# Add two numbers together.
# What is 5 plus 13?
# Evaluates to 18.
# Handle large numbers and negative numbers.

def wordyOperation(string):
    #remove question mark
    string = string[:-1]
    op_dict = {'plus': "+"}
    #split string into array
    arr = string.split()

    if len(arr) == 3: #problem with no operation
        print(arr[-1])
    else:
        #remove the first two words ('what is')
        arr = arr[2:]

        print(arr)

wordyOperation('What is 5 plus 13?')