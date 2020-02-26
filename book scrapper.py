from bs4 import BeautifulSoup

import requests
import re
import pandas as pd

urls_visit = [
    "https://techknowledgebooks.com/product-category/mumbai-university/",
    "https://techknowledgebooks.com/product-category/mumbai-university/page/2/",
    "https://techknowledgebooks.com/product-category/mumbai-university/page/3/",
    "https://techknowledgebooks.com/product-category/mumbai-university/page/4/",
    "https://techknowledgebooks.com/product-category/mumbai-university/page/5/",
    "https://techknowledgebooks.com/product-category/mumbai-university/page/6/"]
book = []
book_prizes=[]
for j in urls_visit:
    r = requests.get(
    j).text
    j = BeautifulSoup(r, 'lxml')
    n = list(
    map(str, (j.find_all("div", {"class": "box-text box-text-products"}))))
    test_str = "".join(n)
    title = re.findall("<\s*a[^>]*>(.*?)<\s*/\s*a>", test_str)

    prize = re.findall("<\s*span[^>]*>(.*?)<\s*/\s*span><\s*/\s*span", test_str)
    prizes = [i.split("</span>")[1] for i in prize]
    print(prizes)
    for t in title:
        book.append(t)
    for p in prizes:
        book_prizes.append(p)
print(book)
print(book_prizes)

retailer_give = [(float(i) / 100) * 30 for i in book_prizes]
our_give=[(float(i) / 100) * 35 for i in book_prizes]
users_profit = [abs(j - i) for i, j in zip(retailer_give, our_give)]

retailer_take = [(float(i) / 100) * 75 for i in book_prizes]
our_take = [(float(i) / 100) * 66 for i in book_prizes]
our_loss_to_retailer=[abs(j-i) for i,j in zip(our_take,retailer_take)]
data=[]
for bn, bpr, rg, og,up, rt, ot,ol in zip(book, book_prizes, retailer_give, our_give,users_profit, retailer_take, our_take,our_loss_to_retailer):
    c = []
    c.append(bn)
    c.append(bpr)
    c.append(rg)
    c.append(og)
    c.append(up)
    c.append(rt)
    c.append(ot)
    c.append(ol)
    data.append(c)
col = ["book_name", "book_prize", "retailer_give", "our_give","user_profit", "retailer_take", "our_take","ourloss"]
df = pd.DataFrame(data, columns=col)
df.to_csv("sales.csv")









