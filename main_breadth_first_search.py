from BaikeUrl import *
from utility import *


def start_search_breadth(startbkurl, targetbkurl):
    """
    Breadth-first search
    :param currentbkurl: current url
    :param targetbkurl: target url
    :return:
    """
    # trace waiting for search
    _tracequeue = [[startbkurl.Word]]

    # words that has been searched
    _wordsearched = set()

    # count the search time
    _searchtime = 0

    while len(_tracequeue):
        # add search time
        _searchtime += 1

        # get searching word
        _currenttrace = _tracequeue.pop(0)
        _currentbkurl = BaikeUrl(_currenttrace[-1])

        # print current searching info
        print("%d. Searching trace: %s -> ?" % (_searchtime, " -> ".join(_currenttrace)))

        # check if this word has been searched
        if _currentbkurl.FullWord in _wordsearched:
            continue
        else:
            _wordsearched.add(_currentbkurl.FullWord)

        # get urls
        _urls = get_baike_urls(_currentbkurl.FullUrl)
        _bkurls = [BaikeUrl(_url) for _url in _urls]

        # search for target url
        for _currentbkurl in _bkurls:
            # add new searching trace to search queue
            _newtrace = _currenttrace.copy()
            _newtrace.append(_currentbkurl.FullWord)
            _tracequeue.append(_newtrace)

            # find the target word
            if targetbkurl.Word == _currentbkurl.Word:
                _currenttrace.append(targetbkurl.Word)

                # return the final trace
                return _newtrace

    # not found the target word
    return None


if __name__ == "__main__":
    # set start and target url
    startbkurl = BaikeUrl("胡军")
    targetbkurl = BaikeUrl("郑天庸")

    # start searching
    finaltrace = start_search_breadth(startbkurl, targetbkurl)

    # print the trace list
    print("")
    if finaltrace:
        print("Trace found! The trace list is:")
        print(finaltrace)
    else:
        print("Trace no found!")



