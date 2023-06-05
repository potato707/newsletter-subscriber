import requests
import time
from faker import Faker


class Livenation_newspaper:

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.6',
        'Connection': 'keep-alive',
        'Origin': 'https://www.livenation.com',
        'Referer': 'https://www.livenation.com/email/setlist',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-GPC': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Brave";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    def subscribe(self, postal_code, email_address):
        params = {
            'email': email_address,
            'postal_code': postal_code,
        }
        response = requests.post('https://www.livenation.com/api/newsletter', params=params, headers=self.headers)
        print(response)

