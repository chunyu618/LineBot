import json
from random import seed
from random import random
from random import sample
from random import randint
from datetime import datetime

def getFood():
    seed(datetime.now())
    rev = ""
    with open('files/food.json') as f:
        data = json.load(f)
        #print(data)
        arr = sample(range(len(data)), 3)
        key = list(data.keys())
        for foodIndex in arr:
            index = randint(0, len(data[key[foodIndex]]) - 1)
            rev += "%s: %s\n" % (key[foodIndex], data[key[foodIndex]][index])

    return rev.strip()

def main():
    print(getFood())

if __name__ == "__main__":
    main()
