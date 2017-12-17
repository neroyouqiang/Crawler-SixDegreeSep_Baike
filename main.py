from BaikeUrl import *
from myfuncs import *


class SolutionFound(RuntimeError):
    """
    "Error" used to indicates finding the solution
    """
    def __init__(self, message):
        self.message = message


def start_search(currentbkurl, targetbkurl, linktree, depth):
    """

    :param currentbkurl:
    :param targetbkurl:
    :return:
    """
    global TraceList

    # if the search is deep enough
    if depth == 0:
        return

    # get Baike urls in current page
    _urls = get_baike_urls(currentbkurl.FullUrl)
    _bkurls = [BaikeUrl(_url) for _url in _urls]
    _words = [_bkurl.Word for _bkurl in _bkurls]

    # create the branch
    for _bkurl in _bkurls:
        linktree[_bkurl.Word] = {}

    # search for target url
    if targetbkurl.Word in _words:
        raise SolutionFound("Solution Found!")

    # recursive search
    for _bkurl in _bkurls:
        try:
            start_search(_bkurl, targetbkurl, linktree[_bkurl.Word], depth - 1)
        except SolutionFound as e:
            # print previous message
            print(e.message)
            # record trace list
            TraceList.insert(1, _bkurl.Word)
            # raise transition word
            raise SolutionFound("Transition word: %s" % _bkurl.Word)

    # return the link tree
    # if depth > 1:
    #     print(_linkree)
    # return _linkree


# global link tree
LinkTree = {}

# global trace list
TraceList = []

if __name__ == "__main__":
    # set start and target url
    startbkurl = BaikeUrl("六度分隔理论")
    targetbkurl = BaikeUrl("马萨诸塞州")

    # create global variables
    LinkTree[startbkurl.Word] = {}
    TraceList.append(startbkurl.Word)

    # print start word
    print("Search Start: %s" % startbkurl.Word)

    # start searching
    try:
        start_search(startbkurl, targetbkurl, LinkTree[startbkurl.Word], 2)
        print("Solution not found")
    except SolutionFound as e:
        # print previous message
        print(e.message)
        # record trace list
        TraceList.append(targetbkurl.Word)
        # print end word
        print("Search End: %s" % targetbkurl.Word)

    # print the link tree
    # print(LinkTree)
    # print(LinkTree[TraceList[0]])
    # print(LinkTree[TraceList[0]][TraceList[1]])
    # print(LinkTree[TraceList[0]][TraceList[1]][TraceList[2]])

    # print the trace list
    print("")
    print("The trace list is:")
    print(TraceList)



