import utils.Utils as _utils
import crawlers.PageScrapper as _page_scrapper
import scanners.defense_mechanisms.Headers as _headers_scanner
import scanners.defense_mechanisms.Body as _body_scanner
from prettytable import PrettyTable

# categories = _utils.fetch_all("SELECT * FROM categories")
# print(categories)

# category_id = _utils.insert_website_with_pages('Secteur public', website = '', pages = [])
# print(category_id)

# _utils.insert_website_with_pages('Secteur public', 'http://www.parlement.ma', pages = [])
# websites = _utils.find_websites()

_pages = _utils.read_file_items('datasets/ecommerce.txt')[:200]

scan_results_table = PrettyTable()
scan_results_table.field_names = ["Page link", "X-FRAME-OPTIONS", "X-Content-Type-Options", "Strict-Transport-Security", "Secure cookie", "HttpOnly", "Iframe sandboxing", "CSRF Tokens"]

page_scrapper = _page_scrapper.PageScrapper('https://www.arganpalace.com', _pages)
pages = page_scrapper.get_results()

print(pages)

for page in pages:
    page_headers = page.get_headers()
    headers_scanner = _headers_scanner.Headers(page_headers)
    contents_scanner = _body_scanner.Body(page.get_content())
    has_xframe = headers_scanner.has_xframe_defence()
    has_x_content_type_options = headers_scanner.has_x_content_type_options_defence()
    has_hsts = headers_scanner.has_hsts_defence()
    has_secure_cookie = headers_scanner.has_secure_cookie_defence()
    has_http_only = headers_scanner.has_http_only_defence()
    has_iframe_sandboxing = contents_scanner.has_iframe_sandboxing_defence()
    has_csrf_tokens = contents_scanner.has_csrf_tokens_defence()
    scan_results_table.add_row([page.get_link(), has_xframe, has_x_content_type_options, has_hsts, has_secure_cookie, has_http_only, has_iframe_sandboxing, has_csrf_tokens])

print(scan_results_table)

# print(pages)
