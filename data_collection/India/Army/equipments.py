import pandas as pd
import requests
from bs4 import BeautifulSoup
import re

class equipments:

    def __init__(self) -> None:
        pass

    def indian_army_equip():

        ia_list = list()
        url = 'https://en.wikipedia.org/wiki/List_of_equipment_of_the_Indian_Army'
        url_request = requests.get(url)
        soup = BeautifulSoup(url_request.text, 'html.parser')
        a = soup.find_all('table', {'class':'wikitable'})
        for i in range(len(a)):
            df = pd.read_html(str(a[i]))
            df = pd.DataFrame(df[0])
            temp_list = df.iloc[:,0]
            # print(temp_list)
            for name in temp_list:
                # print(name)
                new = re.sub(r"\([^()]*\)",'', name)
                new_name = new.lower()
                ia_list.append(new_name)
        print(len(ia_list))
        print(ia_list)
        return (ia_list)

    def navy_ships():

        ship_list = list()
        url = 'https://en.wikipedia.org/wiki/List_of_active_Indian_Navy_ships'
        url_request = requests.get(url)
        soup = BeautifulSoup(url_request.text, 'html.parser')
        a = soup.find_all('table', {'class':'wikitable'})
        for i in range(len(a)):
            df = pd.read_html(str(a[i]))
            df = pd.DataFrame(df[0])
            temp_list = df.iloc[:,3]
            # print(temp_list)
            for name in temp_list:
                # print(name)
                name = name.replace(u'\xa0',u' ')
                name = name.strip()
                new = re.sub(r"\([^()]*\)",'', name)
                new_name = new.lower()
                ship_list.append(new_name)
        print(len(ship_list))
        print(ship_list)
        return (ship_list)

    def  air_weapons():
        
        weapon_list = list()
        url = 'https://en.wikipedia.org/wiki/List_of_active_Indian_military_aircraft'
        url_request = requests.get(url)
        soup = BeautifulSoup(url_request.text, 'html.parser')
        a = soup.find_all('table', {'class':'wikitable'})
        for i in range(len(a)):
            df = pd.read_html(str(a[i]))
            df = pd.DataFrame(df[0])
            temp_list = df.iloc[:,0]
            # print(temp_list)
            for name in temp_list:
                new = re.sub(r"\([^()]*\)",'', name)
                new_name = new.lower()
                weapon_list.append(new_name)
        print(len(weapon_list))
        print(weapon_list)
        return (weapon_list)

    def historic_aircrafts():

        url = 'https://en.wikipedia.org/wiki/List_of_historical_aircraft_of_the_Indian_Air_Force'
        url_request = requests.get(url)
        soup = BeautifulSoup(url_request.text, 'html.parser')
        a = soup.find('table', {'class':'wikitable sortable'})
        df = pd.read_html(str(a))
        df = pd.DataFrame(df[0])
        temp_list = df.iloc[:,0]
        # print(temp_list)
        for name in temp_list:
            new = re.sub(r"\([^()]*\)",'', name)
            new_name = new.lower()
            temp_list = list(map(lambda x: x.replace(name, new_name), temp_list))
        print(temp_list)
        return temp_list





if __name__ == '__main__':

    dict = {'weapons and tanks':equipments.indian_army_equip(),
            'navy ships': equipments.navy_ships(),
            'air weapons': equipments.air_weapons(),
            'historic aircrafts': equipments.historic_aircrafts()}

    df = pd.DataFrame.from_dict(dict, orient='index').T

    print(df)
    df.to_csv('equipments.csv')