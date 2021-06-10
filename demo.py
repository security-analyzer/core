from bs4 import BeautifulSoup
from prettytable import PrettyTable
from src import RankedPages
from src import PageScrapper
from src import Headers
from src import Contents
from src import MixedContentScanner
from src import RemoteJavascriptScanner
from src import XSSProtectionScanner
from src import SSLStrippingFormScanner

# Extract top 10 visited pages
# websites = [
#     {'id': 1, 'url': 'https://www.jumia.ma'},
#     {'id': 4, 'url': 'https://www.decathlon.ma/'},
#     # {'id': 2, 'url': 'https://www.cihnet.co.ma/'},
#     # {'id': 5, 'url': 'https://bpnet.gbp.ma/'},
#     # {'id': 6, 'url': 'http://www.fpbm.ma/new/'},
#     # {'id': 9, 'url': 'https://www.um6p.ma/'}
# ]

# for website in websites:
#     rankedPages = RankedPages(website)
#     ranked_pages_links = rankedPages.get_suggested_pages(limit=10)
#     print('====================' + website['url'] + '==========================')
#     for link in ranked_pages_links:
#         print(link)
#
#
# # Scanning
# websites = [
#     {'id': 1, 'url': 'https://www.jumia.ma'},
#     {'id': 4, 'url': 'https://www.decathlon.ma/'},
#     {'id': 2, 'url': 'https://www.cihnet.co.ma/'},
#     {'id': 5, 'url': 'https://bpnet.gbp.ma/'},
#     {'id': 6, 'url': 'http://www.fpbm.ma/new/'},
#     {'id': 9, 'url': 'https://www.um6p.ma/'}
# ]
# scan_results_table = PrettyTable()
# scan_results_table.field_names = ["Page link", "X-FRAME-OPTIONS", "X-Content-Type-Options", "Strict-Transport-Security", "Secure cookie", "HttpOnly", "Iframe sandboxing", "CSRF Tokens"]
#
# for website in websites:
#     rankedPages = RankedPages(website)
#     ranked_pages_links = rankedPages.get_suggested_pages(limit=3)
#
#     page_scrapper = PageScrapper(ranked_pages_links)
#     pages = page_scrapper.get_results()
#
#     for page in pages:
#         page_headers = page.get_headers()
#         headers_scanner = Headers(page_headers)
#         contents_scanner = Contents(page.get_content())
#         has_xframe = headers_scanner.has_xframe_defence()
#         has_x_content_type_options = headers_scanner.has_x_content_type_options_defence()
#         has_hsts = headers_scanner.has_hsts_defence()
#         has_secure_cookie = headers_scanner.has_secure_cookie_defence()
#         has_http_only = headers_scanner.has_http_only_defence()
#         has_iframe_sandboxing = contents_scanner.has_iframe_sandboxing_defence()
#         has_csrf_tokens = contents_scanner.has_csrf_tokens_defence()
#         scan_results_table.add_row([page.get_link(), has_xframe, has_x_content_type_options, has_hsts, has_secure_cookie, has_http_only, has_iframe_sandboxing, has_csrf_tokens])
#
# print(scan_results_table)


page_scrapper = PageScrapper(['https://spatie.be'])
page = page_scrapper.get_results()[0]
#
# # soup = BeautifulSoup(page.get_content(), features="html.parser")
# # iframes = soup.select('iframe')
# # print(iframes)
# # if len(iframes) == 0:
# #     print('There\'s No iframe tag in this page')
# #
# # for iframe in iframes:
# #     if not iframe.get('sandboxs') is None:
# #         print('here')
# #     else:
# #         print('not here')
#
# # HSTH
# # HtmlUnit browser
# # burp suite
# # https://gf.dev/xss-protection-test
# # kalilinu
#
#
# # contents_scanner = Contents(page.get_content())
# # has_iframe_sandboxing = contents_scanner.has_csrf_tokens_defence()
# # print(has_iframe_sandboxing)
#
# mixed_content_scanner = MixedContentScanner(page.get_content())
# has_iframe_sandboxing = mixed_content_scanner.has_mixed_content_vuls()
# print(has_iframe_sandboxing)

# remote_javascript_scanner = RemoteJavascriptScanner(page.get_content(), 'https://spatie.be')
# has_remote_javascript_vuls = remote_javascript_scanner.has_remote_javascript_vuls()
# print(has_remote_javascript_vuls)
# print(page.get_headers())
# xxs_protection_scanner = XSSProtectionScanner(page.get_headers())
# has_xxs_protection_vuls = xxs_protection_scanner.has_xxs_protection_vuls()
# print(has_xxs_protection_vuls)


ssl_striping_form_scanner = SSLStrippingFormScanner(page.get_content())
has_ssl_striping_form_vuls = ssl_striping_form_scanner.has_ssl_tripping_form_vuls()
print(has_ssl_striping_form_vuls)
