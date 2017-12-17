from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import pickle
import os


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


def save_link_data(startword, targetword, tracelist):
    """
    Save the trace data
    :param startword: start word
    :param targetword: target word
    :param tracelist: trace list
    :return:
    """
    # check the dictionary and create it
    if not os.path.exists("save/"):
        os.mkdir("save/")

    # save1 the file
    _dict = {
        "startword": startword,
        "targetword": targetword,
        "tracelist": tracelist
    }
    _file = open("save/trace_%s_%s.dat" % (startword, targetword), "wb+")
    pickle.dump(_dict, _file)


def load_link_data(startword, targetword):
    """
    Load the trace data
    :param startword: start word
    :param targetword: target word
    :return: return None if not found the file
    """
    # load file
    try:
        _file = open("save/trace_%s_%s.dat" % (startword, targetword), "rb")
        return pickle.load(_file)
    except FileNotFoundError:
        # not found file
        return None
