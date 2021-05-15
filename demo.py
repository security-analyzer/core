from prettytable import PrettyTable
from src import RankedPages
from src import PageScrapper
from src import Headers

# rankedPages = RankedPages({'id': 1, 'url': 'https://www.jumia.ma'})
# rankedPagesLinks = rankedPages.get_suggested_pages(limit=10)
# print(rankedPagesLinks)

scan_results_table = PrettyTable()
scan_results_table.field_names = ["Page link", "X-FRAME-OPTIONS", "X-Content-Type-Options", "Strict-Transport-Security", "Secure cookie (HttpOnly)"]

ranked_pages_links = [
    'https://www.jumia.ma/',
    'https://www.jumia.ma/salvatore/',
    'https://massarservice.men.gov.ma/waliye/Account',
    'https://www.cihnet.co.ma/',
    'https://www.jumia.ma/diamantine/',
    'https://www.jumia.ma/oukitel/',
    'https://www.jumia.ma/kyocera/',
    'https://www.jumia.ma/monogotas/'
]

page_scrapper = PageScrapper(ranked_pages_links)
pages = page_scrapper.get_results()

# my_table.add_row([1, "Bob", 6, 11])
# my_table.add_row([2, "Freddy", 4, 10])
# my_table.add_row([3, "John", 7, 13])

for page in pages:
    page_headers = page.get_headers()
    headers_scanner = Headers(page_headers)
    has_xframe = headers_scanner.has_xframe_defence()
    has_x_content_type_options = headers_scanner.has_x_content_type_options_defence()
    has_hsts = headers_scanner.has_hsts_defence()
    has_http_only = headers_scanner.has_http_only_defence()
    scan_results_table.add_row([page.get_link(), has_xframe, has_x_content_type_options, has_hsts, has_http_only])

print(scan_results_table)

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




# 'Date': 'Fri, 14 May 2021 16:03:51 GMT', 'Content-Type': 'text/html; charset=utf-8', 'Transfer-Encoding': 'chunked', 'Connection': 'keep-alive', 'Vary': 'Accept-Encoding, X-Device, X-Language, X-ABTests, X-Scenario, X-OS', 'Expires': 'Thu, 19 Nov 1981 08:52:00 GMT', 'Cache-Control': 'no-store, no-cache, must-revalidate, no-transform', 'Pragma': 'no-cache', 'Set-Cookie': 'newsletter=1; expires=Thu, 14-May-2026 15:03:51 GMT; path=/; domain=.jumia.ma, sb-closed=true; expires=Fri, 21-May-2021 15:03:51 GMT; path=/; domain=.jumia.ma, ABTests=%5B%7B%22name%22%3A%22SearchABTest%22%2C%22scenario%22%3A%22popularity_rerank_excl_size%22%2C%22updatedAt%22%3A1619161313%7D%2C%7B%22name%22%3A%22MLP%22%2C%22scenario%22%3A%22A%22%2C%22updatedAt%22%3A1617096876%7D%5D; expires=Sat, 14-May-2022 15:03:51 GMT; path=/; domain=.jumia.ma, SOLSESSID=d452d246b10c62c5fc676c05e2b7af1b; expires=Fri, 14-May-2021 16:27:51 GMT; path=/; domain=.jumia.ma; secure; httponly; samesite=Lax, userLanguage=fr_MA; expires=Sat, 14-May-2022 15:03:51 GMT; path=/; domain=.jumia.ma, __cf_bm=677012a0686911eb82ab23347879263e1c5e8df3-1621008231-1800-AZcfkVTPQg3ccHARHXvVBIu0iyHrn0DBDd9OsxnJ0V1Vr4OMzRqhJrIaNtm4YFAR/EykT6w+VtXo4laLF/FdhXE=; path=/; expires=Fri, 14-May-21 16:33:51 GMT; domain=.jumia.ma; HttpOnly; Secure; SameSite=None', 'X-Cacheable': 'NO:Not Cacheable', 'Age': '0', 'X-Proxy': 'varnish-5b6dc5fd99-jx87t', 'X-Cache': 'MISS', 'X-Cache-Hits': '0', 'Access-Control-Allow-Origin': '*', 'X-LB': 'nginx-aws-c01', 'X-XSS-Protection': '1; mode=block', 'Referrer-Policy': 'strict-origin-when-cross-origin', 'X-Content-Type-Options': 'nosniff', 'X-Frame-Options': 'SAMEORIGIN', 'cf-oa': '1', 'Content-Encoding': 'gzip', 'CF-Cache-Status': 'DYNAMIC', 'cf-request-id': '0a0d37c33b0000ff30e3882000000001', 'Expect-CT': 'max-age=604800, report-uri="https://report-uri.cloudflare.com/cdn-cgi/beacon/expect-ct"', 'Server': 'cloudflare', 'CF-RAY': '64f55be52975ff30-MAD'
