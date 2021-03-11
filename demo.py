from src import RankedPages
from src import PageScrapper
import utils.database as db_utils


websites = db_utils.fetch_all('SELECT * FROM websites')

for website in websites:
    print('Start crawling on: ' + str(website[1]))
    rankedPages = RankedPages({'id': website[0], 'url': website[1]})
    rankedPagesLinks = rankedPages.get_suggested_pages(limit=10)
    rankedPages.save_suggested_pages(limit=10)

    website_pages = db_utils.fetch_all('SELECT * FROM pages WHERE website_id = ' + str(website[0]))
    page_scrapper = PageScrapper(website_pages)
    page_scrapper.save_results()
