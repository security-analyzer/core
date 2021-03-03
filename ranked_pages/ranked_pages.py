import requests
import re
from bs4 import BeautifulSoup


class RankedPages:

    def __init__(self, website):
        self.website = website

    def _normalize_url(self, link):
        url = re.search('/url?q=(.*)/&sa=', link)
        return url.group(1)
