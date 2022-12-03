from itertools import product
import requests
import pandas
import time
import csv
import sys
from test_telegram_bot import send_status_to_bot

def Aliexpress_scraper(item_listas,counter_for_item,counter_for_page):
    

    proxy = "173.245.49.47:80"
    url = "https://www.aliexpress.com/glosearch/api/product"
    payload = ""
    img_Url_list = []
    display_Title_list = []
    item_Url_list = []

    """
    s = sys.argv


    s = s[1:-1]

    listToStr = ' '.join([str(elem) for elem in s])
    """
    #print(str(counter_for_page)+"Program başlarken sayfa sayısı bu")
    for counter in range(1):
        time.sleep(1)
        querystring = {"trafficChannel":"main","d":"y","CatId":"0","SearchText":item_listas[counter_for_item],"ltype":"wholesale","SortType":"default","page":counter_for_page,"origin":"y","pv_feature":"1005004732290926,1005003496017478,1005003448490073,1005003424842769,1005003831538969,1005004338833281,1005004453035700,1005001490865918,1005004673584342,1005004248508059,1005003227263359,1005004592233669,1005004527477439,1005004279828609,1005004229753492,1005003081448148,4001253513692,1005004765392040,1005004715460791,4001194328609,1005004526511246,1005004437722660,4000176695736,1005004778883043,1005004379486862,1005004446351746,1005004779818613,4000977620476,1005004148917391,32926952018,1005004779860517,1005004085764652,1005003117573638,1005004765217009,1005003936282923,1005002679058945,1005004141794266,1005003777444354,1005002785054245,1005003461992493"}

        payload = ""
        headers = {
            "cookie": "xman_us_f=x_locale%3Dtr_TR%26x_l%3D0%26x_c_chg%3D1%26x_as_i%3D%257B%2522cookieCacheEffectTime%2522%253A1664655894522%252C%2522isCookieCache%2522%253A%2522Y%2522%252C%2522ms%2522%253A%25220%2522%257D%26acs_rt%3D35bccf760623410ba337104c29d4501e; intl_common_forever=VpMsMCmxoDwy0UpiP%2B%2BhcsEEWd4pHW%2BWvLMUoDer0aULllYKa3t5og%3D%3D; intl_locale=tr_TR; aep_usuc_f=site%3Dtur%26c_tp%3DTRY%26region%3DTR%26b_locale%3Dtr_TR; e_id=pt30; JSESSIONID=C27ED8DABAFCF1D712363E5259EBDF46",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0",
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br",
            "bx-v": "2.2.3",
            "DNT": "1",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "Referer": "https://www.aliexpress.com/wholesale?trafficChannel=main&d=y&CatId=0&SearchText=man+shirt&ltype=wholesale&SortType=default&page=2",
            "Proxy-Authorization": "Basic YWNjZXNzX3Rva2VuOjF1MjZxMG5lNnZubGpiaGFmdXYycGdmbWh1YXFwbG1lYm1pYjJxbDA3cXNpMmEyYW5nMWE=",
            "Connection": "keep-alive",
            "Cookie": "tfstk=cZS1BFZrrfc64OOElCwU_pOLCLtVaYMWhPOGCW75a7-nn8X66sfK4QNKmZcv0KpC.; l=eBxe5QPmTjgsnhjABO5Brurza77TmIR4zkPzaNbMiInca18PtEWiMNCEWOeHSdtfQt5D_etrp8IwkdEkWkzLRx91EJgoeDuIvMp6Re1..; isg=BKWlkruJKpyzlE7wrLNLyAb0t2Hf4ll0wt60F6eK6ly6vscwbzDxRLsYSLrIpXEs; ali_apache_id=11.10.24.123.1664655465608.181957.9; xman_us_f=x_locale=en_US&x_l=0&x_c_chg=1&x_as_i=%7B%22aeuCID%22%3A%22%22%2C%22cookieCacheEffectTime%22%3A1664655823401%2C%22isCookieCache%22%3A%22Y%22%2C%22ms%22%3A%220%22%7D&acs_rt=35bccf760623410ba337104c29d4501e; intl_common_forever=I14hTHVyRjNsPm/Zpoh/DtmsJ89pNDtnYIuGhw7Wu7QLl1o5Nvng/Q==; xman_f=LZGbAVw30ixF6QI84E9LrBJzcp3iwgzCHYBmmJCXKAJT191VZR0leVVKU62xUUmYKk1exRYLgNvKNhELwgjucm7y50jjZtDlxZCUb0Vjm6CGbiJb0hahgA==; xman_t=IWsVC3NsuZMFIrP7uoFlSPXR2wD9l1gbJRwv4coa059Ou8hbjHG9B/gssDJHNpxp; aep_usuc_f=site=glo&c_tp=USD&region=DE&b_locale=en_US; _ga_VED1YSGNC7=GS1.1.1664655431.3.1.1664655568.0.0.0; acs_usuc_t=x_csrf=twiyfrve6wb2&acs_rt=3e75fd6b7cf743e8bdbb29cc6f6386ee; intl_locale=en_US; AKA_A2=A; _m_h5_tk=aa3c978348b07eaa978f837135159cb1_1664657376081; _m_h5_tk_enc=236b07e1d0bc44f49510932322f08332; _gcl_au=1.1.1521743387.1664655487; _ga=GA1.2.2049521050.1664655487; cna=f46/G5iKgjICAQI6LDKzWCk6; xlly_s=1; ali_apache_track=; ali_apache_tracktmp=; e_id=pt30; _gid=GA1.2.1502322719.1664655490; _ym_uid=1664655490566879444; _ym_d=1664655490; _ym_visorc=b; _fbp=fb.1.1664655490636.1662178060; _ym_isad=2; JSESSIONID=B62449DF7FD5BCC7C4D1CF2FBEF156E3; RT=z=1&dm=aliexpress.com&si=5c066540-03aa-4b0d-9814-c2f9710bf3d0&ss=l8qcx1yi&sl=2&tt=f1a&obo=1&rl=1; XSRF-TOKEN=3247c993-41a6-43aa-b92f-36bf4728d95c; _gat=1",
            "TE": "trailers"
        }
        #, proxies={'http': proxy, 'https': proxy}, timeout=3
        try:
            #, proxies={'http':proxy, 'https':proxy},timeout=3
            response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
        except requests.exceptions.ProxyError:
            print("proxy is shit")
            send_status_to_bot("Proxy is shit my man")
            
            exit(1)

        data = response.json()
        
        #print(response.status_code)
        for i in range(0,59):
            #Url_list = []
            #Url_list.append()
            
            img_Url_list.append(data["mods"]["itemList"]["content"][i]["image"]["imgUrl"].replace("220x220","Q90"))
            #print(data["mods"])
            #display_Title_list.append(data["mods"]["itemList"]["content"][i]["title"]["displayTitle"])
            display_Title_list.append(data["mods"]["itemList"]["content"][i]["image"]["imgUrl"].split("/")[-1][:-18].replace("-"," "))
            item_Url_list.append("https://www.aliexpress.com/item/" +data["mods"]["itemList"]["content"][i]["productId"]+ ".html")
            #print(data["mods"]["itemList"]["content"][i]["image"]["imgUrl"])
            #print(data["mods"]["itemList"]["content"][i]["title"]["displayTitle"])
        #["mods"]["itemList"]["content"][0]
    returning_display_title = item_listas[counter_for_item]
    if counter_for_page == 1:
        counter_for_page = 2
        #print(str(counter_for_page)+ "counter for page bu") 
    elif counter_for_page == 2:
        #print("buraya gir di mi diye merak ediyorum")
        counter_for_item += 1
        counter_for_page = 1  


    with open("Image_URLS", 'w', newline='',encoding="utf-8") as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerow(img_Url_list)
        
    with open("Display_Titles", 'w', newline='',encoding="utf-8") as f:
        wr = csv.writer(f, quoting=csv.QUOTE_ALL)
        wr.writerow(display_Title_list)

    with open("Item-Urls",'w', newline='',encoding="utf-8") as abx:
        wr = csv.writer(abx, quoting=csv.QUOTE_ALL)
        wr.writerow(item_Url_list)
    
    print("Aliexpress data has successfully scraped")
    send_status_to_bot("Aliexpress data has successfully scraped")
    return returning_display_title,counter_for_item,counter_for_page