from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pyautogui

# variables
rsival = []
macdval = []
tsival = []
btcval = []
bbval = []
vval = []
i = 0 # day counter

# save data into file
def writef(fpath, vname):
    with open(fpath, "+w") as fhandle:
        for d in vname:
            fhandle.write("%s\n" % d)

def indicator():
    driver.switch_to.frame(
        driver.find_element(
            By.XPATH,
            "/html/body/div/div/main/div/div/div/div[1]/div/div/div[1]/div/iframe",
        )
    )
    driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/table/tr[3]/td[2]/div/div[3]/div/span[2]/a[3]').click()
    # adding RSI chart to the Trading View
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="header-toolbar-indicators"]').click()
    time.sleep(1)
    driver.find_element(
        By.XPATH, "/html/body/div[4]/div/div/div[2]/div[2]/div[1]/input"
    ).send_keys("RSI")
    time.sleep(1)
    driver.find_element(
        By.XPATH, "/html/body/div[4]/div/div/div[2]/div[2]/div[2]/div[1]/div/div/div[1]"
    ).click()
    time.sleep(1)
    # MACD
    driver.find_element(
        By.XPATH, "/html/body/div[4]/div/div/div[2]/div[2]/div[1]/input"
    ).clear()
    driver.find_element(
        By.XPATH, "/html/body/div[4]/div/div/div[2]/div[2]/div[1]/input"
    ).send_keys("MACD")
    time.sleep(1)
    driver.find_element(
        By.XPATH, "/html/body/div[4]/div/div/div[2]/div[2]/div[2]/div[1]/div/div/div[1]"
    ).click()
    time.sleep(1)
    # TSI
    driver.find_element(
        By.XPATH, "/html/body/div[4]/div/div/div[2]/div[2]/div[1]/input"
    ).clear()
    driver.find_element(
        By.XPATH, "/html/body/div[4]/div/div/div[2]/div[2]/div[1]/input"
    ).send_keys("TSI")
    time.sleep(1)
    driver.find_element(
        By.XPATH, "/html/body/div[4]/div/div/div[2]/div[2]/div[2]/div[1]/div/div/div[1]"
    ).click()
    time.sleep(1)
    # BB
    driver.find_element(
        By.XPATH, "/html/body/div[4]/div/div/div[2]/div[2]/div[1]/input"
    ).clear()
    driver.find_element(
        By.XPATH, "/html/body/div[4]/div/div/div[2]/div[2]/div[1]/input"
    ).send_keys("BB")
    time.sleep(1)
    driver.find_element(
        By.XPATH, "/html/body/div[4]/div/div/div[2]/div[2]/div[2]/div[1]/div/div/div[1]"
    ).click()
    time.sleep(1)
    # volume
    driver.find_element(
        By.XPATH, "/html/body/div[4]/div/div/div[2]/div[2]/div[1]/input"
    ).clear()
    driver.find_element(
        By.XPATH, "/html/body/div[4]/div/div/div[2]/div[2]/div[1]/input"
    ).send_keys("volume")
    time.sleep(1)
    driver.find_element(
        By.XPATH, "/html/body/div[4]/div/div/div[2]/div[2]/div[2]/div[1]/div/div/div[1]"
    ).click()
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[3]").click()
    time.sleep(1)

def checkRSIValue():
    # getting RSI value
    RSIvalue = driver.find_element(
        By.XPATH,
        "/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/table/tr[3]/td[2]/div/div[3]/div/div/span[1]/span",
    ).text.encode("utf-8")
    RSIvalue = float((RSIvalue.decode("utf-8"))[1:5])
    return RSIvalue

def checkPriceValue():
    # getting Price value
    Pricevalue = driver.find_element(
        By.XPATH,
        "/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/table/tr[1]/td[2]/div/div[3]/div/div/span[4]/span[2]",
    ).text.encode("utf-8")
    Pricevalue = int((Pricevalue.decode("utf-8"))[1:-1])
    return Pricevalue

