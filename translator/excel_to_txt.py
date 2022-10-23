import os
import pandas as pd
from glob import glob


def write_file(text_list, save_path):
    with open(save_path, 'w', encoding='utf-8') as f:
        for text in text_list:
            f.write(text+ '\n')
    f.close()
    return None


def main():
    path = '../data/translate'
    flist = glob(f'{path}/*.xlsx')
    # print(flist)
    for file in flist:
        fname = file.split('/')[-1].split('.')[0]
        df = pd.read_excel(file)
        df = df.iloc[:, -2:]
        print(df.columns)
        try:
            df.columns = ['src', 'tgt']
            text = [str(df['src'][i]) + '\t' + str(df['tgt'][i]) for i in range(len(df))]
            write_file(text, f'../data/translate/{fname}.txt')
        except Exception as e:
            print(e)
            print(fname)

if __name__ == '__main__':
    main()