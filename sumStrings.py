'''
Input  : str1 = "3333311111111111",
         str2 =   "44422222221111"
Output : 3377733333332222

'''
def sumStrings(str1, str2):
    str1 = str1[::-1]
    str2 = str2[::-1]

    str_sum = ""
    sum = 0
    digit = 0
    carry = 0


    while len(str1) > 0  or  len(str2) > 0:
        num1 = str1[:1]
        num2 = str2[:1]
        str1 = str1[1:]
        str2 = str2[1:]


        int_num1 = int(num1) if num1 else 0
        int_num2 = int(num2) if num2 else 0

        sum = int_num1 + int_num2 + carry

        digit = sum%10
        carry = sum//10

        str_sum = str_sum +  str(digit)


    if carry != 0:
        str_sum = str_sum + str(carry)

    return str_sum[::-1]


result = sumStrings("3333311111111111","44422222221111")
print(result) # '3377733333332222'
