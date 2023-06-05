import requests
import time
from faker import Faker

def livenation(email):
    timestamp = int(time.time())
    cookies_expire = timestamp + 1684268245369
    fake = Faker('en_US')

    cookies = {
        'QueueITAccepted-SDFrts345E-V3_livenation': f'EventId%3Dlivenation%26QueueId%3D00000000-0000-0000-0000-000000000000%26RedirectType%3Ddisabled%26IssueTime%3D{timestamp}%26Hash%3Db40c57a9942dc4089bb0d45ff579961463540c0d662a77639b7bff5ff4977618',
        '_dd_s': f'logs=0&expire={cookies_expire}',
    }

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

    params = {
        'email': email,
        'postal_code': fake.postalcode(),
    }
    print(params)
    response = requests.post('https://www.livenation.com/api/newsletter', params=params, cookies=cookies, headers=headers)
    print(response.text)
    print(response)


livenation('ahmedyasser70007@gmail.com')
