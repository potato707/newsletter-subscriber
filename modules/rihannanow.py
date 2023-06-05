import requests
import random
from datetime import datetime
from faker import Faker

class Rihannanow_newspaper:

    headers = {
        'authority': 'esp.whdemail.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'accept-language': 'en-US,en;q=0.5',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://www.rihannanow.com',
        'referer': 'https://www.rihannanow.com/',
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Brave";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-user': '?1',
        'sec-gpc': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    }

    def subscribe(self, firstname, lastname, year, month, day, postal_code, email_address):
        data = {
            'email': email_address,
            'ZipCode': postal_code,
            'Country': 'US',
            'DateofBirth': f"%{month} / %{day} / %{year}",
            'name': firstname,
            'LastName': lastname,
            'rocnationupdates': 'Yes',
            'gdpr': 'on',
            'hp': '',
            'list': '29kIAcGbZog2UhQ763DziDkw',
            'subform': 'yes',
            'submit': 'Submit',
        }

        response = requests.post('https://esp.whdemail.com/subscribe', headers=self.headers, data=data)
        print(response)
