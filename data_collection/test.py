# import os

# root_dir = "/home/cair/Desktop/data/data_collection"

# for folder, subfolder, files in os.walk(root_dir):
    
#     if folder != root_dir and folder != '/home/cair/Desktop/data/data_collection/India/Army':
#         print(folder)
#         for f in files:
#             if f.endswith(".csv"):

#                 if folder == "/home/cair/Desktop/data/data_collection/Nepal":
#                     print("found")

import pandas as pd

# df = pd.read_csv('entities4_nepal_(copy).csv')
# columns = ['zh_translate_tool1',
#                     'zh_status_tool1',
#                     'pinyin_trans_tool1',
#                     'pinyin_meaning_tool1',
#                     'g2pc_pos_tool1',
#                     'g2pc_tones_tool1',
#                     'g2pc_meaning_tool1',
#                     'g2pm_tone_tool1']

# df = df.dropna(thresh=2)
# df.to_csv('entities4.csv')
# print(df.head())

# df1 = pd.read_csv('entities.csv')
# print(df1.shape[0])
# df2 = pd.read_csv('entities2.csv')
# print(df2.shape[0])
df3 = pd.read_csv('/home/cair/Desktop/data/data_extraction/entities_complete2.csv')
print(df3.shape[0])
df4 = pd.read_csv('/home/cair/Desktop/data/translation_tools/entities_china.csv')
print(df4.shape[0])

pd.concat([df3, df4]).to_csv('/home/cair/Desktop/data/data_extraction/entities_complete2.csv', index=False)

df5 = pd.read_csv('/home/cair/Desktop/data/data_extraction/entities_complete2.csv')
print(df5.shape[0])