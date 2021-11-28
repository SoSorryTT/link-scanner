from typing import List
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests

def get_links(url: str):
    """Find all links on page at the given url.

    Return:
        A list of all unique hyperlinks on the page,
        without page fragments or query parameters.
    """
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    if url == []:
        return []
    else:
        selenium = webdriver.Chrome(options=options)
        selenium.get(url)
        link = selenium.find_element_by_xpath("//a[@href]")
        for i in link:
            use_link = i.get_attribute("href")
            use_link = link.split("#")
            use_link = link[0].split("?")
            if use_link[0] not in [] and use_link[0] != "":
                return use_link[0]


def is_valid_url(url: str):
    """Check is url valid or invalid.

    Args:
        url(str): String of url.

    Return:
        bool: return True if the url is valid.
    """
    try:
        response = requests.head(url)
    except (requests.ConnectionError, requests.ConnectTimeout)
        return False
    if not response.ok:
        return False
    return True


def invalid_urls(urllist: List) -> List[str]:
    """Validate the urls in urllist and return a new list containing
    the invalid or unreachable urls.
    """
    invalid_url = []
    for url in urllist:
        if not is_valid_url(url):
            invalid_url.append(url)
    return invalid_url

