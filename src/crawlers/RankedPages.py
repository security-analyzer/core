# -*- coding: utf-8 -*-
import re
import requests
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from url_normalize import url_normalize

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
                if(not url.endswith('.pdf') and not url.endswith('.docx') and not url.endswith('.csv') and not url.endswith('.xlsx')):
                    links.append(url)
        return links


    def _google_serach(self):
        url = GOOGLE_SEARCH_ENDPOINT + self._website['url']
        results_page = requests.get(url)
        return BeautifulSoup(results_page.content, 'html.parser')


    def get_suggested_pages(self, limit=LIMIT_LINKS):
        soup_links = self._google_serach().select('div.kCrYT > a')
        return self._normalize_soup_links(soup_links, limit)


    def save_suggested_pages(self, limit=LIMIT_LINKS):
        website_links = self.get_suggested_pages(limit)
        for page_link in website_links:
            query = "INSERT INTO pages (url, website_id) VALUES ('"+ str(page_link) +"', '"+ str(self._website['id']) +"')"
            db_utils.commit_query(query)
