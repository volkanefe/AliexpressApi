import os
import json
from numpy import product
from pathlib import Path
from aliexpress_api import AliexpressApi, models
import time
import csv

if os.path.exists('usa_hot_ali.csv'):
    os.remove('usa_hot_ali.csv')

tarama = input("Aranacak ürün adını girin : ")

if tarama != None:

    datas = []

    with open(os.path.dirname(os.path.realpath(__file__)) + os.sep + "aliConfig.json", encoding="utf-8") as config_file:
        config = json.load(config_file)

        aliexpress = AliexpressApi(config['API_KEY'],config['SECRET_KEY'], models.Language.EN, models.Currency.USD, config['TRACKING_ID'])

    hotproducts = aliexpress.get_hotproducts(keywords=tarama, min_sale_price=10)
    datas.append(["link", "resim", "icerik", "urun_no"])
    for i in range(5):
        try:
            product_id = hotproducts.products[i].product_id
            product_desc = hotproducts.products[i].product_title
            resim = hotproducts.products[i].product_main_image_url
            video1 = hotproducts.products[i].product_video_url
            product_aff = aliexpress.get_affiliate_links('https://aliexpress.com/item/'+ str(product_id) +'.html')[0].promotion_link
            

            print(product_id)
        

            datas.append([product_aff,resim,product_desc, product_id])
            
            
        except:
            continue 
        time.sleep(1)

        with open('usa_hot_ali.csv', 'w', newline='', encoding="utf-8") as file:
            writer = csv.writer(file)
            for data in datas:
                writer.writerow(data)

file.close()
