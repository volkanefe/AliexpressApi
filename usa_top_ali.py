import os
import json
import time
import csv
import textwrap
from pathlib import Path
from aliexpress_api import AliexpressApi, models

if os.path.exists('usa_top_ali.csv'):
    os.remove('usa_top_ali.csv')

datas = []
with open(os.path.dirname(os.path.realpath(__file__)) + os.sep +"aliConfig.json", encoding="utf-8") as config_file:
    config = json.load(config_file)

    aliexpress = AliexpressApi(config['API_KEY'],config['SECRET_KEY'], models.Language.EN, models.Currency.USD, config['TRACKING_ID'])

    file1 = open('aliste.txt', 'r') 
    Lines = file1.readlines()
    for line in Lines: 
          

        try:
            product = aliexpress.get_products_details(line.strip())
            baslik = product[0].product_title
            link = aliexpress.get_affiliate_links('https://aliexpress.com/item/'+ line.strip() +'.html')[0].promotion_link
            resim = product[0].product_main_image_url
            print(product[0].product_id)
            
   
            datas.append([link, resim, baslik])
                
            

        except:
            continue
        time.sleep(2)

    with open('usa_top_ali.csv', 'w', newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        for data in datas:
            writer.writerow(data)
         
f = open('aliste.txt', 'r+')
f.truncate(0)
    
    
    
    
  

    