# Returns true if str1 is smaller than str2.
def isSmaller(str1, str2):

    # Calculate lengths of both string
    n1 = len(str1)
    n2 = len(str2)

    if (n1 < n2):
        return True
    if (n2 < n1):
        return False

    for i in range(n1):
        if (str1[i] < str2[i]):
            return True
        elif (str1[i] > str2[i]):
            return False

    return False

# Function for find difference of larger numbers
def findDiff(str1, str2):

    # Before proceeding further, make sure str1
    # is not smaller
    if (isSmaller(str1, str2)):
        temp = str1
        str1 = str2
        str2 = temp

    #Take an empty string for storing result
    str3 = ""

    # Calculate length of both string
    n1 = len(str1)
    n2 = len(str2)

    # Reverse both of strings
    str1= str1[::-1]
    str2 = str2[::-1]

    carry = 0

    # Run loop till small string length
    # and subtract digit of str1 to str2
    for i in range(n2):

        # Do school mathematics, compute difference of
        # current digits

        sub = ((ord(str1[i])-ord('0'))-(ord(str2[i])-ord('0'))-carry)

        # If subtraction is less then zero
        # we add then we add 10 into sub and
        # take carry as 1 for calculating next step
        if (sub < 0):
            sub = sub + 10
            carry = 1

        else:
            carry = 0

        str3 = str3+str(sub )

    # subtract remaining digits of larger number
    for i in range(n2,n1):

        sub = ((ord(str1[i])-ord('0')) - carry)

        # if the sub value is -ve, then make it positive
        if (sub < 0):
            sub = sub + 10
            carry = 1

        else:
            carry = 0

        str3 = str3+str(sub )

    # reverse resultant string
    str3= str3[::-1]

    return str3

# Driver code
if __name__ == "__main__":
    str1 = "222"
    str2 = "555"
    print(findDiff(str1, str2))

    s1 = "100"
    s2 = "1000000"
    print(findDiff(s1,s2))

#This code is contributed by ChitraNayal
