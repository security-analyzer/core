# -*- coding: utf-8 -*-
import re
import ssl
import requests
from bs4 import BeautifulSoup
from url_normalize import url_normalize
from url_normalize.tools import unquote
ssl._create_default_https_context = ssl._create_unverified_context

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
                        '.csv') and not nlink.endswith('.xlsx') and (target in nlink) and ('accounts.google.com') not in nlink):
                    url_google.append(nlink)
            
            if len(raw_links) < 2:
                # Verify if Google's Captcha has caught us!
                print("No more results...")
                return url_google

        return url_google[:limit]


    def get_suggested_pages(self, limit=LIMIT_LINKS):
        return self._google_search(limit)