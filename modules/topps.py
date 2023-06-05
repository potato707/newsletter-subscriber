import random

import cloudscraper
from bs4 import BeautifulSoup

class topps_newspaper:

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/112.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://uk.topps.com',
        'Alt-Used': 'uk.topps.com',
        'Connection': 'keep-alive',
        'Referer': 'https://uk.topps.com/',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
    }

    def __init__(self,):
        self.scraper = cloudscraper.CloudScraper()

    def subscribe(self, email_address):
        form_key = self.__generate_form_key()
        data = {
            'email': email_address,
            'form_key': form_key,
        }
        self.scraper.cookies.update({'form_key': form_key})
        response = self.scraper.post('https://uk.topps.com/newsletter/subscriber/new/', headers=self.headers, data=data,)
        print(self.scraper.cookies.get_dict()['mage-messages'])

    def __generate_form_key(self,):
        chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        form_key = ''.join(list(map(lambda _: chars[random.randint(1,61)], range(16))))
        return form_key
    
if __name__ == '__main__':
    topps_newspaper().subscribe("d838246554@mymaily.lol")