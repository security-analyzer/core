import json
from urllib.parse import quote
from Wappalyzer import Wappalyzer, WebPage
import mysql.connector
from requests.packages import urllib3


# Database config
database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="web_crawler"
)

# Shared utils
def dict_to_json(dictionary):
    return json.dumps(dictionary, indent = 4)


def json_to_array(json_values):
    return json.loads(json_values)


def json_to_dict(json_object):
    return json.loads(json_object)


def contains_one_of(word, terms):
    for term in terms:
        if term in word:
            return True
    return False


def extract_server(url):
    webpage = WebPage.new_from_url(url)
    wappalyzer = Wappalyzer.latest()
    techs = wappalyzer.analyze_with_versions_and_categories(webpage)
    # print(techs)
    for key in techs:
        if 'Web servers' in techs[key]['categories']:
            version = False
            try:
                version = techs[key]['versions'][techs[key]['categories'].index('Web servers')]
            except:
                version = False

            return {'server': key, 'version': version}
    return False


def extract_cms(url):
    webpage = WebPage.new_from_url(url)
    wappalyzer = Wappalyzer.latest()
    techs = wappalyzer.analyze_with_versions_and_categories(webpage)
    for key in techs:
        if 'CMS' in techs[key]['categories']:
            version = False
            try:
                version = techs[key]['versions'][techs[key]['categories'].index('CMS')]
            except:
                version: False
            return {'CMS': key, 'version': version}
    return False


def accepted_url(target, nlink):
    target_domain = target.replace('http://', '').replace('https://', '')
    target_domain_without_www = target_domain.replace('www.', '')
    page_url = nlink.split('/')[-1]
    if (not nlink.endswith('.pdf') and (not nlink.endswith('.PDF')) and (not nlink.endswith('.rtf')) and (not nlink.endswith('.pptx')) and not nlink.endswith('.docx')  and not nlink.endswith('.doc') and not nlink.endswith('.csv') and not nlink.endswith('.xlsx') and ('accounts.google.com') not in nlink) and (nlink.startswith('http://' + target_domain) or nlink.startswith('https://' + target_domain) or nlink.startswith('http://www.' + target_domain_without_www) or nlink.startswith('https://www.' + target_domain_without_www)) and ('.pdf' not in page_url) and ('download' not in nlink):
        return True
    return False


def read_file_items(file_path):
    file = open(file_path, "r")
    return file.readlines()


def fetch_all(query):
    query_cursor = database.cursor(buffered=True)
    query_cursor.execute(query)
    items = query_cursor.fetchall()
    return items


def fetch_one(query):
    query_cursor = database.cursor(buffered=True)
    query_cursor.execute(query)
    item = query_cursor.fetchone()
    return item


def commit_query(query):
    query_cursor = database.cursor()
    query_cursor.execute(query)
    database.commit()


def find_category_by_name(category_name):
    query = "SELECT * FROM categories WHERE name = '" + str(category_name) + "'"
    return fetch_one(query)


def find_website_by_url(url):
    query = "SELECT * FROM websites WHERE url = '" + str(url) + "'"
    return fetch_one(query)


def find_website_by_category_name(category_name):
    query = "SELECT websites.* FROM websites WHERE websites.category_id IN (SELECT categories.id FROM categories WHERE categories.name = '" + str(category_name) + "')"
    return fetch_one(query)


def find_websites_by_category_name(category_name):
    query = "SELECT websites.id, websites.url FROM websites WHERE websites.category_id IN (SELECT categories.id FROM categories WHERE categories.name = '" + str(category_name) + "')"
    websites = fetch_all(query)
    website_with_pages = []
    for website in websites:
        query = "SELECT url FROM pages WHERE website_id = '" + str(website[0]) + "'"
        website_pages = fetch_all(query)
        pages = []
        for page in website_pages:
            pages.append(page[0])
        website_with_pages.append({'website': website[1], 'pages': pages})
    return website_with_pages


def find_web_pages_by_category_name(category_name):
    website = find_website_by_category_name(category_name)
    if website:
        query = "SELECT * FROM pages WHERE website_id = '" + str(website[0]) + "'"
        return fetch_all(query)

    return []


def insert_website_with_pages(category_name, website_url = '', pages = []):
    category = find_category_by_name(category_name)
    if not category:
        query = "INSERT INTO categories (name) VALUES ('" + category_name + "')"
        commit_query(query)
        category = find_category_by_name(category_name)

    website = find_website_by_url(website_url)
    if not website:
        query = "INSERT INTO websites (url, category_id) VALUES ('" + str(website_url) + "', '" + str(category[0]) + "')"
        commit_query(query)
        website = find_website_by_url(website_url)
    
    for page in pages:
        page = page.replace("'", "\\'")
        print(page)
        query = "INSERT INTO pages (url, website_id) VALUES ('" + str(page) + "', '" + str(website[0]) + "')"
        commit_query(query)


def find_websites():
    query = "SELECT * FROM websites"
    return fetch_all(query)

