import os

import pandas as pd

from miscellaneous import cermine as cer


def write_result_cermine_csv(index):
    start_index = index
    df = pd.read_csv('data/raw/crossref/reference_strings.csv', sep='\t')
    cermin_list = list()
    end_index = len(df)
    for i in range(start_index, end_index):
        try:
            bibtex_format = cer.call_cermine(df.iloc[i]['ref_string'])
        except Exception as e:
            print("!!!ERROR calling cermin service for doi: [" + df.iloc[i]['doi'] + "] " + str(e))
            continue

        row = [df.iloc[i]['id'], bibtex_format]
        cermin_list.append(row)
        if start_index % 10 == 0 or start_index == end_index - 1:
            df_bib = pd.DataFrame(cermin_list, columns=['id', 'bibtex_string'])
            if not os.path.isfile('data/raw/cermine_result.csv'):
                try:
                    df_bib.to_csv('data/raw/cermine_result.csv', sep='\t', index=None, header=True)
                except Exception as e:
                    print("!!!ERROR writing to csv" + str(e))
            else:  # else it exists so append without writing the header
                try:
                    df_bib.to_csv('data/raw/cermine_result.csv', sep='\t', mode='a', index=None, header=False)
                except Exception as e:
                    print("!!!ERROR writing to csv" + str(e))
            cermin_list = list()
        start_index += 1


if __name__ == '__main__':
    write_result_cermine_csv(0)
