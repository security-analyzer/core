import requests
from models.Page import Page
from crawlers.RankedPages import RankedPages
from crawlers.PageScrapper import PageScrapper

rankedPages = RankedPages('http://www.fpbm.ma/new/')
# # pageScrapper = PageScrapper('http://www.fpbm.ma/new/', [
# #     'http://www.fpbm.ma/new/concours/',
# #     'http://www.fpbm.ma/new/exam/liste.php',
# #     'http://www.fpbm.ma/new/lef/LEF2020.php',
# #     'http://www.fpbm.ma/new/locaux/suivredemande.php',
# #     'http://www.fpbm.ma/new/getsec/login.php',
# #     'http://www.fpbm.ma/new/exam/index.php',
# #     'http://www.fpbm.ma/new/locaux/login.php',
# #     'http://www.fpbm.ma/new/exam/login.php',
# #     'http://www.fpbm.ma/new/amo.php',
# #     'http://www.fpbm.ma/new/formations.php',
# # ])

# print(pageScrapper.get_results())
ranked_pages_links = rankedPages.get_suggested_pages(limit=200)
print('====================' + 'http://www.fpbm.ma/new/' + '==========================')
print(len(ranked_pages_links))
for link in ranked_pages_links:
    print(link)

# from urllib.parse import urlencode, urlunparse
# from urllib.request import urlopen, Request
# from bs4 import BeautifulSoup

# query = "site:http://www.fpbm.ma/new/"
# url = urlunparse(("https", "www.bing.com", "/search", "", urlencode({"q": query}), ""))
# custom_user_agent = "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0"
# req = Request(url, headers={"User-Agent": custom_user_agent})
# page = urlopen(req)

# # Further code I've left unmodified
# soup = BeautifulSoup(page.read(), 'html.parser')
# links = soup.findAll("a")
# for link in links:
#     print(link["href"])