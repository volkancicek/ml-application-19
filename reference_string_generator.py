import random
import habanero as ha
import csv
import json


inputFile = "sample.json"
outputFileJson = "reference_strings.json"
outputFileTxt = "reference_strings.txt"
outputFileCSV = "reference_strings.csv"
documentNumber = 10
refStyles = ('apa', 'chicago-annotated-bibliography', 'ieee')
maxReferencePerPaper = 4


def main():
    with open(inputFile, 'r') as f:
        data = json.load(f)
    dois = get_random_dois(data)
    doi_styles = dict()

    ref_str_list = list()
    for doi in dois:
        ref_string_count = int(get_random_index(maxReferencePerPaper)) + 1
        for i in range(ref_string_count):
            ref_style = refStyles[get_random_index(len(refStyles))]
            if doi in doi_styles:
                if ref_style in doi_styles[doi]:
                    continue
            else:
                doi_styles[doi] = list()

            ref_str = create_reference_string(dois[doi], ref_style)
            doi_styles[doi].append(ref_style)
            row = [dois[doi], doi, ref_style, ref_str]
            ref_str_list.append(row)

    try:
        write_reference_data_json(ref_str_list)
    except:
        print("!!!ERROR writing to JSON")
    try:
        write_reference_data_txt(ref_str_list)
    except:
        print("!!!ERROR writing to txt")
    try:
        generate_reference_data_csv(ref_str_list)
    except:
        print("!!!ERROR writing to CSV")

    print(ref_str_list)


def get_random_dois(data):
    paper_count = data["size"]
    doi_list = {}
    _id = 0
    for x in range(documentNumber):
        tmp_ind = get_random_index(paper_count)
        doi_list[_id] = (data["sample_dois"][tmp_ind])
        _id += 1
        
    return doi_list


def get_random_index(max_num):
    return random.randint(0, max_num - 1)


def create_reference_string(doi, ref_style):
    ref_string = ha.cn.content_negotiation(ids=doi, format="text", style=ref_style)
    return ref_string


def generate_reference_data_csv(rows):
    output = open(outputFileCSV, 'w')
    writer = csv.writer(output)
    writer.writerow(['doi', 'id', 'style', 'reference string'])
    writer.writerows(rows)


def write_reference_data_txt(refs):
    with open(outputFileTxt, 'w') as f:
        for item in refs:
            f.write("%s\n" % str(item))


def write_reference_data_json(data):
    with open(outputFileJson, 'w') as outfile:
        json.dump(data, outfile)


if __name__ == '__main__':
    main()
