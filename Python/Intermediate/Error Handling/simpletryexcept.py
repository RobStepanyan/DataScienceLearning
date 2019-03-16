try:
    text = input("Input the text here!")
except EOFError:
    print("It's an EOFError btch!!")
except KeyboardInterrupt:
    print("You canceled the process!!")
else:
    print(f"You have typed {text}")