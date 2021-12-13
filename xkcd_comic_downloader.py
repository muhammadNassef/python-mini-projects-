import requests
from bs4 import BeautifulSoup
import pandas as pd
import sys


def get_current_page(url):
    current_page = requests.get(url=url)
    current_page.raise_for_status()
    return current_page.text


def parse_current_page(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')

    comic_image_url = soup.select('#comic img')

    comic_url = 'https://xkcd.com' + comic_image_url[0].attrs['src'][1:]
    comic_title = comic_image_url[0].attrs['title']

    prev_comic_page = soup.select('.comicNav a')
    prev_comic_url = 'https://xkcd.com' + prev_comic_page[1].attrs['href']

    return [comic_url, comic_title, prev_comic_url]


def save_output_data(comic_image_title_lst):
    df = pd.DataFrame(comic_image_title_lst, columns=('URL', 'Title'))
    datatoexcel = pd.ExcelWriter('data.xlsx')
    df.to_excel(datatoexcel, index=False)
    datatoexcel.save()


def main():
    try:
        url = 'https://xkcd.com'
        comic_image_title_lst = []
        for _ in range(10):  # while not url.endswith('#')
            html_content = get_current_page(url)
            output_data = parse_current_page(html_content)
            comic_image_title_lst.append((output_data[0], output_data[1]))
            print('Reading Previous Page!!')
            url = output_data[2]
        save_output_data(comic_image_title_lst)
        print('End Of The Program!!')
    except Exception as ex:
        print(ex)
        sys.exit(0)


main()
