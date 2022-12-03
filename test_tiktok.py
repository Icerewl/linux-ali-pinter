
from twilio.rest import Client 
 
account_sid = 'AC33eecc10651c93d5aa420c8316a3b48f' 
auth_token = 'b099417e1069c527853abf49e7a2b3ce' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='As tave milu mano meile <3',      
                              to='whatsapp:+37064409843' 
                          ) 
 
print(message.sid)

"""
from main import open_selenium
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
driver,wait = open_selenium()

driver.get("https://www.pinterest.de/login/")
email = wait.until(EC.element_to_be_clickable((By.ID, 'email')))
password = wait.until(EC.element_to_be_clickable((By.ID, "password")))
email.send_keys("wabina2102@haizail.com")
password.send_keys("wabina2102")
time.sleep(3/2)
driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div/div/div/div[3]/div/div/div[3]/form/div[7]/button').click()
time.sleep(3)
driver.get("https://www.pinterest.de/pin-builder/")
actions = ActionChains(driver)
a= driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div[1]/div[1]/div/div/div[1]/textarea').send_keys("Allahınız yok")
actions.send_keys(Keys.TAB)
actions.send_keys("ANANIZI SİKİYİM")
actions.perform()
wait.until(EC.text)
"""