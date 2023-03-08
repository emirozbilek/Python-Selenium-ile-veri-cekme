from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json

driver = webdriver.Chrome()
url = "https://www.hukukihaber.net/makale"
driver.get(url)
# time.sleep(5)


makale_tüm = []

makale_linkleri = driver.find_elements(By.CSS_SELECTOR, 'div.row div.col-6 h4.mb-0 a')
for i in range(11):
    i+=1
    link = makale_linkleri[i].get_attribute('href') 
    driver.get(link)
    time.sleep(5)
    try:
        yazar = driver.find_element(By.CSS_SELECTOR, "div.col-lg-8 h4 a").get_attribute('title')
        if yazar:
            print(yazar)
        
    except:
        yazar = ""
        if yazar == "":
            yazar = driver.find_element(By.CSS_SELECTOR, 'div.col-lg-8 div.article-text p strong').text
            print(yazar)
    time.sleep(2)

    baslik = driver.find_element(By.CSS_SELECTOR, "div.infinite-item div.container h1").text
    print(baslik)
    time.sleep(2)

    icerik = driver.find_element(By.CSS_SELECTOR, "div.card div.article-text").text
    #print(icerik)

    time.sleep(2)

    makale = {
                "yazar": yazar,
                "baslik": baslik,
                "icerik": icerik
            }
    makale_tüm.append(makale)
    time.sleep(2)
    driver.back()

time.sleep(2)
with open("Makaleler.json", "w", encoding="utf-8") as f:
    json.dump(makale_tüm, f, ensure_ascii=False)

print("Makaleler kaydedildi")

time.sleep(3)
driver.close()