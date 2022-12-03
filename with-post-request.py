#nefiw79541@imdutex.com
#nefiw79541
from distutils.log import error
import time
from Admitad_link_converter import link_convert, file_opener
import requests
from Aliexpress_scraper import Aliexpress_scraper
from test_telegram_bot import send_status_to_bot
counter_for_item = 0
counter_for_page = 1
error_counter = 0
def main_function(counter_for_item,counter_for_page,error_counter):
    item_list = ["Women Sweaters","Women Skirts","Women leggings","Women Jeans","Pajama sets","Hair accessories"
    ,"Dog toys","Costume shoes","Laptop batteries","Baby Shirts","Wedding Dresses","Scented Candles","Bluetooth Speaker","Smart Watch",
    "Neck massager","Portable Blender","Nail Polish","Wireless phone chargers","Doormats","Wifi repeater","Cat","Socks","Backpack","Baby Swings","Women blouses"]
    
    single_display_title,item_num,page_num = Aliexpress_scraper(item_list,counter_for_item,counter_for_page)
    counter_for_item,counter_for_page = item_num, page_num
    single_display_title = single_display_title.replace(" ","%20")
    images = file_opener("Image_URLS")
    for i in range(0,len(images)):
        images[i] = "https:" + images[i]
        
    displays = file_opener("Display_Titles")
    for i in range(0,len(displays)):
        displays[i] = displays[i].replace(" ","%20")
        displays[i] = single_display_title +"%20"+ displays[i]
        
    items = file_opener("Item-Urls")
    for i in range(0,len(items)):
        items[i] = link_convert(items[i])



    for i in range(0,int(len(items))):
        try:
            #account_post_list = []
            url = "https://www.pinterest.de/resource/PinResource/create"
            payload = f"source_url=%2Fpin-builder%2F&data=%7B%22options%22%3A%7B%22board_id%22%3A%22871868877800615186%22%2C%22field_set_key%22%3A%22create_success%22%2C%22skip_pin_create_log%22%3Atrue%2C%22description%22%3A%22{displays[i]}%22%2C%22link%22%3A%22{items[i]}%22%2C%22title%22%3A%22{single_display_title}%22%2C%22image_url%22%3A%22{images[i]}%22%2C%22method%22%3A%22uploaded%22%2C%22upload_metric%22%3A%7B%22source%22%3A%22partner_upload_standalone%22%7D%2C%22user_mention_tags%22%3A%5B%5D%2C%22no_fetch_context_on_resource%22%3Afalse%7D%2C%22context%22%3A%7B%7D%7D"
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0",
                "Accept": "application/json, text/javascript, */*, q=0.01",
                "Accept-Language": "en-US,en;q=0.5",
                "Accept-Encoding": "gzip, deflate, br",
                "Content-Type": "application/x-www-form-urlencoded",
                "X-Requested-With": "XMLHttpRequest",
                "X-APP-VERSION": "2c3bf4a",
                "X-CSRFToken": "50baef33bd25dc651b9fd73a75ff60a2",
                "X-Pinterest-AppState": "background",
                "X-Pinterest-ExperimentHash": "783b11f71a5e81b7910fdd8c6a0d1f0721b2fe52d4cbbee0b45ce085f97c0b27d942fa1e258d8132d725d55c66b226545c6bce6c947ccb792cf3622b5f9f08c8",
                "X-Pinterest-Source-Url": "/pin-builder/",
                "X-Pinterest-PWS-Handler": "www/pin-builder.js",
                "Origin": "https://www.pinterest.de",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "Referer": "https://www.pinterest.de/",
                "Connection": "keep-alive",
                "Cookie": "csrftoken=50baef33bd25dc651b9fd73a75ff60a2; _pinterest_sess=TWc9PSY4NkNUeXZ4YUprV1JUNmg2ZVd0eTRaQndoODdoR3RUVS83Y2crYnUyNU9CL1ViaWMySjBNZEdlSWozbzZ0Y1Mzc0ZUdGwxTWRwSW5RNFFzTHdMSmtySFF3Mjg5STl3M2tnM3RLVFViZFRYUU5lS0pmTGFPOHhyTGplY0ZPL055MjdiVDFzSytFM1g3RDgzazBwYWNxbWdBcm9idEJ4TDltY2R2RW1QR0NCekliS204d3RtL1AxQkJwSEVldzZWVUgzZjcrWk9rTmNuY0RLMzZuOXZmVFU3a1lKUVI0azh2QlhhQytoNXZ4Z0hYTGZhdTBydU1sQTZIRHNLTy9Zbi9lSzdKMDRhZnl4cEZtaXl6TGdKN3ZwMzYwTUNzaENZd1o4NmsyNzJ4WTlZMzZFVGJvdlArNXcva285NXB4SDB0eEdMT1VTRlovekpiSDlrTzlrOXEyUy9kZ01uRitZRittSks0eVd6ZWhyMXNYTGxRTWNaeVlpVTdYWmQyd1VLOHdIcGF4WElldDJJWnZMOWxiYUZYNC9ucEl6YzZNOWN4d3M1TnZYd1NDaDBSS09uQ1d6VUZMU0ozazE1ckNQTzJ0a0NSS1NaRVdaUXY4bExNbEtDdkpmTkRqNlZVa29XU2ZndWlXTVN0dWdqZXU0ZVJ2Y3p0NVlKRElYUU5acVljZTJwYS9WTVpkMU9CbkM1UUlTWWdtVXMvYWRHOXd1U1diRlNNSUdPTUlzajFLNlA5V1dRNlBSdFp6MU9XdUJGQ1QrQXJoZ1J5MGRtTm9VcWREcVRtL3dZSUpURnhqRjVJSXdyc1YxN1NIajJTQjROenRNUVkwbU5Hc2N0WWhSUWFOcUpkaUF6eTF5aDR2bGFKbWpwU3hIMTBYc0tLcmpjR1Ntb2U3UE5lVGdXQTAxTTdRNTdUd1MyS0RLZEtaMFA2dGgvV0srNnZ2ZUtEdWZBVzVMUExiV3hZR0hzd3o4aFc0dElXeStralpMcFNsZmc1UXZRTGJicUh5RGtLRXZ5UTZ1QTZTbWhaL1d3L0lYK0tlYUJpT0NRR3VxWk9aWEJBRlRzY1B1Wm96bzI2WTdNcDFDQk9jRVRyZHYrL2ZIZ2JpTnluR2x1Y0dwY1paRGFscjdIMTlBUGY1OW8wenR0Vmh2Tk96Nmx2UmN0RWlaLzZBNnlxTW80Z3FURmQ0T24xT1d4dWZUd1VlQktNZ0NuMHFiRzZCVGVNV0h1aDNvNzJOZTZRQ0dCR0ZuNkJsMzNJYkh0VlVUcXFiZHJLZ3dVV29McVpVZjJUdU9XTzQ4dXAxWjFHV2JHZVBzVHUvZ3RKbXh6czYzVnVzM0FNZXVMVndZa2M3L0dNS0pnRVByNzFZMis2Zzc3akRaL09YQ0xaSEF4K1pBSHhiNm5ZT1RMMTZMQWVZTFU3RndIU1M1akNWK2h5SUhoYTZtTWl4VXZTbytnQTJXeTVtaGN3RjNXWXBLRW1EOXorVm85eklCZStBOHZORldzclB1RVFoSFRTVk5Vb3JwcUNzMmxmblNFMGdiM1c4aUhoc3Q0c3VvblNVbmU5cTBRQnkrOTdMRkhIKzNvYkdhRlRYOUlNRHFic2JTQjQvcC9ZTlEzSEMvMGdlRkRCWG9PRFIwQm10NlB6SU9KMFZHaXNCczRJOTBaLy9sbGVUeGlFV09qak0zdXNxK3JyTmRNbTIyNGxYVzJyWlVFamtpd3RiYm02bG02eElCaEYrL1B1cFVXT0QycEwwN3M3SVQyVGRFcGJybGRod0tRL2VGOFVKRFZqUUlSVlFkeWZmVTJnaVJBb290K3FVUG5VR2t3SHV1YnJXM29MVjY3dW4zdnJ4Z21qU2dpVWd6OHk5dzg5QWhEZ0ZHcFFrTHYxL1hDSlJaSHlKb2lqMEFFeElhM2RGeHJlNWRhYzIydHZEaU1SY1JSQ0RKejB1WDZJeHpKcitjM091dXhUOHViaXZSMnFUSUcxM1JkMHYzVzY1OVdjd2hGTkFFUmRYSzl3bFgxVTljdzNkUEtublNGNlIwaTFQazlRRy9SSDFwTlRFbWZFSnlocGRXajZHVWFqd0tIYkR1dmdEdzlGNTBhL3E1NEplSEpZdlZRNlNZUjFpV3FCSGVzZmdwaTJiRDh1SkZPdk8wOUtzcVp5SjRrTVpjZVo3dm1MeGhBQVdKZWtqUHdwbjRjWXJyU2xVL1gvNmxteENlQ201c1UxRHZ1YzlVRDBwZlRuMW5Yc2RKVTJEVXA1ek9xcmtHZXUzWDk1S0dxbmpZQ0RibGVOUmxuMTRmeW8zM1B6ZXY3UC9ab3lxenRZeDFjUEpLL21SSW5QMS9kZzN4QmN5dHdzRUtka2pIZXZKTjAxOWF2aXZsdHBtTGJaenBveFdlc1NERmFGUXhDektTNmNEMXRZYy8xcUlSLzJHTW9zQm1zVGNDN2htU2JKRStiTDJLckZwNm5RWUFRb2grR0lLenBibkJIeUkrbklMdlBnOXArRFQ3TjhoUFIxaU1lZnZlMXNLOXdaM3NUY1F2djlqTHoxZjl2M05qL3JrNGdvMXdNMGFnQ09rcG9Xekk4UlRJWEtaVmdkbXEvNmJxK1dtWjRHdWJ0THdTLzFSb2FEUE5XNndMNUxuSHBaSEVxRGYyWm50ZHZ5eVhsd1JqRHlKaXVJVVlmL1UzWTlONUt4WHJVWklNd0RIdE40WXN5QT0mcWtyQnNqWmM2c290SjcwZFNqQzAzN1hFT1RzPQ==; _auth=1; cm_sub=none; fba=True; _routing_id=fbe4bce4-51fe-4956-8263-7264a6e6610f; sessionFunnelEventLogged=1",
                "TE": "trailers"
            }

            response = requests.request("POST", url, data=payload, headers=headers)


            """
            
            if account_post_list:
                account_post_list = " ".join(account_post_list)
                print("Following accounts have successfully posted their items: " + account_post_list)
                send_status_to_bot("Following accounts have successfully posted their items: " + account_post_list)
            else:
                print("Failed to post in every account")
                send_status_to_bot("Failed to post in every account")
            """
            if response.status_code != 200:
                print(str(i)+". posting failed" + "Reason: Request didn't pass")
                send_status_to_bot("DEVICE 1 "+str(i)+". Posting Failed" + "Reason: Request didn't pass")
                error_counter += 1
            else:
                send_status_to_bot("DEVICE 1 " +str(i)+". Post Created Succesfully" + "  Product Display Title: "+ displays[i][0:15])
                print(str(i)+". Post Created Succesfully" + "  Product Display Title: "+ displays[i][0:30])
        
                  
        except Exception as e:
            print(str(i)+". posting failed" + "Reason: "+ str(e))
            send_status_to_bot("DEVICE "+str(i)+". Posting Failed" + "Reason:" + str(e))
            #time.sleep(300)
            error_counter += 1
            pass
    time.sleep(3600) 
            
    return counter_for_item,counter_for_page,error_counter
if __name__ == "__main__":
    while True:
        counter_for_item,counter_for_page,error_counter = main_function(counter_for_item,counter_for_page,error_counter)

        