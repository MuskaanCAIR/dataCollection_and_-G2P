import os
import sys
from time import sleep
from turtle import begin_fill
import pandas as pd
from csv import DictWriter,writer,reader
import sys
import re
sys.path.insert(0,'/home/cair/Desktop/data/en_to_zh')
from en_zh import data



csv_file_path = '/home/cair/Desktop/data/data_collection/'
csv_file_name = 'entities_start.csv'

def tool_result(tool_function_result, word, tool_name, column_names):

            tool_meaning_dict = {'tool1': {'g2pc': list(), 'pinyin': list()}}
            tool_tones_dict = {'tool1': {'g2pc': list(), 'g2pm': list()}}

            tool_chinese_trans = tool_function_result
            print(f"{word} -----> {tool_chinese_trans}\n")

            print("---------pinyin-----------")
            transliterate, tool_meaning_dict[tool_name]['pinyin'] = data.zh_tool2(tool_chinese_trans)
            x = lambda a: a.split(" ")
            trans_list_pinyin = x(transliterate)
            print(f"translation: {trans_list_pinyin} \n meaning: {tool_meaning_dict[tool_name]['pinyin'] }")

            print("----------------g2pc--------------")
            g2pc_result = data.g2pc_tool(tool_chinese_trans)
            for tups in g2pc_result:

                part_of_speech = tups[1]
                mean = tups[4].split('/')

                #finding first meaning of every tuple in g2pc result     
                if len(mean)==1:
                    new_meaning = None
                else:
                    for strings in mean[1:]:
                        if re.search(u'[\u4e00-\u9fff]', strings):
                            # print(strings)
                            continue
                        else:
                            new_meaning = strings
                            break

                tool_meaning_dict[tool_name]['g2pc'].append(new_meaning)
                tool_tones_dict[tool_name]['g2pc'].append(tups[2])


            print("-----------g2pm----------------")
            tool_tones_dict[tool_name]['g2pm'] = data.g2pm_tool(tool_chinese_trans)
            print(f"{tool_tones_dict[tool_name]['g2pm']}")   

            dict = {'en': word,
                    'zh_correct': '',
                    column_names[0]: tool_chinese_trans,
                    column_names[1]: '',
                    column_names[2]: trans_list_pinyin,
                    column_names[3]: tool_meaning_dict[tool_name]['pinyin'],
                    column_names[4]: part_of_speech,
                    column_names[5]: tool_tones_dict[tool_name]['g2pc'],
                    column_names[6]: tool_meaning_dict[tool_name]['g2pc'],
                    column_names[7]: tool_tones_dict[tool_name]['g2pm']}

            return dict

def dataframe_column_update(tool_name,file_name):

        column_names = ['zh_translate_'+tool_name,
                        'zh_status_'+tool_name,
                        'pinyin_trans_'+tool_name,
                        'pinyin_meaning_'+tool_name,
                        'g2pc_pos_'+tool_name,
                        'g2pc_tones_'+tool_name,
                        'g2pc_meaning_'+tool_name,
                        'g2pm_tone_'+tool_name]

       
        df = pd.read_csv(file_name)
        # df = df.drop('Unnamed: 0',axis=1)
        # print(df)
        for a in column_names:
            # print(a)
            df[a]=''
        df.to_csv(file_name,index=False)
        # print(df) 
        return column_names


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
# field_name = ['en_name',
#             'zh_trans_google',
#             'zh_trans_status',
#             'zh_trans_correct',
#             'zh_trans_pinyin',
#             'zh_g2pc_pos',
#             'zh_meaning(pinyin, g2pc)',
#             'zh_tones(g2pc, g2pm)']

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^main^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
begin_columns = ['en','zh_correct']
df = pd.DataFrame(columns=begin_columns)
df.to_csv(csv_file_name, index=False)

#root directory "data"
root_dir = "/home/cair/Desktop/data/data_collection"
count = 0 
#reading all the subfolders inside the data and 
#gettin all the csv files in them
for folder, subfolder, files in os.walk(root_dir):
    if folder != root_dir and folder not in [csv_file_path+'China',csv_file_path+'Pakistan',csv_file_path+'Nepal']:
        for f in files:
            if f.endswith(".csv"):

                path = os.path.join(folder, f)
                print(f"Path: ",path)
                df = pd.read_csv(path)

                # if folder == '/home/cair/Desktop/data/data_collection/Nepal':
                #     names = df.iloc[7201:,0]
                # else:
                names = df.iloc[:,0]

                #-------------tool setup--------------------------
                col_nm = dataframe_column_update(tool_name='tool1', file_name = csv_file_name)
                
                for word in names:
                    count +=1
                    print('---------------------------')
                    print("folder name: ",folder)
                    print("itteration: ",count)
                    print('---------------------------')
                    tool_dict = tool_result(tool_function_result=data.tool1(word),
                                            word=word,
                                            tool_name='tool1',
                                            column_names=col_nm)

                
                    with open(csv_file_name,'a') as new_f:

                        dwriter_object = DictWriter(new_f, fieldnames=tool_dict.keys())
                        dwriter_object.writerow(tool_dict)
                        new_f.close()   
                            
# dataframe_column_update(tool_name='tool1',file_name=csv_file_name)