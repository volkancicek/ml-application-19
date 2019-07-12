import bibtexparser
import uuid

def main():


    numOfEach = {}
    listA = []
    listB = []
    matches = []
    set1 = []
    set2 = []

    with open('data/cermine_result.bib', encoding='utf-8') as bibtex_file:
        bib_database = bibtexparser.load(bibtex_file)

    for entry in bib_database.entries:
        entry["RefID"] = str(uuid.uuid1())
        if entry["ID"] in numOfEach:
            if numOfEach[entry["ID"]] % 2 == 0:
                numOfEach[entry["ID"]] += 1
                listA.append(entry)
            else:
                numOfEach[entry["ID"]] += 1
                listB.append(entry)
        else:
            numOfEach[entry["ID"]] = 1
            listA.append(entry)



    for elemA in listA:
        for elemB in listB:
            if elemA['ID'] == elemB['ID']:
                matches.append(elemA['RefID']+','+elemB['RefID'])
    save_to_file(matches,"data/matches.csv")

    save_to_file(create_set_for_input(set1, listA),"data/set1.csv")
    save_to_file(create_set_for_input(set2, listB), "data/set2.csv")

def make_entry(tag):
    return "\""+tag+"\""

def save_to_file(input,filename):
    with open(filename, "w" ,encoding='UTF-8') as outfile:
        for entries in input:
            outfile.write(entries)
            outfile.write("\n")

def create_result_for_entry(entry):
    AuthorTag = 'author'
    TitleTag = 'title'
    JournalTag = 'journal'
    PublisherTag = 'publisher'
    YearTag = 'year'
    result = ''
    result = result + make_entry(entry["RefID"])
    result = result + ','
    if TitleTag in entry:
        result = result + make_entry(entry[TitleTag])
    result = result + ','
    if AuthorTag in entry:
        result = result + make_entry(entry[AuthorTag])
    result = result + ','
    if JournalTag in entry:
        result = result + make_entry(entry[JournalTag])
    result = result + ','
    if YearTag in entry:
        result = result + make_entry(entry[YearTag])
    return result

def create_set_for_input(set, list):
    for elem in list:
        set.append(create_result_for_entry(elem))
    return set

if __name__ == '__main__':
    main()






