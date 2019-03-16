def reverse(text):
    return text[::-1]


def rmvsp(text):
    return text.replace(" ", "")


def palindrome(text):
    if rmvsp(text).upper() == reverse(rmvsp(text)).upper():
        print("Is palindrome!!")
    else:
        print("Is not palindrome!!")


inp = input("Input the text here: ")

palindrome(inp)
