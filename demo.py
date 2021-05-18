from prettytable import PrettyTable
from src import RankedPages
from src import PageScrapper
from src import Headers

websites = [
    {'id': 1, 'url': 'https://www.jumia.ma'},
    {'id': 4, 'url': 'https://www.decathlon.ma/'},
    {'id': 2, 'url': 'https://www.cihnet.co.ma/'},
    {'id': 5, 'url': 'https://bpnet.gbp.ma/'},
    {'id': 6, 'url': 'http://www.fpbm.ma/new/'},
    {'id': 9, 'url': 'https://www.um6p.ma/'}
]

scan_results_table = PrettyTable()
scan_results_table.field_names = ["Page link", "X-FRAME-OPTIONS", "X-Content-Type-Options", "Strict-Transport-Security", "Secure cookie", "HttpOnly"]

for website in websites:
    rankedPages = RankedPages(website)
    ranked_pages_links = rankedPages.get_suggested_pages(limit=3)

    page_scrapper = PageScrapper(ranked_pages_links)
    pages = page_scrapper.get_results()

    for page in pages:
        page_headers = page.get_headers()
        headers_scanner = Headers(page_headers)
        has_xframe = headers_scanner.has_xframe_defence()
        has_x_content_type_options = headers_scanner.has_x_content_type_options_defence()
        has_hsts = headers_scanner.has_hsts_defence()
        has_secure_cookie = headers_scanner.has_secure_cookie_defence()
        has_http_only = headers_scanner.has_http_only_defence()
        scan_results_table.add_row([page.get_link(), has_xframe, has_x_content_type_options, has_hsts, has_secure_cookie, has_http_only])

print(scan_results_table)

