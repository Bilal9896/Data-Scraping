# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 04:23:48 2019

@author: ZABI
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 19:13:09 2018

@author: ZABI
"""
import mysql.connector
from mysql.connector import Error
class DbHandler():
    def store(name):
        try:    
                connection = mysql.connector.connect(host='localhost',
                                         database='shopnexus',
                                         user='root',
                                         password='')
                if connection.is_connected():
                        cursor = connection.cursor()
                        sql = "SELECT * FROM sellingstore WHERE name = '"+name+"'"
                        print(sql)
                        cursor.execute(sql)
                        entry = cursor.fetchone()
            
                        if entry is None:
                            sql1 = " INSERT INTO `sellingstore`(`name`)" "VALUES (%s)"
                            val1 = (name,)
                            cursor = connection.cursor()
                            cursor.execute(sql1,val1)
                            connection.commit()
                            return cursor.lastrowid
                        else:
                             return entry[0]
        except Error as e :
                print ("Error while connecting to MySQL", e)
#        finally:
#                #closing database connection.
#                if(connection.is_connected()):
#                    cursor.close()
#                    connection.close()
#                    print("MySQL connection is closed") 
                         
                            
                             
    def product(name,link,image,price,oldprice,brand,feature,storeid,catid):
        try:    
                price=price.replace("Rs.", "")
                price=price.replace(",", "")
                brand=brand.replace(" ", "-")
                price=price.strip()
                oldprice=str(oldprice)
                oldprice=oldprice.replace("Rs.", "")
                oldprice=oldprice.replace(",", "")
                oldprice=oldprice.strip()
                connection = mysql.connector.connect(host='localhost',
                                         database='shopnexus',
                                         user='root',
                                         password='')
                if connection.is_connected():
                        cursor = connection.cursor()
                        sql = "SELECT * FROM product WHERE name = '"+name+"' and category_id='"+str(catid)+"' and store_id='"+str(storeid)+"'"
                        print(sql)
                        cursor.execute(sql)
                        entry = cursor.fetchone()
            
                        if entry is None:
                            sql1 = " INSERT INTO `product`(`name`, `link`, `image`, `price`, `oldprice`, `brand`, `feature`, `store_id`, `category_id`)" "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                            print(sql1);
                            val1 = (name,link,image,price,oldprice,brand,feature,storeid,catid)
                            cursor = connection.cursor()
                            cursor.execute(sql1,val1)
                            connection.commit()
                            return cursor.lastrowid
                        else:
                             return entry[0]
                       
                      
                  
        except Error as e :
                print ("Error while connecting to MySQL", e)
#        finally:
#                #closing database connection.
#                if(connection.is_connected()):
#                    cursor.close()
#                    connection.close()
#                    print("MySQL connection is closed") 
    def categorie(name):
        try:
                name=name.replace("'", "")
                name=name.strip()
                if (name=="Phones & Tablets"): name="Electronic Devices"
                elif (name=="Computing"): name="Electronic Devices"
                elif (name=="Games & Consoles"): name="Electronic Devices"
                elif (name=="TV, Audio & Video"): name="TV & Home Appliances"
                elif (name=="Appliances"): name="TV & Home Appliances"
                elif (name=="Sports & Fitness"): name="Sports & Outdoor"
                elif (name=="Cameras & Accessories"): name="Electronic Accessories"
                elif (name=="Home & Living"): name="Home & Lifestyle"
                elif (name=="Beauty Products"): name="Health & Beauty"
                elif (name=="Kids & Babies"): name="Babies & Toys"
                elif (name=="Books & Stationery"): name="Health & Beauty"
                elif (name=="Automobiles & Motorcycles"): name="Automotive & Motorbike"
                connection = mysql.connector.connect(host='localhost',
                                         database='shopnexus',
                                         user='root',
                                         password='')
                if connection.is_connected():
                        cursor = connection.cursor()
                        sql = "SELECT * FROM category WHERE name = '"+name+"'"
                        cursor.execute(sql)
                        entry = cursor.fetchone()
            
                        if entry is None:
                            sqli = " INSERT INTO `category`(`name`)" "VALUES (%s)"
                            vali = (name,)                          
                            cursor.execute(sqli,vali)
                            connection.commit()
                            return cursor.lastrowid
                        else:
                             return entry[0]
                  
        except Error as e :
                print ("Error while connecting to MySQL", e)
#        finally:
#                #closing database connection.
#                if(connection.is_connected()):
#                    cursor.close()
#                    connection.close()
#                    print("MySQL connection is closed") 
     
    def subcategorie(name,link,pcat):
        try:
                name=name.replace("'", "")
                name=name.strip()
                connection = mysql.connector.connect(host='localhost',
                                         database='shopnexus',
                                         user='root',
                                         password='')
                if connection.is_connected():
                       cursor = connection.cursor()
                       sql = "SELECT * FROM category WHERE name = '"+name+"'"
                       cursor.execute(sql)
                       entry = cursor.fetchone()
            
                       if entry is None:
                               sql1 = " INSERT INTO `category`(`name`,`link`,`pid`)" "VALUES (%s,%s,%s)"
                               val1 = (name,link,pcat,)
                               cursor = connection.cursor()
                               cursor.execute(sql1,val1)
                               connection.commit()
                               return cursor.lastrowid
                       else:
                             return entry[0]
                       
                  
        except Error as e :
                print ("Error while connecting to MySQL", e)
#        finally:
#                #closing database connection.
#                if(connection.is_connected()):
#                    cursor.close()
#                    connection.close()
#                    print("MySQL connection is closed") 
       
        