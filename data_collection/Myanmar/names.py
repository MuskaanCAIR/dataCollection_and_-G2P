import requests
import pandas as pd
from bs4 import BeautifulSoup

class myanmar():

    def __init__(self) -> None:
        pass

    def url_1():

        name_list = list()
        url = 'https://angelsname.com/burmese-names'
        url_request = url_request = requests.get(url)
        soup = BeautifulSoup(url_request.content, 'html.parser')

        #male
        for a in soup.find_all('a', href=True, id='name-linkm'):
            text = a.text
            name = text.strip()
            name_list.append(name)

        #female
        for a in soup.find_all('a', href=True, id='name-linkf'):
            text = a.text
            name = text.strip()
            name_list.append(name)

        print (len(name_list))
        return name_list
    

    def file_create(name_list):

        name_list = [x.lower() for x in name_list]
        # print(name_list)
        count_list=list()
        for name in name_list:
            count_list.append(name_list.count(name))
        
        dict={'Names':name_list,'frequency': count_list}
        
        df = pd.DataFrame(dict)
        df = df.groupby('Names').agg({'frequency':'first'}).reset_index()
        df = df.sort_values(by=['frequency'], ascending=False)
        df.to_csv('names.csv', mode='a', index=False, header=True)



if __name__ == '__main__':

    name_list = myanmar.url_1()
    myanmar.file_create(name_list)