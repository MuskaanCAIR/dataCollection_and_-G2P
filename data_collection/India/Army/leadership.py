import pandas as pd
import requests
from bs4 import BeautifulSoup
import re


class indianArmedForce():
    
  
    def defence_secretary():

        url = 'https://en.wikipedia.org/wiki/Defence_Secretary_(India)'
        url_request = requests.get(url)
        soup = BeautifulSoup(url_request.text, 'html.parser')
        a = soup.find_all('table', {'class':'wikitable'})
        df = pd.read_html(str(a[1]))
        df = pd.DataFrame(df[0])
        ds_list = df.iloc[:,1]
        # print(fm_list)
        for name in ds_list:
            new = re.sub(r"\([^()]*\)",'', name)
            new_name = new.lower()
            ds_list = list(map(lambda x: x.replace(name, new_name), ds_list))
        print(ds_list)
        return ds_list

    def security_advisor():

        url = 'https://en.wikipedia.org/wiki/National_Security_Advisor_(India)'
        url_request = requests.get(url)
        soup = BeautifulSoup(url_request.text, 'html.parser')
        a = soup.find('table', {'class':'wikitable'})
        df = pd.read_html(str(a))
        df = pd.DataFrame(df[0])
        temp_list = df.iloc[:,1]
        # print(fm_list)
        for name in temp_list:
            new = re.sub(r"\([^()]*\)",'', name)
            new_name = new.lower()
            temp_list = list(map(lambda x: x.replace(name, new_name), temp_list))
        print(temp_list)
        return temp_list


    def chief_of_defence_staff():

        url = 'https://en.wikipedia.org/wiki/Chairman_Chiefs_of_Staff_Committee'
        url_request = requests.get(url)
        soup = BeautifulSoup(url_request.text, 'html.parser')
        a = soup.find('table', {'class':'wikitable'})
        df = pd.read_html(str(a))
        df = pd.DataFrame(df[0])
        temp_list = df.iloc[:,2]
        # print(fm_list)
        for name in temp_list:
            new = re.sub(r"\([^()]*\)",'', name)
            new_name = new.lower()
            temp_list = list(map(lambda x: x.replace(name, new_name), temp_list))
        print(temp_list)
        return temp_list
       
    def chief_of_army_staff():

        url = 'https://en.wikipedia.org/wiki/Chief_of_the_Army_Staff_(India)'
        url_request = requests.get(url)
        soup = BeautifulSoup(url_request.text, 'html.parser')
        a = soup.find_all('table', {'class':'wikitable sortable'})
        df = pd.read_html(str(a[2]))
        df = pd.DataFrame(df[0])
        temp_list = df.iloc[:,2]
        # print(fm_list)
        for name in temp_list:
            new = re.sub(r"\([^()]*\)",'', name)
            new_name = new.lower()
            temp_list = list(map(lambda x: x.replace(name, new_name), temp_list))
        print(temp_list)
        return temp_list
       
    def chief_of_naval_staff():

        url = 'https://en.wikipedia.org/wiki/Chief_of_the_Naval_Staff_(India)'
        url_request = requests.get(url)
        soup = BeautifulSoup(url_request.text, 'html.parser')
        a = soup.find_all('table', {'class':'wikitable sortable'})
        df = pd.read_html(str(a[3]))
        df = pd.DataFrame(df[0])
        temp_list = df.iloc[:,2]
        # print(fm_list)
        for name in temp_list:
            new = re.sub(r"\([^()]*\)",'', name)
            new_name = new.lower()
            temp_list = list(map(lambda x: x.replace(name, new_name), temp_list))
        print(temp_list)
        return temp_list

    
    def chief_of_air_staff():

        url = 'https://en.wikipedia.org/wiki/Chief_of_the_Air_Staff_(India)'
        url_request = requests.get(url)
        soup = BeautifulSoup(url_request.text, 'html.parser')
        a = soup.find_all('table', {'class':'wikitable sortable'})
        df = pd.read_html(str(a[1]))
        df = pd.DataFrame(df[0])
        temp_list = df.iloc[:,2]
        # print(fm_list)
        for name in temp_list:
            new = re.sub(r"\([^()]*\)",'', name)
            new_name = new.lower()
            temp_list = list(map(lambda x: x.replace(name, new_name), temp_list))
        print(temp_list)
        return temp_list
    
    def integrated_defence_staff():

        url = 'https://en.wikipedia.org/wiki/Chief_of_Integrated_Defence_Staff'
        url_request = requests.get(url)
        soup = BeautifulSoup(url_request.text, 'html.parser')
        a = soup.find('table', {'class':'wikitable'})
        df = pd.read_html(str(a))
        df = pd.DataFrame(df[0])
        temp_list = df.iloc[:,2]
        # print(fm_list)
        for name in temp_list:
            new = re.sub(r"\([^()]*\)",'', name)
            new_name = new.lower()
            temp_list = list(map(lambda x: x.replace(name, new_name), temp_list))
        print(temp_list)
        return temp_list

    def general_medical_services():

        url = 'https://en.wikipedia.org/wiki/Director_General_Armed_Forces_Medical_Services_(India)'
        url_request = requests.get(url)
        soup = BeautifulSoup(url_request.text, 'html.parser')
        a = soup.find('table', {'class':'wikitable'})
        df = pd.read_html(str(a))
        df = pd.DataFrame(df[0])
        temp_list = df.iloc[:,1]
        # print(fm_list)
        for name in temp_list:
            new = re.sub(r"\([^()]*\)",'', name)
            new_name = new.lower()
            temp_list = list(map(lambda x: x.replace(name, new_name), temp_list))
        print(temp_list)
        return temp_list

    def serving_admirals():

        lk_members = list()
        url = 'https://en.wikipedia.org/wiki/List_of_serving_admirals_of_the_Indian_Navy'
        url_request = requests.get(url)
        soup = BeautifulSoup(url_request.text, 'html.parser')
        a = soup.find_all('table', {'class':'wikitable'})
        for i in range(len(a)):
            df = pd.read_html(str(a[i]))
            df = pd.DataFrame(df[0])
            temp_list = df.iloc[:,2]
            # print(df)
            for name in temp_list:
                new = re.sub(r"\([^()]*\)",'', name)
                new_name = new.lower()
                print(name)
                lk_members.append(new_name)
        print(lk_members)
        return (lk_members)

    def serving_air_marshals():

        lk_members = list()
        url = 'https://en.wikipedia.org/wiki/List_of_serving_air_marshals_of_the_Indian_Air_Force'
        url_request = requests.get(url)
        soup = BeautifulSoup(url_request.text, 'html.parser')
        a = soup.find_all('table', {'class':'wikitable'})
        for i in range(len(a)):
            df = pd.read_html(str(a[i]))
            df = pd.DataFrame(df[0])
            temp_list = df.iloc[:,2]
            # print(df)
            for name in temp_list:
                new = re.sub(r"\([^()]*\)",'', name)
                new_name = new.lower()
                lk_members.append(new_name)
        print(lk_members)
        return (lk_members)

if __name__ == '__main__':

    dict = {'defence secretary': indianArmedForce.defence_secretary(),
            'chairman chief of defence staff': indianArmedForce.chief_of_defence_staff(),
            'security advisor': indianArmedForce.security_advisor(),
            'chief army staff': indianArmedForce.chief_of_army_staff(),
            'chief naval staff': indianArmedForce.chief_of_naval_staff(),
            'chief air staff': indianArmedForce.chief_of_air_staff(),
            'integrated defence staff': indianArmedForce.integrated_defence_staff(),
            'general medical service': indianArmedForce.general_medical_services(),
            'serving admirals': indianArmedForce.serving_admirals()}

    df = pd.DataFrame.from_dict(dict, orient='index').T

    print(df)
    df.to_csv('leadership.csv')

