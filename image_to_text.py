# coding: utf-8

# Functions largely based on @INTERESTING_JPG's cvserver
# https://github.com/cmyr/INTERESTING_JPG/blob/master/cvserver.py

import requests
import bs4
import re
import config

class ImageToText(object):
    def __init__(self, image_url):
        self.raw_text = self.response_for_image(image_url)
        self.soup = bs4.BeautifulSoup(self.raw_text) if self.raw_text else None

    def response_for_image(self, image_url):
        base_url = 'http://deeplearning.cs.toronto.edu/api/url.php'
        files = {
            'urllink': ('', image_url),
            'url-2txt': ('', '')
        }
        headers = {
            'connection': 'keep-alive',
            'X-Requested-With': 'XMLHttpRequest',
            'User-agent': "@earthrovingpoet v. 1.0"
        }
        try:
            r = requests.post(base_url, files=files, headers=headers, timeout=5*60)
        except requests.exceptions.ReadTimeout as err:
            print("read time out")
            return
        text = r.text.strip()
        if config.DEBUG:
            print(r)
        if not len(text):
            print('no text in response. status: %d %s' % (r.status_code, r.reason))
            return None
        return text

    def nearest_neighbour(self):
        try:
            return self.soup.li.get_text()
        except AttributeError as err:
            print(err)
            print(self.soup.prettify())
            return None

    def captions(self):
        header = self.soup.find('h4', text=re.compile(r'Top'))
        if not header:
            print('error parsing text')
            print(self.soup.prettify())
            return
        if config.DEBUG:
            print(header.find_next_sibling().prettify())
        next_sib = header.find_next_sibling()
        if next_sib:
            captions = next_sib.find_all('li')
            if captions:
                return [c.text for c in captions]
        print("no captions found?")
        print(self.soup.prettify())

    def top_caption(self):
        all_captions = self.captions()
        if config.DEBUG:
            print(all_captions)
        if all_captions:
            return all_captions[0]

    def tags(self):
        header = self.soup.find('h4', text=re.compile(r'TAGS'))
        if not header:
            print('error parsing text')
            print(self.soup.prettify())
            return
        if config.DEBUG:
            print(header.find_next_sibling())
        tag_list = header.find_next_sibling().get_text(strip=True)
        if tag_list:
            return tag_list.split()
        print("no tags found?")
        print(soup.prettify())




if __name__ == '__main__':
    test_img = 'https://s-media-cache-ak0.pinimg.com/236x/87/14/cb/8714cbbe006f5117a0cab2d42e65ec61.jpg'

    resp = ImageToText(test_img)
    resp.nearest_neighbour()
    resp.captions()
    resp.top_caption()
    resp.tags()