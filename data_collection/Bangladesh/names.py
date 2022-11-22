import requests
import pandas as pd
from bs4 import BeautifulSoup

class bangladesh():

    def __init__(self) -> None:
        pass

    def url_1():

        url_1 = list()
        url = 'https://angelsname.com/bangladeshi-names'
        url_request = url_request = requests.get(url)
        soup = BeautifulSoup(url_request.content, 'html.parser')

        #male
        for a in soup.find_all('a', href=True, id='name-linkm'):
            text = a.text
            name = text.strip()
            url_1.append(name)

        #female
        for a in soup.find_all('a', href=True, id='name-linkf'):
            text = a.text
            name = text.strip()
            url_1.append(name)

        page_no = 2
        while(page_no <= 177):
            url_new = url + '/' + str(page_no)
            print(url_new) 
            url_request = url_request = requests.get(url_new)
            soup = BeautifulSoup(url_request.content, 'html.parser')

            #male
            for a in soup.find_all('a', href=True, id='name-linkm'):
                text = a.text
                name = text.strip()
                url_1.append(name)

            #female
            for a in soup.find_all('a', href=True, id='name-linkf'):
                text = a.text
                name = text.strip()
                url_1.append(name)
            
            page_no += 1

            print (len(url_1))
        return url_1
    
    def url_2():
        #---------------------first run-----------------------
        # name_list = list()
        # url = 'https://adoption.com/baby-names/origin/Afghan'
        # url_request = requests.get(url)
        # soup = BeautifulSoup(url_request.content, 'html.parser')
        # for a in soup.find_all('table', attrs = {'class':'table table-striped table-bordered'}):
        #     text = a.tbody.text
        #     lines = text.split("\n\n")
        #     for name in lines:
        #         if not name=='':
        #             name =  name.split("\n")
        #             name = list(filter(None, name))
        #             final_name = name[0].split('/')
        #             for b in final_name:
        #                 name_list.append(b)

        #-------------------next run----------------------------

        url2_list = list()
        url = 'https://adoption.com/baby-names/origin/Bengali?page='

        page_no = 1
        while(page_no <= 50):
            new_url = url + str(page_no)
            print(new_url)
            url_request = requests.get(new_url)
            soup = BeautifulSoup(url_request.content, 'html.parser')
            for a in soup.find_all('table', attrs = {'class':'table table-striped table-bordered'}):
                text = a.tbody.text
                lines = text.split("\n\n")
                # print(lines)
                for name in lines:
                    if not name=='':
                        name =  name.split("\n")
                        name = list(filter(None, name))
                        final_name = name[0].split('/')
                        for b in final_name:
                            url2_list.append(b)
            page_no += 1 
            print(len(url2_list))
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
        df.to_csv('adoption_names.csv', mode='a', index=False, header=True)

   
    def file_append(file_1, file_2):

        df1 =  pd.read_csv(file_1)
        print(len(df1))
        df2 = pd.read_csv(file_2)
        print(len(df2))

        df = pd.concat([df1,df2], ignore_index=True)
        new_df = df.groupby(['Names']).sum()
        # print(new_df)
        new_df = new_df.sort_values(by=['frequency'], ascending=False)
        new_df = new_df.drop('Unnamed: 0',axis=1)
        new_df.to_csv('bangla_names.csv')


if __name__ == '__main__':

    # name_list = bangladesh.url_2()
    # bangladesh.file_create(name_list)

    file_1 = 'angel_names.csv'
    file_2 = 'adoption_names.csv'

    bangladesh.file_append(file_1,file_2)
    

    