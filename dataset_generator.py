import utils.Utils as _utils

# categories = _utils.fetch_all("SELECT * FROM categories")
# print(categories)

# category_id = _utils.insert_website_with_pages('Secteur public', website = '', pages = [])
# print(category_id)

_utils.insert_website_with_pages('Secteur public', 'http://www.parlement.ma', pages = [])
websites = _utils.find_websites()

print(websites)
