import random
import habanero as ha
import csv
import json
from config import conf


def main():
    with open(conf['input_file'], 'r') as f:
        data = json.load(f)
    dois = get_random_dois(data, conf['reference_paper_count'])
    doi_styles = dict()
    reference_style_count = len(conf['reference_styles'])
    ref_str_list = list()
    for doi in dois:
        ref_string_count = int(get_random_index(conf['max_reference_per_paper'])) + 1
        for i in range(ref_string_count):
            ref_style = conf['reference_styles'][get_random_index(reference_style_count)]
            if doi in doi_styles:
                if ref_style in doi_styles[doi]:
                    continue
            else:
                doi_styles[doi] = list()

            ref_str = create_reference_string(dois[doi], ref_style)
            doi_styles[doi].append(ref_style)
            row = [dois[doi], doi, ref_style, ref_str]
            ref_str_list.append(row)

    ref_str_list = generate_typos(ref_str_list)

    try:
        write_reference_data_json(ref_str_list)
    except:
        print("!!!ERROR writing to JSON")
    try:
        write_reference_data_txt(ref_str_list)
    except:
        print("!!!ERROR writing to txt")
    try:
        write_reference_data_csv(ref_str_list)
    except:
        print("!!!ERROR writing to CSV")

    print(ref_str_list)


def get_random_dois(data, document_count):
    paper_count = data["size"]
    sample_dois = data["sample_dois"]
    doi_list = {}
    _id = 0
    for x in range(document_count):
        tmp_ind = get_random_index(paper_count)
        doi = (sample_dois[tmp_ind])
        doi_list[_id] = doi
        sample_dois.remove(doi)
        paper_count -= 1
        _id += 1
        
    return doi_list


def get_random_index(max_num):
    return random.randint(0, max_num - 1)


def create_reference_string(doi, ref_style):
    ref_string = ha.cn.content_negotiation(ids=doi, format="text", style=ref_style)
    return ref_string


def generate_typos(reference_list):
    references_with_typo = reference_list[0: int(len(reference_list) * .10)]

    return new_list


def write_reference_data_csv(rows):
    output = open(conf['output_file_csv'], 'w')
    writer = csv.writer(output)
    writer.writerow(['doi', 'id', 'style', 'reference string'])
    writer.writerows(rows)


def write_reference_data_txt(refs):
    with open(conf['output_file_txt'], 'w') as f:
        for item in refs:
            f.write("%s\n" % str(item))


def write_reference_data_json(data):
    with open(conf['output_file_json'], 'w') as outfile:
        json.dump(data, outfile)


if __name__ == '__main__':
    main()
