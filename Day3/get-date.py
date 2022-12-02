from datetime import datetime as dt
from time import sleep
import os

def clear():
    if os.name == "nt":
        _ = os.system("cls")
    else:
        _ = os.system("clear")

print(dt.today())
print(str(dt.today()).split(" ")[0].replace("-",":"))


def zeit():

    time = str(dt.today()).split(" ")[0].replace("-",":")
    return time


print("hallo")
sleep(5)
clear()

def main():
    while