"""
Implement atoi which converts a string to an integer.

Cases:

-> basic conversion from string to integer

-> if we have anything in our string which is not numerical we are skipping it. Ex: "4193 with words". That the numerical part should be occuring first.

-> if we have non-numerical part before the numerical part, we return 0 Ex: "words and 987" -> 0

-> if there are whitespace characters, then ignore them and move on.

-> there can be both +ve and -ve numbers in our input string

-> if the integer number obtained is out of range then return 0.


Examples:
    1. "     83" -> 83"
    S1 : "83 with wior"


    "83" -> 83
    negative = True
    "83" -> 83
    if negative is True:
    -83
    else:
    83
    ""
    "-83" > 83

    "-" or "+" => ""
    "-43 with words"
    "words with 54"
    "43567" -> 4 3 5 6 7

     1000 100 10 0


     0*10 + int(c) => 0+4 = 4
     4*10 + int(3) => 40+3 = 43
     43*10 + int(5) => 430+5 = 435
     43567
"""

def myAtoi(str):
    #S1: what happens when we have whitespace characters
    str = str.strip()

    #S2: identify if it's +ve or -ve
    negative = False
    if str and str[0] == "-":
        negative = True

    #negative = True if str[0] == "-" else False

    #S3: removed the sign and obtain the actual number
    if str and (str[0] == '+' or str[0] == '-'):
        str = str[1:]

    # if string becomes invalid after removing the sign -> ""
    if not str:
        return 0

    #S4: check for non-numeric characters
    # set(['1', '0', '3', '2', '5', '4', '7', '6', '9', '8'])
    digits = {i for i in '0123456789'}

    result = 0
    for c in str:
        # if it's invalid
        if c not in digits:
            break

        # 4567 with words
        # words with 4567
        result = result * 10 + int(c)
        #print("result: ", result)

    # utilizing the -ve sign
    if negative:
        result = -result

    # remember
    # S5: checking for overflow cases
    result = max(min(result, 2**31-1), -2**31)
    print("result", result)
    # INT_MIN : -2**31
    # INT_MAX : 2**31-1

myAtoi("42")
myAtoi("-42")
myAtoi("words with 345")
myAtoi("234 with words")
myAtoi("      234      ")
myAtoi("  -324")
print(myAtoi("-"))
print(myAtoi(""))

