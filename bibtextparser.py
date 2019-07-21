import uuid

import bibtexparser
import pandas as pd


def main():
    numOfEach = {}
    listA = []
    listB = []
    matches = []
    set1 = []
    set2 = []
    set1header = 'id1,author,title,journal,year'
    set2header = 'id2,author,title,journal,year'
    fileName = 'exparser_result.csv'
    fileAddress = 'data/raw/crossref/exparser/'

    # df = pd.read_csv("data/raw/crossref/" + fileName, encoding='utf-8', sep='\t')
    df = pd.read_csv("data/raw/crossref/" + fileName, encoding='ISO-8859-1', sep='\t')
    for index, row in df.iterrows():
        bibtex_file = row["bibtex_string"]
        bib_database = bibtexparser.loads(bibtex_file)
        for entry in bib_database.entries:
            entry["ID"] = row["id"]
            entry["RefID"] = str(uuid.uuid1())
            listA.append(entry)

    listB = listA.copy()

    matches.append('id1,id2')
    for elemA in listA:
        for elemB in listB:
            if elemA['ID'] == elemB['ID']:
                matches.append(elemA['RefID'] + ',' + elemB['RefID'])
    save_to_file(matches, fileAddress + "matches.csv")

    create_and_save(set1, listA, set1header, fileAddress + "set1.csv")
    create_and_save(set2, listB, set2header, fileAddress + "set2.csv")


def make_entry(tag):
    return "\"" + tag + "\""


def save_to_file(input, filename):
    with open(filename, "w", encoding='UTF-8') as outfile:
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
        result = result + get_year_as_number(entry[YearTag])
    return result


def create_set_for_input(set, list):
    for elem in list:
        set.append(create_result_for_entry(elem))
    return set


def add_header(setheader, set):
    set.insert(0, setheader)
    return set


def create_and_save(set, list, setheader, filename):
    set = create_set_for_input(set, list)
    set = add_header(setheader, set)
    save_to_file(set, filename)


def get_year_as_number(year):
    extracted_year = ""
    for i in year:
        if i.isdigit():
            extracted_year += i
            if len(extracted_year) == 4:
                return extracted_year
        else:
            extracted_year = ""
    return ""


if __name__ == '__main__':
    main()
