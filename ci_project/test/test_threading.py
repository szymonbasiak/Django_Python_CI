import time
import os

print("### TEST for 2 jobs threading... PATH: ", os.getcwd())

file1 = "../coordinates1.txt"
file2 = "../coordinates2.txt"
while True:
    with open(file1, "r") as fil:
        content1 = fil.readlines()
        fil.close()
    with open(file2, "r") as fil:
        content2 = fil.readlines()
        time.sleep(1)
        print(f"{content1} | {content2}")
        fil.close()