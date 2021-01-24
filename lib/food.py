import json
from random import seed
from random import random
from random import sample
from random import randint
from datetime import datetime
seed(datetime.now())

def getFood():
    rev = ""
    with open('files/food.json') as f:
        data = json.load(f)
        #print(data)
        arr = sample(range(len(data)), 3)
        key = list(data.keys())
        for foodIndex in arr:
            index = randint(0, len(data[key[foodIndex]]) - 1)
            rev += "%s: %s " % (key[foodIndex], data[key[foodIndex]][index])

    return rev    

def main():
    print(getFood())

if __name__ == "__main__":
    main()
