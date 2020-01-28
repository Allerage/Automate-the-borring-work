from mlxtend.frequent_patterns import apriori
from mlxtend.preprocessing import TransactionEncoder
import pandas as pd
import random
import os
from os import path
import collections
def product_re():
    df = pd.read_csv('product.csv')
    pps = df['Product_search'].apply(lambda x: x.split(','))
    #print (pps)
    te = TransactionEncoder()
    te_ary = te.fit(pps).transform(pps)#convert the data in boolean matrix
    #print(te_ary)
    mpp = pd.DataFrame(te_ary, columns=te.columns_)

    frequent_ps = apriori(mpp, min_support=0.03, use_colnames=True)# used for getting the pattern of frequent  search performed by user

    frequent_ps['length'] = frequent_ps['itemsets'].apply(lambda x: len(x))
    items = frequent_ps[(frequent_ps['length'] >= 2) &
                              (frequent_ps['support'] >= 0.04)]
    P = items['itemsets']
    #print(P) #get most popular items
def user_speci_rec():
    n=input("Enter the user {} ".format(['A','B','C','D'])).upper()
    w=os.getcwd() # get path os current working directory
    df=pd.read_csv(os.path.join(w,"product.csv"))
    user=df.values.tolist()
    j=[i[2].split(',') for i in user if i[1]==n] # get product serch
    #print(j)
    df1=pd.DataFrame(j)
    #print(df1)


    te = TransactionEncoder()
    te_ary = te.fit(j).transform(j)
    # print(te_ary)
    df1 = pd.DataFrame(te_ary, columns=te.columns_)

    frequent_us = apriori(df1, min_support=0.03, use_colnames=True)

    frequent_us['length'] = frequent_us['itemsets'].apply(lambda x: len(x))
    items = frequent_us[(frequent_us['length'] >= 2) &
                              (frequent_us['support'] >= 0.04)]
    pattern_set = items['itemsets'] # set of frequent pattern discoverd
    rec_p_to_user=[j for i in pattern_set for j in list(i)]
    m=dict(collections.Counter(rec_p_to_user))
    pr=max(m,key=m.get)
    #print(pr)
    print("product pattern found for User {} {} ".format(n,pattern_set))
    print("Product Most Likely product to  be recommend to user {} is {}".format(n,pr))



def create_data_set(): #fuction to create a dummy dataset that represent the search made by user and save in csv
    print("Creating dataset")
    users=['A','B','C','D']
    c=['User','Product_search']

    products=["Iphone",'Samsung','Milk','Butter','Alienware','Oneplus','Almonds']
    data_u=[]


    for i in range(1000):
        j=random.choice(range(5,10))
        u=random.choice(users)
        product_sear=[]
        for k in range(j):
            pro=random.choice(products)
            product_sear.append(pro)
        data_u.append((u,",".join(product_sear)))

    df=pd.DataFrame(columns=c,data=data_u)
    wd=os.getcwd()
    if path.exists(os.path.join(wd,'product.csv')):
        os.remove(os.path.join(wd,"product.csv"))
    df.to_csv("product.csv")
    print("dataset Created ..")
create_data_set()


user_speci_rec()
# product_re() get most famous product of shop






