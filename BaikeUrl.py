import re
import urllib.parse


class BaikeUrl:
    """
    The manager of Baike url
    """
    # domain name of Baike
    DomainName = "baike.baidu.com"

    # current url
    FullUrl = None
    # Baike word of the url
    Word = None
    # postfix of the url
    Others = None
    # Baike full word of the url. Inluding "Word" and "Others"
    FullWord = None

    def __init__(self, url):
        # regular expressions
        pattern_url1 = re.compile(r"^(?:(?:(?:https?://)?" + self.DomainName + ")?/)?item/([^/?]*)([/?].*)?")
        pattern_url2 = re.compile(r"([^/]*)(/.*)?")

        # url decode
        url = urllib.parse.unquote(url)

        # match and extract infos
        matches = pattern_url1.search(url)
        if not matches:
            matches = pattern_url2.search(url)

        if matches:
            if matches[1]:
                self.Word = matches[1]
            else:
                self.Word = ""
            if matches[2]:
                self.Others = matches[2]
            else:
                self.Others = ""
        else:
            self.Word = ""
            self.Others = ""

        # make up the full url
        self.FullUrl = "https://" + self.DomainName + "/item/" + urllib.parse.quote(self.Word) + self.Others
        self.FullWord = self.Word + self.Others

        #print("Result:")
        #print(self.BaikeWord)
        #print(self.BaikeOthers)


