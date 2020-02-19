# print(j,'"'+'{%'+ ' static' +' "'+ j +'"'+ ' %}'+'"' )
from bs4 import BeautifulSoup
from html.parser import HTMLParser

import sys
import os


static_path = []


def walk_folder():

    for root, d, f in os.walk(r"F:\automation scripts\portfoilio\Template"):
        print(root)
        print("--")
        print(d)
        jh = f
    print(jh)
    try:
        os.mkdir(os.getcwd() + '\\tempdjango')
    except:
        pass

    for df in jh:

        ha = open(r"F:\automation scripts\portfoilio\Template\{}".format(df) ,
                  encoding='utf-8')
        soup = BeautifulSoup(ha, 'html.parser')
        n = soup.find_all("img")
        cs_link = soup.find_all("link")
        sc_link = soup.find_all('script')
        print(cs_link)

        ha.close()
        for j in cs_link:
            static_path.append(j['href'])
            print(j['href'])
        for i in n:
            static_path.append(i['src'])
    # print(static_path)
        print(static_path)
        print(sc_link)
        for s in sc_link:

            try:
                static_path.append(s['src'])
            except:
                pass
        replace_s(static_path,df)


def replace_s(sp,file_name):
    with open(r"F:\automation scripts\portfoilio\Template\{}".format(file_name), encoding="utf-8") as nw:
        nst = open(os.path.join(os.getcwd() + '\\tempdjango',file_name),
                   "w+", encoding="utf-8")
        n = nw.readlines()
        for i in n:
            for j in sp:
                if (i.find(j) == -1):

                    nst.write(i)

                    break
                else:
                    print(" "+'{%' + ' static' + ' "' + j + '"' + ' %}'+" ")
                    jk = i.replace(
                        j, " "+'{%' + ' static' + ' "' + j + '"' + ' %}'+" ")
                    sp.remove(j)

                    nst.write(jk)
                    break

        print("finish")

    pass


def basic_setting():
    m = open(r"F:\automation scripts\ecommerce\ecommerce\settings.py", "r")
    n = m.readlines()
    print(n)
    n.append("""STATICFILES_DIRS=[
        os.path.join(BASE_DIR, "Static"),

    ] """)
    n.append("""\n\b\b STATIC_ROOT=os.path.join(BASE_DIR,'assets')""")
    print(n)
    with open("settings.py", "w") as ns:
        for i in n:
            ns.write(i)

    print(n)


# replace_s(static_path)
# j=static_path[0]
# replace_s(static_path)
walk_folder()
