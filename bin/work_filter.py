import pandas as pd
import re

# Todo ,/s[A-Z] 일때 앞에서 split
# REF 가 포함된 문장 확인후 delete 컬럼 추가하여 표기

if __name__ == '__main__':
    df = pd.read_excel('../data/work/pdfdoc_to_txt_20221114.xlsx')
    print(df.head())

    comma_upper = []
    split_lines, filenames_list = [], []
    for i in range(len(df)):
        if len(re.findall('\.\s[A-Z]', df['text'][i])) > 0:
            comma_upper.append(i)
            split_text = re.split('(?=\.\s[A-Z])', df['text'][i])
            for t in split_text:
                try:
                    if t[0] == '.':
                        t = t[2:]
                        split_lines.append(t)
                        filenames_list.append(df['filename'][i])
                    else:
                        t = t + '.'
                        split_lines.append(t)
                        filenames_list.append(df['filename'][i])
                except:
                    pass
    drop_df = df.drop(comma_upper)
    split_df = pd.DataFrame({'filename': filenames_list, 'text':split_lines})
    print(len(df))
    df = pd.concat([drop_df, split_df], axis=0)
    print(len(df))
    df.reset_index(inplace=True, drop=True)
    delete_idx = []
    delete_bool = []
    for j in range(len(df)):
        if len(re.findall('(REF\s)', df['text'][j])) > 0:
            delete_idx.append(j)
            delete_bool.append('T')
        else:
            # delete_idx.append(j)
            delete_bool.append('F')
    df['delete'] = delete_bool
    print(df.head())
    print(len(df))

    drop_idx = [x for x in range(len(df)) if len(re.findall('[a-zA-Z]', str(df['text'][x]))) > 0]
    print(len(drop_idx))
    df = df.loc[drop_idx]
    # df = df.sort_values(['filename'])
    print(df.head())
    df.to_csv('../data/work/pdfdoc_to_txt_20221115.csv', index=False, encoding='utf-8-sig')

