import image_database as database
from selenium import webdriver
from bs4 import BeautifulSoup
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
db = database.DbHandler
storeid=db.store('DARAZ')
driver = webdriver.Firefox(options=options)

driver.get("https://www.daraz.pk/")
soup = BeautifulSoup(driver.page_source, 'html5lib')
#print(soup)
main_ads=soup.find_all('div', class_='J_Item card-banner-slider-item')
if main_ads is None:         
         print()
else:
    getlen=len(main_ads)
    for row in range(0,getlen):
        f_ad=main_ads[row]
        title=f_ad.find('a')['title']
        link=f_ad.find('a')['href']
        img=f_ad.find('img',class_="main-img")
        print(title)
        print(link)
        if img.get('src')  :
         imglink=img['src']
        else:
            imglink=img['data-ks-lazyload']
        
        print(imglink)
        
        
        
        
       
        #Image Recognizition
        from skimage import io
        img = io.imread("https:"+ imglink)
        import cv2
        import numpy as np
        import pytesseract
        from PIL import Image
        
        
        # Path of working folder on Disk
        src_path = "C:/Users/ZABI/Desktop/temp/"
    
        def get_string(img_path):
            # Read image with opencv
            img =img_path
        
            # Convert to gray
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
            # Apply dilation and erosion to remove some noise
            kernel = np.ones((1, 1), np.uint8)
            img = cv2.dilate(img, kernel, iterations=1)
            img = cv2.erode(img, kernel, iterations=1)
        
            # Write image after removed noise
            cv2.imwrite(src_path + "removed_noise.png", img)
        
            #  Apply threshold to get image with only black and white
            #img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
        
            # Write the image after apply opencv to do some ...
            cv2.imwrite(src_path + "thres.png", img)
            pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        
            # Recognize text with tesseract for python
            result = pytesseract.image_to_string(Image.open(src_path + "thres.png"))
        
            # Remove template file
            #os.remove(temp)
        
            return result
        
        
        print ('--- Start recognize text from image ---')
        string=get_string(img)
        print(string)
        print ('hello')
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        
        # Recognize text with tesseract for python
        result = pytesseract.image_to_string(img)
        print(result)
        import re
        print ('--- Get number from string ---')
        string=string.replace(",", "")
        result=result.replace(",", "")
        numbers = re.findall('\d\d\%',string)
        numbers = numbers + re.findall('\d\d\%',result)
        numbers = [w.replace('%', '') for w in numbers]
        print(numbers)
        if len(numbers) :
            numbers = map(str,numbers) 
            sale=(max(numbers))
            print (sale)
        else:
            sale= 0
            print ("u") 
        
            
        
        print ("------ Done -------")
        db.ad(title,"https:"+link,"https:"+ imglink,string,sale,storeid)   
        



