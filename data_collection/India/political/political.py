from operator import le
import pandas as pd
import requests
from bs4 import BeautifulSoup
import re

class political:

    def __init__(self) -> None:
        pass

    def president():

        president_list = list()
        url = 'https://www.careerpower.in/list-of-presidents-of-india.html'
        url_request = requests.get(url)
        soup = BeautifulSoup(url_request.content, 'html.parser')
        for a in  soup.find_all('tr'):
            name = a.td.text
            name = name.lower()
            president_list.append(name[3:])
        president_list.remove(president_list[0])
        print(president_list)
        return president_list

    def vice_president():
       
        url = 'https://en.wikipedia.org/wiki/List_of_vice_presidents_of_India'
        url_request = requests.get(url)
        soup = BeautifulSoup(url_request.text, 'html.parser')
        a = soup.find('table', {'class':'wikitable sortable'})
      
        df = pd.read_html(str(a))
        df = pd.DataFrame(df[0])
        vp_list = df['Name (Birth–Death)', 'Name (Birth–Death)']
        for name in vp_list:
            new = re.sub(r"\([^()]*\)",'', name)
            new_name = new.lower()
            vp_list = list(map(lambda x: x.replace(name, new_name), vp_list))
        vp_list.remove(vp_list[0])
        print(vp_list)
        return vp_list
    
    def prime_minister():

        url = 'https://en.wikipedia.org/wiki/List_of_prime_ministers_of_India'
        url_request = requests.get(url)
        soup = BeautifulSoup(url_request.text, 'html.parser')
        a = soup.find('table', {'class':'wikitable sortable'})
                
        df = pd.read_html(str(a))
        df = pd.DataFrame(df[0])
        pm_list = df.iloc[:,1]
        # print(pm_list)
        for name in pm_list:
            new = re.sub(r"\([^()]*\)",'', name)
            new_name = new.lower()
            pm_list = list(map(lambda x: x.replace(name, new_name), pm_list))
        print(pm_list)
        return pm_list

    def governors():

        url = 'https://en.wikipedia.org/wiki/List_of_current_Indian_governors'
        url_request = requests.get(url)
        soup = BeautifulSoup(url_request.text, 'html.parser')
        a = soup.find('table', {'class':'sortable wikitable'})
                
        df = pd.read_html(str(a))
        df = pd.DataFrame(df[0])
        g_list = df.iloc[:,1]
        # print(g_list)
        for name in g_list:
            new = re.sub(r"\([^()]*\)",'', name)
            new_name = new.lower()
            g_list = list(map(lambda x: x.replace(name, new_name), g_list))
        print(g_list)
        return g_list

    def deputy_pm():

        d_pm_list = ['Vallabhbhai Patel' ,
                    'Morarji Desai',
                    'Charan Singh',
                    'Jagjivan Ram',
                    'Yashwantrao Chavan',
                    'Devi Lal',
                    'Lal Krishna Advani']
        dpm_list = [x.lower() for x in d_pm_list]
        print(dpm_list)
        return dpm_list

    def chief_justice():

        url = 'https://en.wikipedia.org/wiki/List_of_chief_justices_of_India'
        url_request = requests.get(url)
        soup = BeautifulSoup(url_request.text, 'html.parser')
        a = soup.find('table', {'class':'nowraplinks'})
        name = a.td.text
        cj_list = name.split('\n')
        cj_list = [x.lower() for x in cj_list]
        cj_list.remove(cj_list[0])
        print(cj_list)
        return cj_list

    def speakers_ls():

        url = 'https://en.wikipedia.org/wiki/Speaker_of_the_Lok_Sabha'
        url_request = requests.get(url)
        soup = BeautifulSoup(url_request.text, 'html.parser')
        a = soup.find('table', {'class':'wikitable'})
        
        df = pd.read_html(str(a))
        df = pd.DataFrame(df[0])
        speaker_list = df.iloc[:,2]
        print(speaker_list)
        for name in speaker_list:
            new = re.sub(r"\([^()]*\)",'', name)
            new_name = new.lower()
            speaker_list = list(map(lambda x: x.replace(name, new_name), speaker_list))
        speaker_list = list(set(speaker_list))
        print(speaker_list)
        return speaker_list

    def chief_minister():

        url = 'https://en.wikipedia.org/wiki/List_of_current_Indian_chief_ministers'
        url_request = requests.get(url)
        soup = BeautifulSoup(url_request.text, 'html.parser')
        a = soup.find('table', {'class':'wikitable'})
        
        df = pd.read_html(str(a))
        df = pd.DataFrame(df[0])
        cm_list = df.iloc[:,1]
        # print(cm_list)
        for name in cm_list:
            new = re.sub(r"\([^()]*\)",'', name)
            new_name = new.lower()
            cm_list = list(map(lambda x: x.replace(name, new_name), cm_list))
        cm_list = list(set(cm_list))
        print(cm_list)
        return cm_list

    def bharat_ratna():

        url = 'https://en.wikipedia.org/wiki/Bharat_Ratna'
        url_request = requests.get(url)
        soup = BeautifulSoup(url_request.text, 'html.parser')
        a = soup.find_all('table', {'class':'wikitable'})
        
        df = pd.read_html(str(a[1]))
        df = pd.DataFrame(df[0])
        br_list = df.iloc[:,2]
        print(br_list)
        for name in br_list:
            new = re.sub(r"\([^()]*\)",'', name)
            new_name = new.lower()
            br_list = list(map(lambda x: x.replace(name, new_name), br_list))
        print(br_list)
        return br_list
        

    def sc_judges():

        url = 'https://en.wikipedia.org/wiki/List_of_sitting_judges_of_the_Supreme_Court_of_India'
        url_request = requests.get(url)
        soup = BeautifulSoup(url_request.text, 'html.parser')
        a = soup.find_all('table', {'class':'wikitable'})
            
        df = pd.read_html(str(a))
        df = pd.DataFrame(df[0])
        sc_list = df.iloc[:,2]
        print(sc_list)
        for name in sc_list:
            new = re.sub(r"\([^()]*\)",'', name)
            new_name = new.lower()
            sc_list = list(map(lambda x: x.replace(name, new_name), sc_list))
        print(sc_list)
        return sc_list

    def chief_election_commissioners():

        url = 'https://en.wikipedia.org/wiki/Chief_Election_Commissioner_of_India'
        url_request = requests.get(url)
        soup = BeautifulSoup(url_request.text, 'html.parser')
        a = soup.find_all('table', {'class':'wikitable'})
        # print(a[1])
        df = pd.read_html(str(a[1]))
        df = pd.DataFrame(df[0])
        cec_list = df.iloc[:,1]
        # print(df)
        for name in cec_list:
            new = re.sub(r"\([^()]*\)",'', name)
            new_name = new.lower()
            cec_list = list(map(lambda x: x.replace(name, new_name), cec_list))
        print(cec_list)
        return cec_list

    def attorney_generals():
        
        url = 'https://en.wikipedia.org/wiki/Attorney-General_for_India'
        url_request = requests.get(url)
        soup = BeautifulSoup(url_request.text, 'html.parser')
        a = soup.find_all('table', {'class':'wikitable'})
        # print(a[1])
        df = pd.read_html(str(a[1]))
        df = pd.DataFrame(df[0])
        ag_list = df.iloc[:,1]
        # print(df)
        for name in ag_list:
            new = re.sub(r"\([^()]*\)",'', name)
            new_name = new.lower()
            ag_list = list(map(lambda x: x.replace(name, new_name), ag_list))
        ag_list = list(set(ag_list))
        print(ag_list)
        return ag_list

    def defence_ministers():

        url = 'https://en.wikipedia.org/wiki/Minister_of_Defence_(India)'
        url_request = requests.get(url)
        soup = BeautifulSoup(url_request.text, 'html.parser')
        a = soup.find('table', {'class':'wikitable'})
        # print(a[1])
        df = pd.read_html(str(a))
        df = pd.DataFrame(df[0])
        dm_list = df.iloc[:,2]
        # print(df)
        for name in dm_list:
            new = re.sub(r"\([^()]*\)",'', name)
            new_name = new.lower()
            dm_list = list(map(lambda x: x.replace(name, new_name), dm_list))
        print(dm_list)
        return dm_list

    def education_minister():

        url = 'https://en.wikipedia.org/wiki/Minister_of_Education_(India)'
        url_request = requests.get(url)
        soup = BeautifulSoup(url_request.text, 'html.parser')
        a = soup.find('table', {'class':'wikitable'})
        # print(a[1])
        df = pd.read_html(str(a))
        df = pd.DataFrame(df[0])
        em_list = df.iloc[:,1]
        # print(df)
        for name in em_list:
            new = re.sub(r"\([^()]*\)",'', name)
            new_name = new.lower()
            em_list = list(map(lambda x: x.replace(name, new_name), em_list))
        print(em_list)
        return em_list
    
    def external_affairs_minister():

        url = 'https://en.wikipedia.org/wiki/Minister_of_External_Affairs_(India)'
        url_request = requests.get(url)
        soup = BeautifulSoup(url_request.text, 'html.parser')
        a = soup.find('table', {'class':'wikitable'})
        # print(a[1])
        df = pd.read_html(str(a))
        df = pd.DataFrame(df[0])
        exm_list = df.iloc[:,2]
        # print(df)
        for name in exm_list:
            new = re.sub(r"\([^()]*\)",'', name)
            new_name = new.lower()
            exm_list = list(map(lambda x: x.replace(name, new_name), exm_list))
        print(exm_list)
        return exm_list

    
    def finance_minister():

        url = 'https://en.wikipedia.org/wiki/Minister_of_Finance_(India)'
        url_request = requests.get(url)
        soup = BeautifulSoup(url_request.text, 'html.parser')
        a = soup.find('table', {'class':'wikitable'})
        # print(a[1])
        df = pd.read_html(str(a))
        df = pd.DataFrame(df[0])
        fm_list = df.iloc[:,2]
        fm_list = fm_list[:42]
        # print(fm_list)
        for name in fm_list:
            new = re.sub(r"\([^()]*\)",'', name)
            new_name = new.lower()
            fm_list = list(map(lambda x: x.replace(name, new_name), fm_list))
        print(fm_list)
        return fm_list

    def home_minister():

        url = 'https://en.wikipedia.org/wiki/Minister_of_Home_Affairs_(India)'
        url_request = requests.get(url)
        soup = BeautifulSoup(url_request.text, 'html.parser')
        a = soup.find('table', {'class':'wikitable'})
        # print(a[1])
        df = pd.read_html(str(a))
        df = pd.DataFrame(df[0])
        hm_list = df.iloc[:,2]
        # hm_list = fm_list[:42]
        # print(fm_list)
        for name in hm_list:
            new = re.sub(r"\([^()]*\)",'', name)
            new_name = new.lower()
            hm_list = list(map(lambda x: x.replace(name, new_name), hm_list))
        print(hm_list)
        return hm_list

    
    def justice_minister():

        url = 'https://en.wikipedia.org/wiki/Minister_of_Law_and_Justice'
        url_request = requests.get(url)
        soup = BeautifulSoup(url_request.text, 'html.parser')
        a = soup.find('table', {'class':'wikitable'})
        # print(a[1])
        df = pd.read_html(str(a))
        df = pd.DataFrame(df[0])
        jm_list = df.iloc[:,2]
        # print(fm_list)
        for name in jm_list:
            new = re.sub(r"\([^()]*\)",'', name)
            new_name = new.lower()
            jm_list = list(map(lambda x: x.replace(name, new_name), jm_list))
        print(jm_list)
        return jm_list


    def railway_minister():

        url = 'https://en.wikipedia.org/wiki/Minister_of_Railways_(India)'
        url_request = requests.get(url)
        soup = BeautifulSoup(url_request.text, 'html.parser')
        a = soup.find('table', {'class':'wikitable'})
        # print(a[1])
        df = pd.read_html(str(a))
        df = pd.DataFrame(df[0])
        rm_list = df.iloc[:,2]
        # print(fm_list)
        for name in rm_list:
            new = re.sub(r"\([^()]*\)",'', name)
            new_name = new.lower()
            rm_list = list(map(lambda x: x.replace(name, new_name), rm_list))
        print(rm_list[:len(rm_list)-1])
        return rm_list[:len(rm_list)-1]

    def road_minister():

        url = 'https://en.wikipedia.org/wiki/Ministry_of_Road_Transport_and_Highways'
        url_request = requests.get(url)
        soup = BeautifulSoup(url_request.text, 'html.parser')
        a = soup.find_all('table', {'class':'wikitable'})
        # print(a[1])
        df = pd.read_html(str(a[2]))
        df = pd.DataFrame(df[0])
        roadm_list = df.iloc[:,2]
        # print(df)
        for name in roadm_list:
            new = re.sub(r"\([^()]*\)",'', name)
            new_name = new.lower()
            roadm_list = list(map(lambda x: x.replace(name, new_name), roadm_list))
        print(roadm_list)
        return roadm_list


    def members_of_lokSabha():

        lk_members = list()
        url = 'https://en.wikipedia.org/wiki/List_of_members_of_the_17th_Lok_Sabha'
        url_request = requests.get(url)
        soup = BeautifulSoup(url_request.text, 'html.parser')
        a = soup.find_all('table', {'class':'wikitable sortable'})
        for i in range(len(a)):
            df = pd.read_html(str(a[i]))
            df = pd.DataFrame(df[0])
            temp_list = df.iloc[:,2]
            # print(df)
            for name in temp_list:
                new = re.sub(r"\([^()]*\)",'', name)
                new_name = new.lower()
                lk_members.append(new_name)
        print(len(lk_members))
        print(lk_members)
        return (lk_members)


