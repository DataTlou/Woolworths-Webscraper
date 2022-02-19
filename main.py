from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import time
import pandas as pd

driver = webdriver.Chrome(executable_path="C:/Users/Tlou Ramotshela/Downloads/chromedriver/chromedriver.exe") # The location of your chrome driver
url = "https://www.woolworths.co.za/cat/Food/Food-Cupboard/_/N-1lw4dzx"
driver.get(url)
time.sleep(3)
products = []
n = driver.find_element_by_xpath("/html/body/div[1]/div/div/main/div/div[2]/div[2]/div/div[2]/div[2]").text
num = n[:5]
nu = int(num)
number = int(num)
numof = (number / 60)
c = round(numof, 0) + 1
print(int(c))
for i in range(1, 15):
    img = driver.find_elements_by_class_name("product-card_img lazyloaded")
    counting = len(img)+1
    time.sleep(6)
    for t in range(1, 61):
        try:
            driver.find_element_by_xpath(f"/html/body/div[1]/div/div/main/div/div[2]/div[2]/div/div[3]/div[{str(t)}]/article/div[3]/div/div[1]/a").click() # Choosing an item
            time.sleep(6)
            try:
                name = driver.find_element_by_xpath("/html/body/div[1]/div/div/main/div[1]/div[2]/div/div[2]/div[1]/div[1]/div[1]/div").text # Extracting the item's name
            except NoSuchElementException:
                name = driver.find_element_by_xpath("/html/body/div[1]/div/div/main/div/div/div[2]/div/div[2]/div[1]").text
            else:
                name = driver.find_element_by_class_name("prod-name").text
            try:
                bar = driver.find_element_by_xpath("/html/body/div[1]/div/div/main/div[1]/div[2]/div/div[2]/div[3]/div[1]/div/ul/div").text # Extracting the item's barcode
            except NoSuchElementException:
                bar = driver.find_element_by_xpath("/html/body/div[1]/div/div/main/div/div/div[2]/div/div[2]/div[4]/div[1]/div/ul").text
            # driver.find_element_by_xpath("/html/body/div[1]/div/div/main/div/div/div[2]/div/div[2]/div[4]/div[2]/h4").click()
            # time.sleep(1)
            # diet = driver.find_element_by_xpath("/html/body/div[1]/div/div/main/div/div/div[2]/div/div[2]/div[4]/div[2]/div").text
            products.append({"name": name, "barcode": bar})
            time.sleep(5)
            driver.back()
            time.sleep(6)
        except NoSuchElementException:
            time.sleep(5)
            df = pd.DataFrame(products)
            df.to_csv('prod1.csv')
            driver.find_element_by_xpath("/html/body/div[1]/div/div/main/div/div[2]/div[2]/div/div[3]/div["+str(t)+"]/article/div[3]/div/div[1]/a").click()
            time.sleep(6)
            try:
                name = driver.find_element_by_xpath("/html/body/div[1]/div/div/main/div/div/div[2]/div/div[2]/div[1]/div").text
            except NoSuchElementException:
                name = driver.find_element_by_xpath(
                    "/html/body/div[1]/div/div/main/div/div/div[2]/div/div[2]/div[1]").text
            else:
                name = driver.find_element_by_class_name("prod-name").text
            try:
                bar = driver.find_element_by_xpath(
                    "/html/body/div[1]/div/div/main/div/div/div[2]/div/div[2]/div[4]/div[1]/div/ul/div").text

            except NoSuchElementException:
                bar = driver.find_element_by_xpath(
                    "/html/body/div[1]/div/div/main/div/div/div[2]/div/div[2]/div[4]/div[1]/div/ul").text
            driver.find_element_by_xpath(
                "/html/body/div[1]/div/div/main/div/div/div[2]/div/div[2]/div[4]/div[2]/h4").click()
            time.sleep(5)
            diet = driver.find_element_by_xpath(
                "/html/body/div[1]/div/div/main/div/div/div[2]/div/div[2]/div[4]/div[2]/div").text
            products.append({"name": name, "barcode": bar, "Good for": diet})
            time.sleep(6)
            driver.back()
            time.sleep(6)
        else:
            try:
                driver.find_element_by_xpath("/html/body/div[1]/div/div/main/div/div[2]/div[2]/div/div[3]/div["+str(t)+"]/article/div[1]/a/div[2]/img").click()
                time.sleep(6)
            except ElementClickInterceptedException:
                time.sleep(5)
                driver.find_element_by_xpath("/html/body/div[1]/div/div/main/div/div[2]/div[2]/div/div[3]/div[" + str(t) + "]/article/div[1]/a/div[2]/img").click()
            try:
                name = driver.find_element_by_xpath(
                    "/html/body/div[1]/div/div/main/div/div/div[2]/div/div[2]/div[1]/div").text
            except NoSuchElementException:
                name = driver.find_element_by_xpath(
                    "/html/body/div[1]/div/div/main/div/div/div[2]/div/div[2]/div[1]").text
            else:
                name = driver.find_element_by_class_name("prod-name").text
            try:
                bar = driver.find_element_by_xpath("/html/body/div[1]/div/div/main/div/div/div[2]/div/div[2]/div[4]/div[1]/div/ul/div").text

            except NoSuchElementException:
                bar = driver.find_element_by_xpath(
                    "/html/body/div[1]/div/div/main/div/div/div[2]/div/div[2]/div[4]/div[1]/div/ul").text
            driver.find_element_by_xpath(
                "/html/body/div[1]/div/div/main/div/div/div[2]/div/div[2]/div[4]/div[2]/h4").click()
            time.sleep(4)
            diet = driver.find_element_by_xpath(
                "/html/body/div[1]/div/div/main/div/div/div[2]/div/div[2]/div[4]/div[2]/div").text
            products.append({"name": name, "barcode": bar, "Good for": diet})
            time.sleep(5)
            driver.back()
            time.sleep(6)
    try:
        driver.find_element_by_xpath("/html/body/div[1]/div/div/main/div/div[2]/div[2]/div/nav/div/li[2]/span[1]").click()
        time.sleep(6)
    except NoSuchElementException:
        df = pd.DataFrame(products)
        df.to_csv('product.csv')
        driver.find_element_by_xpath("/html/body/div[1]/div/div/main/div/div[2]/div[2]/div/nav/div/a[2]/span[2]").click()
        time.sleep(6)
    print(i)
df = pd.DataFrame(products)
df.to_csv('prod.csv')
driver.close()