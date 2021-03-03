from RankedPages import RankedPages

rankedPages = RankedPages('facebook.com')
l = rankedPages.get_suggested_links()

print(l)
