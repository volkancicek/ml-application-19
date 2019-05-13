import json
import random


fileName ="sample.json"
documentNumber = 10
referenceStringNumber = 100

def main():
    with open(fileName, 'r') as f:
        data = json.load(f)
    dois = getRandomDois(data)
    
    return dois

def getRandomDois(data):
        paperCount = data["size"]
        doiList =  set()
        for x in range(documentNumber):
                tmp_ind = getRandomIndex(paperCount - 1)
                doiList.add(data["sample_dois"][tmp_ind])
        
        return doiList

def getRandomIndex(maxIndex):
        return random.randint(0,maxIndex)


if __name__ == '__main__':
    main()