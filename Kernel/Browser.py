from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from Kernel.Settings import Settings, Colors
from Kernel.CsvCore import CsvCore

from colorama import Fore, Back, Style
from colorama import init

from tqdm import tqdm
from bs4 import BeautifulSoup
import os, time, sys, csv, re, threading, requests, random, colorama


class Browser:
    def __init__(self, linkdb,option):
        self.LINKS_LOCAL = linkdb
        print("PATH IS {}".format(linkdb))
        self.CHROME = webdriver.Chrome(executable_path=r"/usr/lib/chromium-browser/chromedrive", chrome_options=self.config_browser())
        if option == 'sublinks':
            self.Sublinks()
        if option == 'extract':
            self.LoadLinks()

    def config_browser(self):
        option = Options()
        #option.headless = True
        option.add_argument("--window-size=1920,1080")
        option.add_argument('--no-sandbox')
        return option

    
    def LoadLinks(self):
        LINKSTACK = Settings().Read(Settings.CACHE_PAGES).split('\n')
        for link in LINKSTACK:
            print("OPENING {}".format(link))
            try:
                self.CHROME.get(link)
                Exfiltrator(self.CHROME,link).getBox()
            except ConnectionAbortedError:
                print("CONNECTION PROBLEM {}".format(link))
            except ConnectionRefusedError:
                print("CONNECTION PROBLEM {}".format(link))
            WebDriverWait(self.CHROME,5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "body")))
            #Exfiltrator(self.CHROME, link).getBox()

    def Sublinks(self):
        self.CHROME = webdriver.Chrome(executable_path=r"/usr/lib/chromium-browser/chromedriver", chrome_options=self.config_browser())
        LINKSTACK = Settings().Read(self.LINKS_LOCAL).split('\n')
        for link in LINKSTACK:
            print(link)
            self.CHROME.get(link)
            if self.Exists(Settings.SUB_LINKS):
                pgs = self.CHROME.find_elements(By.XPATH, Settings.SUB_LINKS)
                for pg in pgs:
                    link = pg.get_attribute('href')
            if link not in Settings().Read(Settings.CACHE_PAGES):
                print(link)
                self.WritePage(link)
        self.CHROME.quit()

    def SoupHtml(self,url):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:20.0) Gecko/20100101 Firefox/20.0'}

        return requests.get(url, headers=headers).content.decode('utf-8')

    def WritePage(self,page):
        print(page)
        with open(Settings.CACHE_PAGES,"a") as writer:
            writer.write(page+"\n")
    def Exists(self,target):
        try:
            if self.CHROME.find_elements(By.XPATH, target):
                return True
            return False
        except NoSuchElementException:
            return False
class Exfiltrator:
    def __init__(self, chrome,link):
        self.CHROME  = chrome
        self.LINK = link    
        self.CHROME.get(link)                 
        try:
            self.COMPANY_NAME = self.CHROME.find_element(By.XPATH, Settings.HEADER_PATH).get_attribute('innerText')
            self.COMPANY_NUMBER = self.CHROME.find_element(By.XPATH, Settings.HEADER_NUMBER).get_attribute('innerText')
        except NoSuchElementException:
            pass
        print('LOADED ' + self.LINK)
     
    def getBox(self):
        Box = self.CHROME.find_elements(By.XPATH, Settings.BOX_PATH)
        for i in range(0,len(Box)):
            text = self.Compile(str(Box[i].get_attribute('innerText').replace("\n",":")))
            spl = text.split("$")
            CsvCore().Append(spl, Settings.EXPORT)
            print('EXPORTED')
        #self.CHROME.quit()


    def Compile(self,text):
        text= self.Rep(text)
        text= "{} ${} $ {} $ {}".format(self.LINK, self.COMPANY_NAME, self.COMPANY_NUMBER, text)
        colors = list(vars(colorama.Fore).values())
        colored_chars = [random.choice(colors) + char for char in self.COMPANY_NAME]
        for i in tqdm(range(0, 10), total = 10, desc = ''.join(colored_chars)): 

            print('\r')
            time.sleep(.1) 
        return text
    
    def Rep(self,text):
        text = text.replace("Correspondence address:","$")
        text = text.replace("Role ACTIVE:","$")
        text = text.replace("Role RESIGNED:","$")
        text = text.replace("Appointed on:","$")
        text = text.replace("Date of birth:","$")
        text = text.replace("Nationality:","$")
        text = text.replace("Country of residence:","$")
        text = text.replace("Occupation:","$")
        text = text.replace(":","$").replace("\n","")
        text = text.replace("\n","")
        text = text.replace("$$","$")
        text = text.replace(",","")
        text = text.replace("'","")
        text = text.replace("[","")
        text = text.replace("]","")
        return str(text)
    
    def debug(self,data):
        with open('log.txt','a', encoding='utf-8') as writer:
            writer.write(str(data))
            