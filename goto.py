# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 12:24:54 2019

@author: ZABI
"""
import goto_database as database
db = database.DbHandler
storeid=db.store('GOTO')
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
options = webdriver.FirefoxOptions()
#options.add_argument('-headless')
options.add_argument('--no-sandbox') # Bypass OS security model
options.add_argument('--disable-gpu')  # applicable to windows os only
options.add_argument('start-maximized') # 
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
driver = webdriver.Firefox(options=options)
response = requests.get("https://www.goto.com.pk/")
soup = BeautifulSoup(response.content, 'html.parser')
main_categorie=soup.ul.find_all('li', recursive=False)
print(main_categorie)
if main_categorie is None:         
         print()
else:
    getlen=len(main_categorie)
    print(getlen)
    for row1 in range(3,getlen):
        f_cat=main_categorie[row1]
        main_cat_name = f_cat.find('span', class_='title')
        #Main Categoriee
        print(main_cat_name.text)
        db = database.DbHandler
        mid=db.categorie(main_cat_name.text) 
        #print(mid)
#        l2_categorie=f_cat.find('div', class_='mega1-cont')
#        l3=l2_categorie.find_all('li', class_='mega-title')
        l4=f_cat.ul.find_all('li' , recursive=False)
        #Sub Categorie
        if l4 is None:         
                 print()
        else:
            getlen=len(l4)
            print(getlen)
            for row12 in range(0,getlen):
                s_cat_link=l4[row12].find('a')['href']
                s_cat_name=l4[row12].find('a').text
                print (s_cat_name);
            for row12 in range(0,getlen):
                s_cat_link=l4[row12].find('a')['href']
                s_cat_name=l4[row12].find('a').text
                print (s_cat_name);
                #db = database.DbHandler
                #cid=db.subcategorie(s_cat_name,s_cat_link,mid) 
#                #Pagination
#                url2="https://www.goto.com.pk"+s_cat_link
#                driver.get(url2)
#                soup2 = BeautifulSoup(driver.page_source, 'html5lib')
#                page=soup2.find('div', class_="limiter")
#                titleofpage=page.find('label').text
#                import re
#                numbers = re.findall('\d\d',titleofpage)
#                if len(numbers) :
#                    numbers = map(str,numbers) 
#                    pages=(max(numbers))
#                print (pages)
                for page in range(1,2):
                    
                    url="https://www.goto.com.pk"+s_cat_link+"/filter/p/"+str(page)
                    print(url)
                    driver.get(url)
                    soup1 = BeautifulSoup(driver.page_source, 'html5lib')
                    products=soup1.find_all('div', class_='item-inner')
                    if not products:
                                   print ("null")
                    else:
                        getlen=len(products)
                        print ("hello")
                        print (getlen)
                        for row12 in range(0,4):
                            product=products[row12]
                            print("Product is here")
                            #print(product)
                            p_links=product.find('div',class_="product-image")
                            p_link=p_links.find('a')['href']
                            p_img_link=p_links.find('img')['data-image']
                            p_title=product.find('div',{"class":"product-name"})
                            p_title_name=p_title.find('a')['title']
                            
                            #Prices
                            p_prices=product.find_all('span',{"class":"price"})
                            getlen=len(p_prices)
                            #print (getlen)
                            if(getlen==1):
                                          p_price=p_prices[0].text
                                          p_old_price="0"
                                            
                            else:       
                                 p_old_price=p_prices[0].text
                                 p_price=p_prices[1].text
                                
                            print(p_price)
                            print(p_old_price)
                            
                            url="https://www.goto.com.pk"+s_cat_link+"/filter/p/"+str(page)
                            print(p_link)
                            driver.get(p_link)
                            soup4 = BeautifulSoup(driver.page_source, 'html5lib')                            
                            p_brand=soup4.find('div',{"class":"product-brand"})
                            p_brand_name=p_brand.find('img')['title']
                            
                            
                            # PRODUCT FEATURE
                            response = requests.get(p_link)
                            soup2 = BeautifulSoup(response.content, 'html.parser')
                            productfeatures=soup2.find('div', class_='short-description')
                            text=''.join(productfeatures.find_all(text=True))  
                            
                            print(p_title_name,p_link,p_img_link,p_price,p_old_price,p_brand_name,text,storeid,cid)