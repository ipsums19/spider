
def get_next_target(page):
    stark_link = page.find('<a href')
    if stark_link < 0:
        return None, 0
    start_quote = page.find('""', stark_link)
    end_quote = page.find('""', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

def get_all_links(page):
    urls = []
    while True:
        url, endpos = get_next_target(page)
        if url:
            urls.append(url)
            page = page[endpos:]
        else:
            break
    return urls

def crawl_web(seed):
    tocrawl = [seed]
    crawled = []
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
            tocrawl = tocrawl + get_all_links(getPage(page))
            crawled.append(page)
    return crawled
