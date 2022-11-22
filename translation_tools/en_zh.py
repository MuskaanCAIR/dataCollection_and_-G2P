from distutils.log import error
from time import sleep
from idna import check_initial_combiner
import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
from nltk.corpus import stopwords
# import translators as ts
from googletrans import Translator
import pinyin
import pinyin.cedict as pc
from g2pc import G2pC 
from g2pM import G2pM
from csv import DictWriter
from urllib.error import HTTPError
from scipy.stats import expon



class GenRandDelayExpDist():

    def __init__(self,nsamples,lambda_param=0.2,scale=1):
        self.lambda_param = lambda_param
        self.scale = scale
        self.dist = None 
        self.samples = nsamples
        self.sample = None
        self.__exp()

    def __exp(self):
        
        self.dist = expon(self.scale / self.lambda_param)
        self.sample = self.dist.rvs(self.samples)

    def get_sample(self):
        return(self.sample[0])


class data():

    def __init__(self) -> None:
        pass

    def data_scrape():

        news_url_en = "https://www.rfa.org/english/news/china/beijing-mosque-09132022145624.html"
        # print(news_url_en)
        url_request = requests.get(news_url_en)
        soup = BeautifulSoup(url_request.content, 'html.parser')

        for a in soup.find_all('div', attrs = {'id':'storytext'}):
            print("\n------------THIS IS THE NEWS CORPUS-----------------")
            corpus = a.text
            print (corpus) 
        return corpus

    def data_preprocess():

        #tokenization
        raw_data = data.data_scrape()
        #removing all commas, full stops, quotes, brackets
        comma_data= raw_data.replace(",","")
        stop_data = comma_data.replace(".", "")
        quotes_data = stop_data.replace('"','')
        quotes_data = quotes_data.replace('\'','')
        brackets_data = re.sub(r"[\([{})\]]","", quotes_data)
        #remove double spaces and new lines 
        tokens = ' '.join(brackets_data.split())
        tokens = tokens.split(" ")
        tokens = [x.lower() for x in tokens]
        # print(len(tokens))

        #removing stop words
        stop_words = set(stopwords.words('english'))
        clean_list = []
        for r in tokens:
            if not r in stop_words:
                clean_list.append(r)

        # print(len(clean_list))
        # print(clean_list)

        return clean_list


    # def rest_func():



    def tool1(word):
        
        # tool1: google translator"
        # zh_translation = ts.google(word, from_language='en', to_language='zh')
        # return zh_translation
        while True:
            try:
               
                translator = Translator(service_urls=[
                                'translate.google.com',
                                'translate.google.co.kr',])
                result = translator.translate(word, src='en', dest='zh-cn')
                
                return result.text

                
            except:

                print("----------server error-------------")
                grded_obj = GenRandDelayExpDist(1)
                print("time: ",grded_obj.get_sample())
                sleep(grded_obj.get_sample())
                continue


    def zh_tool2(word):

        #tool2: pinyin
        transliterate = pinyin.get(word, format="numerical", delimiter=" ")
        print(transliterate)
        meanings = pc.translate_word(word)
        return transliterate,meanings                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 

    def g2pc_tool(word):

        g2p = G2pC()
        tone = g2p(word)
        return tone

    def g2pm_tool(word):

        model = G2pM()
        tone2 = model(word,tone=True, char_split=False)
        return tone2


# if __name__ == "__main__":

#     df = pd.DataFrame(columns=['en_word','zh_translate','pypinyin','g2pM'])
#     df.to_csv('en_zh.csv',index=True)
#     field_name = ['','en_word','zh_translate','pypinyin','g2pC_pos','g2pc_pinyin','g2pc_tone','g2pc_meaning','g2pM']
#     word_list = data.data_preprocess()

#     for word in word_list:

#         print("\n-----------google translator-----------")
#         google_translated = data.to_chinese(word)
#         print(f"{word} -----> {google_translated}\n")

#         print("---------pinyin-----------")
#         transliterate, meanings = data.zh_tool2(google_translated)
#         print(f"{google_translated} ----> {transliterate} ----> {meanings}")

#         print(".........g2pc..............")
#         g2pc_result = data.g2pc_tool(google_translated)
#         print(f"{google_translated} ----> {g2pc_result}")

#         print(".........g2pM..............")
#         g2pm_result = data.g2pm_tool(google_translated)
#         print(f"{google_translated} ----> {g2pm_result}")

#         dict = {'':'',
#                 'en_word':word,
#                 'zh_translate':google_translated,
#                 'pypinyin':(transliterate,meanings),
#                 'g2pC_pos':g2pc_result[1],
#                 'g2pc_pinyin':g2pc_result[2],
#                 'g2pc_tone':g2pc_result[3],
#                 'g2pc_meaning':g2pc_result[4],
#                 'g2pM':g2pm_result}

#         with open('en_zh.csv','a') as f:

#             dwriter_object = DictWriter(f, fieldnames=field_name)
#             dwriter_object.writerow(dict)
#             f.close()
