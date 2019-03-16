meme = """
Teacher: What are you laughing at?
Me: Nothing!
My Mind: Elon Dusk!
"""

f = open("Meme.txt", "w")
f.write(meme)
f.close()

f = open("Meme.txt")
while True:
    line = f.readline()
    if len(line) == 0:
        break
    print(line)