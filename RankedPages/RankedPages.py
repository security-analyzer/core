import requests
import re
from bs4 import BeautifulSoup


GOOGLE_SEARCH_ENDPOINT = 'https://www.google.com/search?num=40&lr=lang_en&q='


class RankedPages:

    def __init__(self, website):
        self.website = website

    def _normalize_url(self, link):
        url = re.search('/url?q=(.*)/&sa=', link)
        return link

    def _normalize_soup_links(self, soup_links):
        links = []
        for link in soup_links:
            href = link.get('href')
            links.append(self._normalize_url(href))
        return links

    def get_suggested_links(self):
        link = GOOGLE_SEARCH_ENDPOINT + self.website
        results_page = requests.get(link)
        soup = BeautifulSoup(results_page.content, 'html.parser')
        soup_links = soup.select('div.kCrYT > a')
        links = self._normalize_soup_links(soup_links)
        return links
