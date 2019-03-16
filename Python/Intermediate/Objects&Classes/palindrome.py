def reverse(text):
    return text[::-1]

def palindrome(text):
    if text == reverse(text):
        print("Is palindrome!")
    else:
        print("Is Not palindrome!")

inp = input("Input the text: ")
palindrome(inp)