class ShortInputException(Exception):
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast


try:
    text = input("Input your text here: ")
    if len(text) < 4:
        raise ShortInputException(len(text), 4)

except EOFError:
    print("Get out with your EOF")
except KeyboardInterrupt:
    print("OMG fckyrslf, you have canceled the program, get out bch!!")
except ShortInputException as ex:
    print(f"You have as short text, as your self confidence!!, {ex.length } symbols!")
else:
    print(f"GoodJob bruh, you have types the following-> {text}")
