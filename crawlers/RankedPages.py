# -*- coding: utf-8 -*-
import time
import re
import ssl
import requests
import urllib.parse
from bs4 import BeautifulSoup
from url_normalize import url_normalize
from url_normalize.tools import unquote
ssl._create_default_https_context = ssl._create_unverified_context
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

LIMIT_LINKS = 20

class RankedPages:

    def __init__(self, website):
        self._website = website


    def _normalize_url(self, link):
        try:
            url = re.search(r'url\?q=(.*?)&sa=', link).group(1)
        except:
            url = link
        return url_normalize(url)


    def _google_search(self, limit):
        start_page = 0
        nlink = ""
        url_google = []
        user_agent = {'User-agent': 'Mozilla5.0'}
        contador = 100
        target = self._website
        target_domain = target.replace('http://').replace('https://')

        while len(url_google) < limit:
            search_google = "https://www.google.com/search?q=+site:" + target + " -filetype:pdf&filter=0&start=" + str(
                start_page) + "&num=" + str(contador)
            contador += 100
            start_page += 100

            try:
                response = requests.get(search_google, headers=user_agent)
            except requests.exceptions.RequestException as e:
                print("\nError connection to server!")
                return url_google
            except requests.exceptions.ConnectTimeout as e:
                print("\nError Timeout", target)
                return url_google

            # Parser HTML of BeautifulSoup
            soup = BeautifulSoup(response.text, "html.parser")
            if response.text.find("Our systems have detected unusual traffic") != -1:
                print("Our systems have detected unusual traffic")
                return url_google
            
            # Parser url's throught regular expression
            raw_links = soup.find_all("a", href=re.compile("(?<=/url\?q=)(htt.*://.*)"))
            
            for link in raw_links:
                # Cache Google
                if link["href"].find("webcache.googleusercontent.com") == -1:
                    nlink = link["href"].replace("/url?q=", "")
                
                # Parser likns
                nlink = re.sub(r'&sa=.*', "", nlink)
                
                nlink = unquote(nlink).decode('utf8')

                if (not nlink.endswith('.pdf') and not nlink.endswith('.docx') and not nlink.endswith(
                        '.csv') and not nlink.endswith('.xlsx') and (target_domain in nlink) and ('accounts.google.com') not in nlink):
                    print(nlink)
                    url_google.append(nlink)
            
            if len(raw_links) < 2:
                # Verify if Google's Captcha has caught us!
                print("No more results...")
                return url_google
            
        return url_google[:limit]


    def _bing_search(self, limit):
        browser_options = Options()
        browser_options.headless = False  # You can set 'False' if you need disable background mode
        browser = webdriver.Firefox(options=browser_options)
        dork=["site:","-site:","filetype:","intitle:","intext:"]
        target = self._website
        urls_final = []
        try:
            serach_url = "https://www.bing.com/search?q=site:" + target + "&count=100"#+dork[0]+target+"&count=100&go=Buscar"
            browser.get(serach_url)
            page_html = browser.page_source
            soup = BeautifulSoup(page_html, "html.parser")
            links = soup.find_all("a")
            for link in links:
                nlink = link.get('href')
                nlink = unquote(nlink).decode('utf8')
                if (not nlink.endswith('.pdf') and not nlink.endswith('.docx') and not nlink.endswith(
                        '.csv') and not nlink.endswith('.xlsx') and ('accounts.google.com') not in nlink):
                    urls_final.append(nlink)
            while (len(urls_final) < limit):
                urls_final = self.parser_html(page_html)
        except Exception as e:
            pass
        
        return urls_final

    
    def parser_html(content):
        urls = []
        urls_clean = []
        urls_final =[]
        delete_bing=["microsoft", "msn", "bing"]
        soup = BeautifulSoup(content, 'html.parser')
        
        try:
            for link in soup.find_all('a'):
                print(link.get('href'))
                if (urllib.parse(link.get('href')) != '' and urllib.parse(link.get('href'))[1].strip() != ''):	
                    print(urllib.parse(link.get('href')))
                    urls.append(urllib.parse(link.get('href'))[1])
                
                # Delete duplicates
                [urls_clean.append(i) for i in urls if not i in urls_clean] 
                
                # Delete not domains belongs to target
                for value in urls_clean:
                    if (value.find(delete_bing[0])  == -1):
                        if (value.find(delete_bing[1])  == -1):
                            if (value.find(delete_bing[2])  == -1):
                                urls_final.append(value)
        except Exception as e:
            pass

        return urls_final


    def get_suggested_pages(self, limit=LIMIT_LINKS):
        return self._google_search(limit)