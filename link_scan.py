from selenium import webdriver
import selenium
from selenium.webdriver.chrome import options
from selenium.webdriver.chrome.options import Options

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


def is_valid_url(url: str)
