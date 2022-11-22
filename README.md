# PROJECT TILE

Data collection using web scraping and analysis of different chinese phonetic tools for transliteration

# PROJECT DESCRIPTION

The project is divided into 3 parts :

1.  first part deals with collecting data of different neighbouring countries of India using web scraping with the help of **beautifulsoup** tool. All the datas are stored in the respective country folder in the form of .csv file. The total size of the data is roughly around 5 MB.

2.  This was followed by the analysis of different phonetic tools for chinese language. The tools taken into account are: 
    1. pinyin
    2. g2pC
    3. g2pM
    Every word in the 5 MB data collected in english is translated to chinese using **googletrans** API and the translation is passed as an input to each of the above mentioned tools. The result of every word is stored in one mega .csv file.

3. the result of the above steps can viewed in sample as desired by the user. The user will be given a choice of random selection of data (which could include improper results by the tools) or selection of only those datas which have proper results by the tools.

# TABLE OF CONTENT

1. How to install and run the project
2. How to use the project
    1. For data collection only
    2. For analysis of different tools
    3. For extracting a sample from the dataset
3. Overview of the data collected and created
4. Issues faced while working with **googletrans**  
5. Resolving the issue
6. Credits 

# 1. Running the project

For two parts of the project i.e, data_collection and translation, there is a setup.sh file in the respective directories which creates and activates a conda virtual environment and installs all the required packages for each part of the project. Change the present working directory to the required directory and run any one of the following commands:
                                                ./setup.sh
                                                sh setup.sh
                                                bash setup.sh

**Important**: please do not run the project on your preinstalled python package as it might give error while running g2pc and g2pm models. Follow the above instructions for uninterrupted performance.

# 2. How to use the project:

As mentioned in the description, the project is divided into three parts.

    1. The first part (data collection) is handled by **data_collection** directory
    you can collect human names for any one of the following countries:
        China, Bhutan, Nepal, Pakistan, Bangladesh, Myanmar, Maldives, Sri Lanka and India.
    Note: For India the data_collection is further extended to political personalities and army equipments and leaders.
    Change the present working directory to the required COUNTRY directory and run _python names.py_

    2. The translation part is handled by **translation_tools** directory.
    There are two files: 
            *en_to_zh_entities.py* : iterates over directories and produces results and converts it to csv
            *en_zh.py* : contains functions of all the translation tools
    Change the present working directory to this directory and run *python en_to_zh_entities.py*
    This will start translating all the datas collected in the first part.
    *working*
    This python file walks through all the directories inside the *data_collection* directory in random order and reads only the .csv files which contains the words to be translated.
    If you want to translate data of only one of the countries, specifiy the folder name in **line no: 115** of the *en_to_zh_entities.py* file.
    			for example: if you want to run this only for China: change line 115 to:
    							if folder != root_dir and folder == 'China':

    3. Finally, to extract data from the translated .csv file switch to *data_extraction* folder
    Run *python data_extraction.py* file.
    User will be asked to input the desired number of rows which they want to extract from the main translated .csv file followed by an option to choose whether they want random rows* or only the rows with proper translated output.

    **random row selection means that rows with improper output i.e, where no translation results where generated, will also be included*

# 4. Issue faced with googletrans:

Googletrans allows only 2000 continues translation to occur at one run. Any further translation attempt will produce a connection or https error.

# 5. Solution to the problem:

After 2000 translations, when the API throws an error, it is excepted using try, except method of python and the program is made to sleep for exponential amount of time. Exponential functions kind of mimics a human and chooses a random non-patterned value which is not understood by the API thus preventing it from blocking our IP address.
This function is written in *en_zh.py* file in translation_tools directory
