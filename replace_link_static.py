# print(j,'"'+'{%'+ ' static' +' "'+ j +'"'+ ' %}'+'"' )
from bs4 import BeautifulSoup
from html.parser import HTMLParser

import sys

from shutil import move, copymode
from os import fdopen, remove
ha=open(r"F:\automation scripts\portfoilio\Template\index.html",encoding='utf-8')
soup = BeautifulSoup(ha, 'html.parser')
n = soup.find_all("img")
cs_link=soup.find_all("link")
ha.close()
static_path=[]
def replace_s(sp):
    with open(r"F:\automation scripts\portfoilio\Template\index.html",encoding="utf-8") as nw:
        nst=open("newindext.html","w+",encoding="utf-8")
        n=nw.readlines()
        for i in n :
            for j in sp:
                if( i.find(j) ==-1):

                    break
                else:
                    print(" "+'{%'+ ' static' +' "'+ j +'"'+ ' %}'+" ")
                    jk=i.replace(j," "+'{%'+ ' static' +' "'+ j +'"'+ ' %}'+" " )
                    sp.remove(j)
                    nst.write(jk)
            nst.write(i)


        print("finish")
def replace_a_img():
    pass




for i in n:
    static_path.append(i['src'])
    # print(static_path)

replace_s(static_path)
# j=static_path[0]


























