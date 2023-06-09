import requests
from faker import Faker

class Mileycyrus_newspaper:

    headers = {
        'authority': 'www.mileycyrus.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'accept-language': 'en-US,en;q=0.8',
        'referer': 'https://www.mileycyrus.com/',
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Brave";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'sec-gpc': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    }

    def subscribe(self, email_address):
        data = {
            "field_email_address": email_address
        }

        response = requests.post('https://subs.sonymusicfans.com/submit/', data=data, headers=self.headers)
        print(response.text)
