# -*- coding: utf-8 -*-
import re
import requests
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from src.models.Page import Page


class PageScrapper:

    def __init__(self, website_pages=[]):
        self._website_pages = website_pages

    def _get_content(self, page):
        return str(page.content).replace("'", "")

    def _get_headers(self, page):
        return page.headers

    def get_results(self):
        results = []
        for page_link in self._website_pages:
            page_infos = requests.get(page_link)
            page = Page(website=page_link, link=page_link, headers=self._get_headers(page_infos), content=self._get_content(page_infos))
            results.append(page)
        return results

    def save_results(self):
        for page_link in self._website_pages:
            page_infos = requests.get(page_link[1])
            query = "UPDATE pages SET headers = '" + self._get_headers(page_infos) + "', content = '" + self._get_content(page_infos) + "' WHERE id = " + str(page_link[0])
            db_utils.commit_query(query)
