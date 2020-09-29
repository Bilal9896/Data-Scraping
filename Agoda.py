import mysql.connector
from mysql.connector import Error
import requests
from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import request
import re
import urllib 
from urllib.request import Request, urlopen
import sys
from PIL import Image
import base64
from io import StringIO
import PIL.Image
from mysql.connector import Error
from mysql.connector import errorcode
from multiprocessing import Pool
import time
options = webdriver.FirefoxOptions()
options.add_argument('-headless')
options.add_argument('--no-sandbox') # Bypass OS security model
options.add_argument('--disable-gpu')  # applicable to windows os only
options.add_argument('start-maximized') # 
options.add_argument('disable-infobars')
options.add_argument("--disable-extensions")
options.add_argument("--incognito")
options.add_argument("--disable-impl-side-painting")
options.add_argument("--disable-setuid-sandbox")
options.add_argument("--disable-seccomp-filter-sandbox")
options.add_argument("--disable-breakpad")
options.add_argument("--disable-client-side-phishing-detection")
options.add_argument("--disable-cast")
options.add_argument("--disable-cast-streaming-hw-encoding")
options.add_argument("--disable-cloud-import")
options.add_argument("--disable-popup-blocking")
options.add_argument("--ignore-certificate-errors")
options.add_argument("--disable-session-crashed-bubble")
options.add_argument("--disable-ipv6")
options.add_argument("--allow-http-screen-capture")
options.add_argument("--start-maximized")
filename="Product List.csv"
f = open(filename, "a")
headers = "Product_url\n"
f.write(headers+"\n")
localtime = time.asctime( time.localtime(time.time()) )
print (localtime)
f.write(localtime+"\n")
i=0
try:
    connection = mysql.connector.connect(host="166.62.28.141",database="beebay",user="bilal",password="bilalshah",port=3306)
    cursor = connection.cursor(prepared=True)
    sql_select_query = """ SELECT * FROM optinex_product_details"""
    result  = cursor.execute(sql_select_query)
    total_products=cursor.fetchall()
    connection.commit()
    print ("Total Number of Rows: ",cursor.rowcount)
    sql_select_query_url1=""" SELECT url FROM optinex_product_details WHERE store_id='19' AND id >='3831' """
    result  = cursor.execute(sql_select_query_url1)
    records6=cursor.fetchall()
    connection.commit()
    print ("Total Number of Rows: ",cursor.rowcount)
    for row in records6:
        existing_price=''
        price=''
        localtime = time.asctime( time.localtime(time.time()) )
        print (localtime)
        url=row[0].decode()
        print(url)
        if url is None:
            print("Product has no url please check databse table name Product details")
        else:
            try:
                driver = webdriver.Firefox(options=options)
                driver.get(url)
                response = requests.get(url)
                soup = BeautifulSoup(driver.page_source,'html5lib')
                product_price=soup.find('div',{'class':'PriceRibbon'})
                print(product_price)
                if product_price:
                    new_price=product_price.find('span',{'class':'PriceRibbon__Price'}).text.strip()
                    new_price=new_price.replace('Rs','')
                    new_price=new_price.replace(',','')
                    new_price=new_price.replace(' ','')
                    old_price=new_price
                    try:
                        connection = mysql.connector.connect(host="166.62.28.141",database="beebay",user="bilal",password="bilalshah",port=3306)
                        cursor = connection.cursor(prepared=True)
                        sql_insert_query = """ UPDATE optinex_product_details SET price= %s, new_price= %s where url= %s"""
                        insert_tuple=(old_price,new_price,url)
                        print(old_price,new_price,url)
                        result  = cursor.execute(sql_insert_query, insert_tuple)
                        connection.commit()
                        print ("Record Updated successfully into Items table:",i)
                        i+=1
                    except mysql.connector.Error as error:
                        connection.rollback()
                        print("Failed to Update into MySQL table {}".format(error))
                    driver.quit()
                else:
                    print("Check Product Url")
            except Exception:
                print("Check Dtabase Entry")

except mysql.connector.Error as error :
    #connection.rollback()
    print("Failed to Access MySQL table {}".format(error))
driver.quit()