from src import RankedPages
from src import PageScrapper

rankedPages = RankedPages('jumia.com')
rankedPagesLinks = rankedPages.get_suggested_links(limit=10)

print(rankedPagesLinks)


page_scrapper = PageScrapper(rankedPagesLinks)
results = page_scrapper.get_results()

print(results[0]['headers'])
