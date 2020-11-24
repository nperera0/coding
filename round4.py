'''Amazon tracks the errors that occur on its website very closely in order to identify bugs and quickly fix them.
However, sometimes errors are a result of a sequence of actions rather than logic on a single page alone.
How would you create a program/system that parses a log file of page requests and error codes
to identify the most common 3-page sequences that lead to an error on the third page?
 
The log file format is:
<session ID>,<pageURL>,<errorCode>
 
Example log file:

[ [1,A,0],
[1,B,0]
2,B,0
1,C,0
1,F,1
2,C,0
8,G,0
2,F,1
8,J,0
1,K,1]
...
 
Resulting erring 3-page sequence:
B->C->F (1)->K (1)->Y->H, with count of 2 occurrences in this example

'''

a = { 1: [('A',0) , ('B',0) , ('C',0)  , ('F', 1)], 2: [('B',0), ('C',0)  , ('F', 1)] }


def sessionErrors(file):

    if file is None or len(file) == 0:
        return 'error'

    sessionDict = {}

    for key, line in file.items():
        sessionId =  line[0]
        page = (line[1], line[2])

        if sessionId in sessionDict:
            sessionDict[sessionId] = sessionDict[sessionId].append(page)
        else:
            sessionDict[sessionId] = []
            sessionDict[sessionId] = sessionDict[sessionId].append(page)

    for key, value in sessionDict.items():

        if len(value) < 3:
            continue

        stack = [] # always has prev 3 items
        errors = []

        for i, session in enumerate(value):
            stack.append(session)

            if stack[2][1] == 1:
                errorSequence = (stack[0], stack[1], stack[2])
                errors.append(errorSequence)

            if i > 2:
                stack.pop(0)

    errerCount ={} # {(A,B,C): 3, (D.f.G): 5}

    for error in errors:

        if error in errerCount:
            errerCount[error] = errerCount[error] + 1
        else:
            errerCount[error] = 1


    return max(errerCount, value)

sessionErrors(a)
