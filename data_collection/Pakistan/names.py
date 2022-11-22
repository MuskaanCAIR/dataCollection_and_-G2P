import requests
import pandas as pd
from bs4 import BeautifulSoup

class pakistan:

    def __init__(self) -> None:
        pass

    def url_1():

        name_list = list()
        url = 'https://angelsname.com/pakistani-names'
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

        page_no = 2
        while(page_no <= 48):
            url_new = url + '/' + str(page_no)
            print(url_new) 
            url_request = url_request = requests.get(url_new)
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
            
            page_no += 1

            print (len(name_list))
        return name_list

    def url_2():

        #---------------------first run-----------------------
        url2_list = list()
        url = 'https://adoption.com/baby-names/origin/Persian'
        url_request = requests.get(url)
        soup = BeautifulSoup(url_request.content, 'html.parser')
        for a in soup.find_all('table', attrs = {'class':'table table-striped table-bordered'}):
            text = a.tbody.text
            lines = text.split("\n\n")
            for name in lines:
                if not name=='':
                    name =  name.split("\n")
                    name = list(filter(None, name))
                    final_name = name[0].split('/')
                    for b in final_name:
                        url2_list.append(b)

        #-------------------next run----------------------------

        # url2_list = list()
        # url = 'https://adoption.com/baby-names/origin/chinese?page='

        # page_no = 2
        # while(page_no <= 5):
        #     new_url = url + str(page_no)
        #     print(new_url)
        #     url_request = requests.get(new_url)
        #     soup = BeautifulSoup(url_request.content, 'html.parser')
        #     for a in soup.find_all('table', attrs = {'class':'table table-striped table-bordered'}):
        #         text = a.tbody.text
        #         lines = text.split("\n\n")
        #         # print(lines)
        #         for name in lines:
        #             if not name=='':
        #                 name =  name.split("\n")
        #                 name = list(filter(None, name))
        #                 final_name = name[0].split('/')
        #                 for b in final_name:
        #                     url2_list.append(b)
        #     page_no += 1 
        #     print(len(url2_list))
        return url2_list 

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
        df.to_csv('adopt_names.csv', mode='a', index=False, header=True)

    
    def file_append(file_1, file_2):

        df1 =  pd.read_csv(file_1)
        print(len(df1))
        df2 = pd.read_csv(file_2)
        print(len(df2))

        df = pd.concat([df1,df2], ignore_index=True)
        new_df = df.groupby(['Names']).sum()
        # print(new_df)
        new_df = new_df.sort_values(by=['frequency'], ascending=False)
        # new_df = new_df.drop('Unnamed: 0',axis=1)
        new_df.to_csv('persian_names.csv')



if __name__ == '__main__':

    # name_list = pakistan.url_2()
    # pakistan.file_create(name_list)

    file_1 = 'names.csv'
    file_2 = 'adopt_names.csv'

    pakistan.file_append(file_1,file_2)