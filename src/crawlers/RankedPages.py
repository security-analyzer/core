# -*- coding: utf-8 -*-
import re
import ssl
import requests
from bs4 import BeautifulSoup
from url_normalize import url_normalize
from urllib.request import Request, urlopen
ssl._create_default_https_context = ssl._create_unverified_context
from requests.packages.urllib3.exceptions import InsecureRequestWarning

GOOGLE_SEARCH_ENDPOINT = 'https://www.google.com/search?num=1008&q=site:'
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

    def _normalize_soup_links(self, soup_links, limit=LIMIT_LINKS):
        links = []
        for link in soup_links:
            if len(links) < limit:
                href = link.get('href')
                url = self._normalize_url(href)
                if (not url.endswith('.pdf') and not url.endswith('.docx') and not url.endswith(
                        '.csv') and not url.endswith('.xlsx')):
                    links.append(url)
        return links

    def _google_serach(self):
        url = GOOGLE_SEARCH_ENDPOINT + self._website['url']
        results_page = requests.get(url)
        return BeautifulSoup(results_page.content, 'html.parser')

    def search_google(num, target, option):
        start_page = 0
        nlink = ""
        url_google = []
        user_agent = {'User-agent': 'Mozilla5.0'}
        contador = 100
        i = 0
        while i < num:
            i += 1
            search_google = "https://www.google.com/search?q=+site:" + target + " -filetype:pdf&filter=0&start=" + str(
                start_page) + "&num=" + str(contador)
            print(search_google)
            contador += 100
            start_page += 100

            try:
                response = requests.get(search_google, headers=user_agent)
            except requests.exceptions.RequestException as e:
                print("\nError connection to server!")  # + response.url,
                pass
            except requests.exceptions.ConnectTimeout as e:
                print("\nError Timeout", target)
                pass

            # Parser HTML of BeautifulSoup
            soup = BeautifulSoup(response.text, "html.parser")
            if response.text.find("Our systems have detected unusual traffic") != -1:
                print("CAPTCHA detected - Plata or captcha !!!Maybe try form another IP...")
                url_google.append("CAPTCHA detected - Plata or captcha !!!Maybe try form another IP...")
                return url_google
            # Parser url's throught regular expression
            raw_links = soup.find_all("a", href=re.compile("(?<=/url\?q=)(htt.*://.*)"))
            # print raw_links
            for link in raw_links:
                # Cache Google
                if link["href"].find("webcache.googleusercontent.com") == -1:
                    nlink = link["href"].replace("/url?q=", "")
                # Parser likns
                nlink = re.sub(r'&sa=.*', "", nlink)
                # nlink = urllib.parse.unquote(nlink).decode('utf8')
                url_google.append(nlink)
            if len(raw_links) < 2:
                # Verify if Google's Captcha has caught us!
                print("No more results...")
                url_google.append("No more results")
                # captcha = True
                return url_google

        return url_google

    def get_suggested_pages(self, limit=LIMIT_LINKS):
        soup_links = self._google_serach().select('div.kCrYT > a')
        return self._normalize_soup_links(soup_links, limit)
