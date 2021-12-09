import sys
import requests
import webbrowser
import bs4
from datetime import datetime


def get_inputs():
    # serach words starts from 2nd place, last word will be num of results to be displayed
    search_keywords = sys.argv[1:-1]
    # replace each space with + sign "works better with google search"
    search = '+'.join(search_keywords)
    # include one more sarch result in case of any kind of errors or not working urls
    num_of_results = int(sys.argv[-1]) + 1
    return [search, num_of_results]


def get_search_page():
    try:
        search_keywords = get_inputs()[0]
        num_of_results = get_inputs()[1]
        search_result_page = requests.get(
            f'https://google.com/search?q={search_keywords}&num={num_of_results}')
        search_result_page.raise_for_status()
        return search_result_page
    except Exception as ex:
        print(ex, "\nExit Program now !!")
        sys.exit(0)


def parse_html_result():
    result_set = []
    html = get_search_page()
    soup = bs4.BeautifulSoup(html.content, 'html.parser')
    links = soup.find_all("a")

    for link in links:
        if "url?q=" in link.get('href') and not "webcache" in link.get('href'):
            title = link.find_all('h3')
            if len(title) > 0:
                url = link.get('href').split("?q=")[1].split("&sa=U")[0]
                # check for the correct urls only, and ignore the the corrupted one
                if requests.get(url).status_code == 200:
                    result_set.append(url)
    return result_set


def open_new_browser_tab():
    urls = parse_html_result()
    num_of_tabs = min(get_inputs()[1] - 1, len(urls))
    for url_indx in range(num_of_tabs):
        webbrowser.open_new_tab(urls[url_indx])


def main():
    print(datetime.now())
    open_new_browser_tab()
    print(datetime.now())


main()
