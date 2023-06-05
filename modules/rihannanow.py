import requests
import random
from datetime import datetime
from faker import Faker

def rihannanow(email):
    year = random.randint(1970, 2004)
    month = random.randint(1, 12)
    day = random.randint(1, 28)

    formatted_date = datetime(year, month, day).strftime("%m / %d / %y")

    faker = Faker('en_US')
    name = faker.name()
    firstname, lastname = name.strip().split(' ')[:2]

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

    data = {
        'email': email,
        'ZipCode': faker.postalcode(),
        'Country': 'US',
        'DateofBirth': formatted_date,
        'name': firstname,
        'LastName': lastname,
        'rocnationupdates': 'Yes',
        'gdpr': 'on',
        'hp': '',
        'list': '29kIAcGbZog2UhQ763DziDkw',
        'subform': 'yes',
        'submit': 'Submit',
    }

    print(data)
    response = requests.post('https://esp.whdemail.com/subscribe', headers=headers, data=data)
    print(response.text)
    print(response)

rihannanow('a8c5a07cdc@mymaily.lol')