class businessman():

    def __init__(self) -> None:
        pass

    def names():

        url = 'https://en.wikipedia.org/wiki/List_of_Indians_by_net_worth'
        url_request = requests.get(url)
        soup = BeautifulSoup(url_request.text, 'html.parser')
        a = soup.find('table', {'class':'wikitable sortable'})
      
        df = pd.read_html(str(a))
        df = pd.DataFrame(df[0])
        rich_peeps_list = df.iloc[:,1]
        print(rich_peeps_list)
        for name in rich_peeps_list:
            new = re.sub(r"\([^()]*\)",'', name)
            new_name = new.lower()
            rich_peeps_list = list(map(lambda x: x.replace(name, new_name), rich_peeps_list))

        print(rich_peeps_list)
        return rich_peeps_list
    



if __name__ == '__main__':

    # political.vice_president()
    # political.prime_minister()
    # political.deputy_pm()
    # political.chief_justice()
    # political.speakers_ls()
    # political.chief_minister()
    # political.bharat_ratna()
    # political.sc_judges()
    # businessman.names()

    dict = {'president': political.president(),
            'vice-president': political.vice_president(),
            'prime-minister': political.prime_minister(),
            'governors': political.governors(),
            'deputy prime minister': political.deputy_pm(),
            'chief minister': political.chief_minister(),
            'chief justice': political.chief_justice(),
            'speaker': political.speakers_ls(),
            'bharat ratna':political.bharat_ratna(),
            'sc_judges': political.sc_judges(),
            'businessmen':businessman.names(),
            'election commissioners':political.chief_election_commissioners(),
            'attorney generals': political.attorney_generals(),
            'defence minister': political.defence_ministers(),
            'education ministers': political.education_minister(),
            'external affairs ministers': political.external_affairs_minister(),
            'finance minister': political.finance_minister(),
            'home ministers': political.home_minister(),
            'law & justice minister': political.justice_minister(),
            'railway minister': political.railway_minister(),
            'road and highways ministers': political.road_minister(),
            'lok sabha members': political.members_of_lokSabha()}

    df = pd.DataFrame.from_dict(dict, orient='index').T

    print(df)
    df.to_csv('important_personalities.csv')


