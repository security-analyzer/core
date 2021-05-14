from src import RankedPages
from src import PageScrapper
# import utils.database as db_utils

# rankedPages = RankedPages({'id': 1, 'url': 'https://www.jumia.ma'})
# rankedPagesLinks = rankedPages.get_suggested_pages(limit=10)
# print(rankedPagesLinks)

rankedPagesLinks = ['https://www.jumia.ma/', 'https://www.jumia.ma/salvatore/', 'https://www.jumia.ma/diamantine/', 'https://www.jumia.ma/oukitel/', 'https://www.jumia.ma/kyocera/', 'https://www.jumia.ma/monogotas/', 'https://www.jumia.ma/calin/', 'https://www.jumia.ma/logitech/', 'https://www.jumia.ma/lesieur/', 'https://www.jumia.ma/castrol/']

page_scrapper = PageScrapper(rankedPagesLinks)
pages = page_scrapper.get_results()[:1]

for page in pages:
    print(page.get_headers()['Date'])

# websites = db_utils.fetch_all('SELECT * FROM websites')
#
# for website in websites:
#     print('Start crawling on: ' + str(website[1]))
#     rankedPages = RankedPages({'id': website[0], 'url': website[1]})
#     rankedPagesLinks = rankedPages.get_suggested_pages(limit=10)
#     rankedPages.save_suggested_pages(limit=10)
#
#     website_pages = db_utils.fetch_all('SELECT * FROM pages WHERE website_id = ' + str(website[0]))
#     page_scrapper = PageScrapper(website_pages)
#     page_scrapper.save_results()
