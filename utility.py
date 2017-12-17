from urllib.request import urlopen
from bs4 import BeautifulSoup
import re


class SolutionFound(RuntimeError):
    """
    "Error" used to indicates finding the solution
    """
    def __init__(self, message):
        self.message = message


def get_baike_urls(url):
    """
    Collect the Baike urls in the given page
    :param url: url of the given page
    :return: Baike url list
    """
    # get page and parse html
    _response = urlopen(url)
    _bsobj = BeautifulSoup(_response, "html.parser")

    # collect all the Baike urls
    _bkurls = {_link["href"] for _link in _bsobj.findAll("a", href=re.compile(r"^/item/.+"))}
    return _bkurls
