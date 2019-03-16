import time

try:
    f = open("Meme.txt")
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print(line)
        time.sleep(2)

except KeyboardInterrupt:
    print("Reading is canceled!")
finally:
    f.close()
    print("File is closed!")

