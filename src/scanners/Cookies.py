# -*- coding: utf-8 -*-
import re
import requests
from bs4 import BeautifulSoup
import utils.database as db_utils


class Cookies:

    def __init__(self, page):
        self._page = page


    def _get_content(self):
        return str(_page.content).replace("'", "")


    def _get_headers(self, page):
        return str(_page.headers).replace("'", "")