# print(j,'"'+'{%'+ ' static' +' "'+ j +'"'+ ' %}'+'"' )
from bs4 import BeautifulSoup
from html.parser import HTMLParser

import sys


ha = open(r"F:\automation scripts\portfoilio\Template\elements.html",
          encoding='utf-8')
soup = BeautifulSoup(ha, 'html.parser')
n = soup.find_all("img")
cs_link = soup.find_all("link")
sc_link = soup.find_all('script')
print(cs_link)

ha.close()
static_path = []


def replace_s(sp):
    with open(r"F:\automation scripts\portfoilio\Template\elements.html", encoding="utf-8") as nw:
        nst = open("newindext.html", "w+", encoding="utf-8")
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



def replace_a_img():
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



# replace_s(static_path)
# j=static_path[0]
replace_s(static_path)
