import pickle

superdata = ["FBI1234", "FBI4543"]
print(superdata)

f = open("database.data", "wb")
pickle.dump(superdata, f)
f.close()
print("Files are now in safe area!!")

print("\nTime to get the data!!!")

f = open("database.data", "rb")
superdata = pickle.load(f)
f.close()

print(superdata)