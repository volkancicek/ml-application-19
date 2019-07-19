import json
import os
import random
import re
import habanero as ha
import pandas as pd
from config import *


def write_results_to_csv(index):
    start_index = index
    with open(config[input_file], 'r') as f:
        data = json.load(f)
    dois = data["sample_dois"]
    doi_styles = dict()
    reference_style_count = len(config[reference_styles])
    ref_str_list = list()

    doi_count = len(dois)
    for doi_id in range(start_index, doi_count):
        ref_string_count = int(get_random_index(config[max_reference_per_paper])) + 1
        print(str(start_index) + ' ref_string_count ' + str(ref_string_count))
        for i in range(ref_string_count):
            ref_style = config[reference_styles][get_random_index(reference_style_count)]
            if doi_id in doi_styles:
                if ref_style in doi_styles[doi_id]:
                    continue
            else:
                doi_styles[doi_id] = list()

            try:
                ref_str = create_reference_string(dois[doi_id], ref_style)
            except Exception as e:
                print("!!!ERROR calling crossref service for doi: [" + dois[doi_id] + "] " + str(e))
                continue

            doi_styles[doi_id].append(ref_style)
            ''' Create typo for random records ~%10!!! '''
            if get_random_index(100) < 10:
                ref_str = create_typo(ref_str)

            row = [dois[doi_id], doi_id, ref_style, ref_str]
            ref_str_list.append(row)
        if start_index % 20 == 0 or start_index == doi_count - 1:
            df = pd.DataFrame(ref_str_list, columns=['doi', 'id', 'style', 'ref_string'])
            if not os.path.isfile('data/raw/crossref/reference_strings.csv'):
                try:
                    df.to_csv('data/raw/crossref/reference_strings.csv', sep='\t', index=None, header=True)
                except Exception as e:
                    print("!!!ERROR writing to csv" + str(e))
            else:  # else it exists so append without writing the header
                try:
                    df.to_csv('data/raw/crossref/reference_strings.csv', sep='\t', mode='a', index=None, header=False)
                except Exception as e:
                    print("!!!ERROR writing to csv" + str(e))
            ref_str_list = list()
        start_index += 1


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


if __name__ == '__main__':
    write_results_to_csv(0)
