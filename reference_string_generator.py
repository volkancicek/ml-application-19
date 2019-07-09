import random
import habanero as ha
import csv
import json
import re
from config import *
from miscellaneous import cermine as cer


def main():
    with open(config[input_file], 'r') as f:
        data = json.load(f)
    dois = get_random_dois(data, config[reference_paper_count])
    doi_styles = dict()
    reference_style_count = len(config[reference_styles])
    ref_str_list = list()
    cermine_results = ''
    for doi_id in dois:
        ref_string_count = int(get_random_index(config[max_reference_per_paper])) + 1
        for i in range(ref_string_count):
            ref_style = config[reference_styles][get_random_index(reference_style_count)]
            if doi_id in doi_styles:
                if ref_style in doi_styles[doi_id]:
                    continue
            else:
                doi_styles[doi_id] = list()

            ref_str = create_reference_string(dois[doi_id], ref_style)
            doi_styles[doi_id].append(ref_style)
            ''' Create typo for random records ~%10!!! '''
            if get_random_index(100) < 10:
                ref_str = create_typo(ref_str)
            ''' ['doi', 'doi id', 'style', 'reference string'] '''
            if int(config[cermine_active]) > 0:
                cermine_results += cer.call_cermine(ref_str)

            row = [dois[doi_id], doi_id, ref_style, ref_str]
            ref_str_list.append(row)

    write_results(ref_str_list, cermine_results)


def write_results(ref_str_list, cermine_result):
    try:
        if int(config[cermine_active]) > 0:
            write_cermine_txt(cermine_result)
    except Exception as e:
        print("!!!ERROR writing cermine text"+str(e))
    try:
        write_reference_data_json(ref_str_list)
    except Exception as e:
        print("!!!ERROR writing to JSON"+str(e))
    try:
        write_reference_data_txt(ref_str_list)
    except Exception as e:
        print("!!!ERROR writing to txt"+str(e))
    try:
        write_reference_data_csv(ref_str_list)
    except Exception as e:
        print("!!!ERROR writing to CSV"+str(e))


def get_random_dois(data, document_count):
    paper_count = data["size"]
    sample_dois = data["sample_dois"]
    doi_list = {}
    _id = 1
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
    # for rem in ['doi\:10\..*',
    #             'Available at: http://dx.doi.org/.*',
    #             'Available from: http://dx.doi.org/.*',
    #             'Crossref. Web.',
    #             '[^ ]*doi\.org/10\.[^ ]*',
    #             '[^ ]*' + doi[:5] + '[^ ]*']:
    #     ref_string = re.sub(rem, '', ref_string)
    ref_string = re.sub(' +', ' ', ref_string)
    ref_string = re.sub('\n', ' ', ref_string)
    return ref_string.strip()


def create_typo(s):
    words = s.split()
    for word in words:
        if len(word) > 5 and word.isalpha():
            w = change_last_character(word)
            words[words.index(word)] = w
            s = ' '.join(words)
            return s

    return s


def change_last_character(s):
    s += s[-1:]
    return s


def write_reference_data_csv(rows):
    output = open(config[output_file_csv], 'w')
    writer = csv.writer(output)
    writer.writerow(['doi', 'id', 'style', 'reference string'])
    writer.writerows(rows)


def write_reference_data_txt(refs):
    with open(config[output_file_txt], 'w') as f:
        for item in refs:
            try:
                f.write("%s\n" % str(item))
            except:
                print("!!!ERROR writing to txt" + str(item))
                continue


def write_reference_data_json(data):
    with open(config[output_file_json], 'w') as outfile:
        json.dump(data, outfile)


def write_cermine_txt(txt):
    with open(config[cermine_result], 'wb') as f:
        f.write(txt.encode('utf8'))


if __name__ == '__main__':
    main()
