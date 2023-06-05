from faker import Faker
import requests


class Paulmccartney_newspaper:
    def subscribe(self, firstname, lastname, email_address):
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/112.0',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.5',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/json',
            'Origin': 'https://www.paulmccartney.com',
            'Connection': 'keep-alive',
            'Referer': 'https://www.paulmccartney.com/newsletter',
            # 'Cookie': '_ga_S233XE4V5W=GS1.1.1685959537.1.0.1685959552.45.0.0; _ga=GA1.1.836979441.1685959538; OptanonConsent=isGpcEnabled=0&datestamp=Mon+Jun+05+2023+13%3A05%3A39+GMT%2B0300+(Eastern+European+Summer+Time)&version=6.35.0&isIABGlobal=false&hosts=&landingPath=https%3A%2F%2Fwww.paulmccartney.com%2Fnewsletter&groups=C0001%3A1%2CC0002%3A0%2CC0003%3A0%2CC0004%3A0; _gcl_au=1.1.1952787643.1685959539; _gid=GA1.2.1310908589.1685959540; _gat_UA-48405904-1=1; _sp_ses.57a9=*; _sp_id.57a9=f3407235-8366-4faa-8a7f-a3318900a441.1685959540.1.1685959540.1685959540.146ccfdf-90de-4561-8090-3102c6f503f8; _ga_QKEQR920KZ=GS1.1.1685959539.1.0.1685959539.60.0.0; _li_dcdm_c=.paulmccartney.com; _lc2_fpi=f1f3a2f769a2--01h25g9zp5m5a5ngvysvhxme9b; _pin_unauth=dWlkPU1EVTFaVGt3T1dFdFlUTm1NaTAwWldReExUaGtZMk10WTJWa01qVmtOelF5WldFNA; _tt_enable_cookie=1; _ttp=VZESygcvD-DnVTBpEGa9J_VU9cy',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            # Requests doesn't support trailers
            # 'TE': 'trailers',
        }

        json_data = {
            'firstName': firstname,
            'lastName': lastname,
            'email': email_address,
            'emailConsent': 'true',
            'country': 'US',
        }

        response = requests.post('https://www.paulmccartney.com/api/mailing-list', headers=headers, json=json_data)
        print(response.text)


if __name__ == '__main__':
    faker = Faker('en_US')
    name = faker.name()
    firstname, lastname = name.strip().split(' ')[:2]
    Paulmccartney_newspaper().subscribe(firstname, lastname, "d838246554@mymaily.lol")
