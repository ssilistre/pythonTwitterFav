import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webelement import WebElement
import mysql.connector

urltwitter="https://twitter.com/login"
kadi="/html/body/div/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input"
sifre="/html/body/div/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input"
logintus="//*[@id='react-root']/div/div/div[2]/main/div/div/div[1]/form/div/div[3]/div/div"
favtus="//*[@data-testid='like']"

#################################################################
urllist="https://twitter.com/i/lists/1329717353463025667"
urllist2="https://twitter.com/i/lists/1324410141345763330"
urllist3="https://twitter.com/i/lists/1329830124397662215"


#################################################################
toplamkacadet=130 #saatlik tweeter beğeni sayısı
tekrar = 0 #0 kalsın.


#################################################################
kullaniciaditwitter="***"
kullanicisifresitwitter="*****"

kullaniciaditwitter2="*****"
kullanicisifresitwitter2="****"
#################################################################
#################################################################

opts = Options()
opts.headless = False

driver = webdriver.Chrome(options=opts,executable_path="chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(15)

def kaydir():
    y = 1000
    for timer in range(0, 50):
        driver.execute_script("window.scrollTo(0, " + str(y) + ")")
        y += 1000
        time.sleep(1)
        print("Aşağı Doğru Kaydırılıyor.")
        break

def kapat():
     print("Uygulama Kapanıyor.")
     time.sleep(5)
     driver.quit()



driver.get(urltwitter)
driver.find_element_by_xpath(kadi).send_keys(kullaniciaditwitter2)
driver.find_element_by_xpath(sifre).send_keys(kullanicisifresitwitter2)
driver.find_element_by_xpath(logintus).click()
driver.get(urllist2)
while tekrar <= toplamkacadet:
    print(str(tekrar) + " kere fav atıldı.")
    try:
        driver.find_element_by_xpath(favtus).click()
        time.sleep(1)
        tekrar = tekrar + 1
    except:
        kaydir()

kapat()