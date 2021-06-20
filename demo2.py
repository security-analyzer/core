from models.Page import Page
from crawlers.RankedPages import RankedPages
from crawlers.PageScrapper import PageScrapper

# rankedPages = RankedPages('http://www.fpbm.ma/new/')
pageScrapper = PageScrapper('http://www.fpbm.ma/new/', [
    'http://www.fpbm.ma/new/concours/',
    'http://www.fpbm.ma/new/exam/liste.php',
    'http://www.fpbm.ma/new/lef/LEF2020.php',
    'http://www.fpbm.ma/new/locaux/suivredemande.php',
    'http://www.fpbm.ma/new/getsec/login.php',
    'http://www.fpbm.ma/new/exam/index.php',
    'http://www.fpbm.ma/new/locaux/login.php',
    'http://www.fpbm.ma/new/exam/login.php',
    'http://www.fpbm.ma/new/amo.php',
    'http://www.fpbm.ma/new/formations.php',
])

print(pageScrapper.get_results())
# ranked_pages_links = rankedPages.get_suggested_pages(limit=10)
# print('====================' + 'http://www.fpbm.ma/new/' + '==========================')
# for link in ranked_pages_links:
#     print(link)