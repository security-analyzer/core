import requests
from models.Page import Page
from crawlers.RankedPages import RankedPages
from crawlers.PageScrapper import PageScrapper

rankedPages = RankedPages('http://www.parlement.ma')
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

# http://www.parlement.ma
# http://www.conseil-constitutionnel.ma
# http://www.diplomatie.ma
# http://www.justice.gov.ma
# www.habous.gov.ma
# http://www.minculture.gov.ma
# http://www.tourisme.gov.ma
# http://www.sante.gov.ma
# http://www.mcrp.gov.ma
# http://www.mem.gov.ma
# http://www.water.gov.ma
# http://www.mincom.gov.ma
# http://www.mcinet.gov.ma
# http://www.mmsp.gov.ma
# http://www.marocainsdumonde.gov.ma


# print(pageScrapper.get_results())
ranked_pages_links = rankedPages.get_suggested_pages(limit=100)
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