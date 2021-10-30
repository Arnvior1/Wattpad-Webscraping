from typing import Container, Text
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import html5lib
import os
import json
import string
from itertools import product
import lxml
import codecs
import warnings
from requests.api import request  
import requests       
i = string

 

min_len = 9
max_len = 10
character = "0","1","2","3","4","5","6","7","8","9"    

for i in range(min_len,max_len+1):
    for j in product(character, repeat=i):
        word = "".join(j)

        try:                  
            r = requests.get("https://www.wattpad.com/apiv2/info?id=" + word, headers={'User-Agent': 'Mozilla/5.0'})
            soup = BeautifulSoup(r.text)
            all_Titles = soup.prettify().encode('ascii','ignore')
            #all_Titles = soup.find_all("p")
            print(all_Titles)
            # try:
            #     if "<class 'array.array'>" in all_Titles:
            #         all_Titles.pop(0)
            # except:
            #     pass

            # for i in range(len(all_Titles)):
            #     all_text = str(all_text)
            #     text = all_Titles[i].text
            #     text = str(text)
            #     print("----------------------------------------------------" + text)
            #     all_text = all_text + " " + text
            all_text = str(all_Titles)
            # all_text = all_text.split("{")
            # test = str(all_text)
            # print("----------------------" + test + "-----------------------------------------------------------------------------------------------------------")
            # all_text = all_text.pop(-1)
            # all_text = str(all_text)
            # all_text = all_text.split("}")
            # test = str(all_text)
            # print("#+##+#+#+##" + test + "#+#+#+#+##")
            # all_text = all_text.pop(0)
            # all_text = str(all_text)
            # all_text = "{" + all_text + "}"
            print("##############################" + all_text + "#########################")
            ###############################################
            all_text = all_text[29:len(all_text)]
            all_text = str(all_text)
            # all_text = all_text.split("}")
            # all_text = all_text.pop(-1)
            # all_text = str(all_text)
            # all_text = all_text + "}"
            for i in range(27):
                all_text = all_text.rstrip(all_text[-1])
            print("/////////////////////////////////////////" + all_text)
            

            try:
                if all_text != "" or " ":
                    with open(word + ".txt", "w") as f:
                        f.write(all_text)
                        print("hah gespeichert, das wirst du nie wieder los: " + word )
            #     test = open(word + ".txt", "w+")
            #     test = test.read
            #     if test == "" or " " or "  " or "\n":
            #         os.remove(word + ".txt")
            except:
                pass
        finally:
            print(word)
            
print("finished")