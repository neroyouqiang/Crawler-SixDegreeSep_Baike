from BaikeUrl import *
from utility import *


def start_search_depth(currentbkurl, targetbkurl, linktree, finaltrace, depth):
    """
    Depth-first search
    :param currentbkurl: current url
    :param targetbkurl: target url
    :param linktree: link tree for record
    :param finaltrace: final trace for record
    :param depth: the max level of depth
    :return:
    """

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
            start_search_depth(_bkurl, targetbkurl, linktree[_bkurl.Word], finaltrace, depth - 1)
        except SolutionFound as e:
            # print previous message
            print(e.message)
            # record trace list
            finaltrace.insert(1, _bkurl.Word)
            # raise transition word
            raise SolutionFound("Transition word: %s" % _bkurl.Word)



if __name__ == "__main__":
    # set start and target url
    startbkurl = BaikeUrl("六度分隔理论")
    targetbkurl = BaikeUrl("马萨诸塞州")

    # link tree
    linktree = {}

    # final trace
    finaltrace = []

    # create global variables
    linktree[startbkurl.Word] = {}
    finaltrace.append(startbkurl.Word)

    # print start word
    print("Search Start: %s" % startbkurl.Word)

    # start searching
    try:
        start_search_depth(startbkurl, targetbkurl, linktree[startbkurl.Word], finaltrace, 2)
        print("Solution not found")
    except SolutionFound as e:
        # print previous message
        print(e.message)
        # record trace list
        finaltrace.append(targetbkurl.Word)
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
    print(finaltrace)