def checkMACDValue():
    # getting MACD value
    MACDvalue = driver.find_element(
        By.XPATH,
        "/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/table/tr[5]/td[2]/div/div[3]/div/div/span[1]/span",
    ).text.encode("utf-8")
    if MACDvalue.decode("utf-8")[1] == "\u2212":
        MACDvalue = int((MACDvalue.decode("utf-8"))[2:-6])
    else:
        MACDvalue = int((MACDvalue.decode("utf-8"))[1:-6])
    return abs(MACDvalue)

def checkBBValue():
    # getting BB value
    BBvalue = driver.find_element(
        By.XPATH,
        "/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/table/tr[1]/td[2]/div/div[3]/div[2]/div/span[3]/span",
    ).text.encode("utf-8")
    BBvalue2 = driver.find_element(
        By.XPATH,
        "/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/table/tr[1]/td[2]/div/div[3]/div[2]/div/span[2]/span",
    ).text.encode("utf-8")
    BBvalue = int((BBvalue.decode("utf-8"))[1:-6])
    BBvalue2 = int((BBvalue2.decode("utf-8"))[1:-6])
    return BBvalue2 - BBvalue

def checkTSIValue():
    # getting TSI value
    TSIvalue = driver.find_element(
        By.XPATH,
        "/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/table/tr[7]/td[2]/div/div[3]/div/div/span[1]/span",
    ).text.encode("utf-8")
    if TSIvalue.decode("utf-8")[1] == "\u2212":
        TSIvalue = float((TSIvalue.decode("utf-8"))[2:-4]) * -1
    else:
        TSIvalue = float((TSIvalue.decode("utf-8"))[1:-4])
    return TSIvalue

def checkVolumeValue():
    # getting TSI value
    Volumevalue = driver.find_element(
        By.XPATH,
        "/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/table/tr[9]/td[2]/div/div[3]/div/div/span[1]/span",
    ).text
    rgb = driver.find_element(
        By.XPATH,
        "/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/table/tr[9]/td[2]/div/div[3]/div/div/span[1]/span",
    ).get_attribute("style")
    if rgb[11] == '8':
        Volumevalue = 'G'+str(Volumevalue)
    else:
        Volumevalue = 'R'+str(Volumevalue)
    return Volumevalue

def getDatas(days):
    global i
    for day in range(days):
        pyautogui.press("left")
        time.sleep(0.3)
        try:
            btcval.append(checkPriceValue())
        except:
            time.sleep(1)
            btcval.append(checkPriceValue())
        
        try:
            rsival.append(checkRSIValue())
        except:
            time.sleep(1)
            rsival.append(checkRSIValue())
        
        try:
            bbval.append(checkBBValue())
        except:
            time.sleep(1)
            bbval.append(checkBBValue())
        
        try:
            macdval.append(checkMACDValue())
        except:
            time.sleep(1)
            macdval.append(checkMACDValue())
        
        try:
            tsival.append(checkTSIValue())
        except:
            time.sleep(1)
            tsival.append(checkTSIValue())
        try:
            vval.append(checkVolumeValue())
        except:
            time.sleep(1)
            vval.append(checkVolumeValue())
        i += 1
        print(f"{i}/{days}", end='\r')


# Driver settings
chromedriver = "chromedriver.exe"
chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome("chromedriver", options=chrome_options)
driver.get("https://nobitex.ir/app/exchange/btc-rls/")
time.sleep(15)

# run functions
indicator()
time.sleep(5)
getDatas(4065) #fetch past 4065 hours
writef("datasetRSIval.txt", rsival)
writef("datasetPrice.txt", btcval)
writef("datasetMACD.txt", macdval)
writef("datasetTSI.txt", tsival)
writef("datasetBB.txt", bbval)
writef("datasetVolume.txt", vval)
