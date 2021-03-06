# -*- coding: utf-8 -*-
import re
import requests
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup


class PageScrapper:

    def __init__(self, links=[]):
        self._links = links

    def _get_content(self, page):
        return page.content

    def _get_headers(self, page):
        return page.headers

    def get_results(self):
        results = []
        for link in self._links:
            page_infos = requests.get(link)
            page = dict()
            page['link'] = link
            page['headers'] = self._get_headers(page_infos)
            page['content'] = self._get_content(page_infos)
            results.append(page)
        return results
