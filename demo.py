from rankedPages import RankedPages

rankedPages = RankedPages('facebook.com')
rankedPagesLinks = rankedPages.get_suggested_links(limit=10)

print(rankedPagesLinks)
